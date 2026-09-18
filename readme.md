<!--START_SECTION:header-->
<div align="center">
  <p align="center">
    <img 
      alt="DIO Education" 
      src="https://raw.githubusercontent.com/digitalinnovationone/template-github-trilha/main/.github/assets/logo.webp" 
      width="100px" 
    />
    <h1>Agente de Organização de Tarefas com Google ADK e Trello</h1>
  </p>
</div>
<!--END_SECTION:header-->

<p align="center">
  <img src="https://img.shields.io/static/v1?label=DIO&message=Education&color=E94D5F&labelColor=202024" alt="DIO Project" />
  <img src="https://img.shields.io/static/v1?label=Nivel&message=Basico&color=E94D5F&labelColor=202024" alt="Nivel">
</p>

## Sobre o projeto

Este projeto foi desenvolvido de forma orientada durante meus estudos na DIO.

A proposta da atividade foi ter um primeiro contato prático com o desenvolvimento de agentes de Inteligência Artificial, entendendo melhor como eles funcionam e como podem utilizar ferramentas para realizar ações fora do próprio modelo de IA.

Durante as aulas, acompanhei a construção de um agente de organização de tarefas utilizando Python, Google Agent Development Kit (ADK), Gemini e Trello.

Além de acompanhar a implementação apresentada no curso, fiz alguns testes e alterações no agente para entender melhor o funcionamento do código e o fluxo entre o usuário, o modelo de IA, as funções em Python e o Trello.

## O que eu procurei entender com o projeto

Meu principal objetivo com esta atividade não foi desenvolver um sistema completo ou pronto para produção, mas entender os conceitos básicos por trás de um agente de IA.

Durante o projeto, pude observar na prática:

- como um agente recebe uma solicitação em linguagem natural;
- como o modelo interpreta o que o usuário está pedindo;
- como são definidas instruções para orientar o comportamento do agente;
- como funções em Python podem ser disponibilizadas como ferramentas;
- como o agente escolhe uma ferramenta de acordo com a solicitação;
- como uma ferramenta pode se comunicar com um serviço externo, como o Trello;
- como o resultado dessa ação retorna para o agente.

## Funcionalidades trabalhadas

O agente desenvolvido durante a atividade consegue trabalhar com algumas ações básicas de organização de tarefas:

- consultar a data e a hora atual;
- adicionar uma tarefa;
- adicionar descrição e prazo;
- consultar tarefas cadastradas;
- filtrar tarefas de acordo com o status;
- movimentar uma tarefa entre as listas A Fazer, Em Andamento e Concluído.

## Estrutura básica do agente

Durante o projeto foram utilizadas quatro funções principais.

### `get_temporal_context`

Consulta a data e a hora do computador para que o agente tenha uma referência do momento atual.

Isso permite interpretar solicitações como:

`Estudar Python hoje às 14:00.`

### `adicionar_tarefa`

Recebe as informações da tarefa e utiliza a integração com o Trello para criar um cartão na lista A Fazer.

### `listar_tarefas`

Consulta os cartões existentes no Trello e permite que o agente apresente as tarefas cadastradas.

### `mudar_status_tarefa`

Permite localizar uma tarefa e movimentá-la entre as listas A Fazer, Em Andamento e Concluído.

## Tecnologias utilizadas durante a atividade

- Python
- Google Agent Development Kit (ADK)
- Gemini
- Trello
- py-trello
- python-dotenv
- Git
- GitHub

## O que aprendi

Antes desta atividade, minha visão de um agente de IA estava muito ligada apenas à ideia de conversar com uma Inteligência Artificial.

O projeto me ajudou a entender melhor que um agente também pode receber instruções, analisar uma solicitação, escolher uma ferramenta disponível e utilizar essa ferramenta para realizar uma ação.

Um dos pontos que achei mais importantes foi entender a diferença entre o modelo de IA e as funções do programa.

O modelo interpreta o pedido do usuário, mas são as ferramentas desenvolvidas em Python que realizam determinadas ações, como consultar ou adicionar uma tarefa no Trello.

Também tive contato com conceitos que ainda estou aprendendo, como APIs, variáveis de ambiente, integração entre serviços e tratamento de erros.

## Testes e dificuldades encontradas

Durante os testes também encontrei alguns erros, o que fez parte do processo de aprendizado.

Entre eles estiveram erros relacionados ao formato de data enviado ao Trello e limites de utilização da API do Gemini no plano gratuito.

Esses problemas ajudaram a perceber que, além da lógica do agente, uma aplicação desse tipo depende da comunicação correta entre diferentes serviços e das regras de cada API utilizada.

## Considerações finais

Este foi um projeto de estudo desenvolvido de forma orientada na DIO e representa meu contato inicial com a construção de agentes de IA.

O objetivo foi principalmente entender a lógica por trás desse tipo de aplicação e começar a desenvolver uma base para continuar estudando Python, APIs, Inteligência Artificial e desenvolvimento de agentes.
