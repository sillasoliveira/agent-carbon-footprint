from google.adk.agents.llm_agent import Agent
from trello import TrelloClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

API_KEY = os.getenv('TRELLO_API_KEY')
API_SECRET = os.getenv('TRELLO_API_SECRET')
TOKEN = os.getenv('TRELLO_TOKEN')


# Consulta a data e a hora do computador.
def get_temporal_context():
    now = datetime.now()
    return now.strftime('%Y/%m/%d %H:%M:%S')


# Cria um cartão na lista A Fazer.
def adicionar_tarefa(
    nome_da_task: str,
    descricao_da_task: str,
    due_date: str
):
    client = TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN
    )

    boards = client.list_boards()
    meu_board = [
        b for b in boards
        if b.name == 'Agente Automatizador'
    ][0]

    listas = meu_board.list_lists()

    minha_lista = [
        l for l in listas
        if l.name.upper() in ['TO DO', 'A FAZER']
    ][0]

    # Converte a data recebida pelo agente.
    # Exemplo:
    # "2026-09-18 18:00"
    # vira
    # "2026-09-18T18:00:00"
    due_datetime = datetime.strptime(
        due_date,
        "%Y-%m-%d %H:%M"
    )

    due_date_formatada = due_datetime.isoformat()

    minha_lista.add_card(
        name=nome_da_task,
        desc=descricao_da_task,
        due=due_date_formatada
    )


# Consulta os cartões, podendo filtrar pela lista.
def listar_tarefas(status: str = "todas"):
    client = TrelloClient(
        api_key=API_KEY,
        api_secret=API_SECRET,
        token=TOKEN
    )

    boards = client.list_boards()
    meu_board = [
        b for b in boards
        if b.name == 'Agente Automatizador'
    ][0]

    listas = meu_board.list_lists()
    status = status.strip().lower()

    if status == "todas":
        listas_filtradas = listas

    elif status == "a fazer":
        listas_filtradas = [
            l for l in listas
            if l.name.upper() in ['A FAZER', 'TO DO', 'TODO']
        ]

    elif status == "em andamento":
        listas_filtradas = [
            l for l in listas
            if l.name.upper() in ['EM ANDAMENTO', 'DOING']
        ]

    elif status in ["concluido", "concluído"]:
        listas_filtradas = [
            l for l in listas
            if l.name.upper() in [
                'CONCLUÍDO',
                'CONCLUIDO',
                'DONE'
            ]
        ]

    else:
        listas_filtradas = listas

    tarefas = []

    for lista in listas_filtradas:
        cards = lista.list_cards()

        for card in cards:
            tarefas.append({
                "nome": card.name,
                "descricao": card.desc,
                "vencimento": card.due,
                "status": lista.name,
                "id": card.id
            })

    return tarefas


# Move um cartão para outra lista do mesmo quadro.
def mudar_status_tarefa(
    nome_da_task: str,
    novo_status: str
) -> str:
    try:
        # 1. Configura o acesso ao Trello.
        client = TrelloClient(
            api_key=API_KEY,
            api_secret=API_SECRET,
            token=TOKEN
        )

        # 2. Encontra o quadro e consulta suas listas.
        boards = client.list_boards()

        meu_board = [
            b for b in boards
            if b.name == 'Agente Automatizador'
        ][0]

        listas = meu_board.list_lists()

        # 3. Relaciona o status solicitado à lista de destino.
        status_map = {
            "a fazer": "A FAZER",
            "em andamento": "EM ANDAMENTO",
            "concluido": "CONCLUÍDO",
            "concluído": "CONCLUÍDO"
        }

        nome_lista_destino = status_map.get(
            novo_status.strip().lower()
        )

        if not nome_lista_destino:
            return (
                "Status inválido. Use: A Fazer, "
                "Em Andamento ou Concluído."
            )

        lista_destino = next(
            (
                lista for lista in listas
                if lista.name.strip().upper()
                == nome_lista_destino
            ),
            None
        )

        if lista_destino is None:
            return (
                f'Lista "{nome_lista_destino}" '
                'não encontrada.'
            )

        # 4. Procura o cartão pelo nome nas listas.
        card_encontrado = None
        lista_origem = None

        for lista in listas:
            cards = lista.list_cards()

            card_encontrado = next(
                (
                    card for card in cards
                    if card.name.strip().lower()
                    == nome_da_task.strip().lower()
                ),
                None
            )

            if card_encontrado is not None:
                lista_origem = lista
                break

        if card_encontrado is None:
            return (
                f'Tarefa "{nome_da_task}" '
                'não encontrada.'
            )

        # 5. Move o cartão.
        card_encontrado.change_list(
            lista_destino.id
        )

        return (
            f'Tarefa "{card_encontrado.name}" movida de '
            f'"{lista_origem.name}" para '
            f'"{lista_destino.name}".'
        )

    except Exception:
        return (
            "Não foi possível confirmar a movimentação. "
            "Confira o cartão no Trello antes de "
            "tentar novamente."
        )


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='Agente de Organização de Tarefas',

    instruction="""
        Você é um agente de organização de tarefas.

        No início da conversa, consulte get_temporal_context
        para saber a data e pergunte quais são as tarefas do dia.

        Suas funções disponíveis:
        1. Adicionar tarefas com nome, descrição e prazo.
        2. Listar todas as tarefas ou filtrar por status.
        3. Mover tarefas entre A Fazer, Em Andamento e Concluído.

        Para criar uma tarefa, pergunte as informações que faltarem.
        Não invente um prazo que o usuário não informou.

        Ao chamar adicionar_tarefa, envie o prazo
        obrigatoriamente no formato YYYY-MM-DD HH:MM.

        Para mudar o status, use o nome exato do cartão.
        Se precisar consultar os nomes, use listar_tarefas.

        Execute somente ações para as quais tenha ferramentas
        disponíveis.

        Não afirme ter alterado o Trello sem executar
        a ferramenta correspondente com sucesso.

        Se houver falha ou resultado incerto,
        informe isso ao usuário.

        Você ainda não possui uma ferramenta
        para excluir tarefas.
    """,

    tools=[
        get_temporal_context,
        adicionar_tarefa,
        listar_tarefas,
        mudar_status_tarefa,
    ],
)
