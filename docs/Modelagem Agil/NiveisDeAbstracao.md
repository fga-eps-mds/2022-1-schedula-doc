# Backlog

### Histórico da Revisão
| Data       | Versão | Descrição                    | Autor                   |
| ---------- | ------ | ---------------------------- | ----------------------- |
| 09/07/2022 | 0.1    | Criação do documento         | Pedro Henrique          |
| 09/07/2022 | 0.2    | Adicionado Epicos 01, 02, 03 | Eduardo Pícolo, Roberto |

## Épicos

O Épico é um quantidade elevada de trabalho que pode ser dividido em tarefas específicas (chamadas de estórias de usuário) com base nas necessidades / solicitações dos clientes ou usuários finais.[1]

| Épico | Descrição  |
| ----- | ---------- |
| E01   | Usuários   |
| E02   | Chamados   |
| E03   | Relatórios |
| E04   | Tutoriais  |
| E05   | Eventos    |

## Features

O objetivo de uma Feature é realizar um Épico, podem haver 1 ou mais features agrupados sob um Épico. Uma Feature agrupa 1 ou muitas User Stories (estórias equivalem a requisitos funcionais) que estão no contexto da Feature.
Uma Feature faz parte de um Módulo, e possui seus Requisitos Funcionais e suas Regras de Negócio. [2]


| Épico | Feature | Descrição                |
| ----- | ------- | ------------------------ |
| E01   | F01     | Cadastro de Usuários     |
| E01   | F02     | Autenticação de Usuários |
| E02   | F03     | Cadastro de Chamados     |
| E03   | F04     | Dashboard                |
| E03   | F05     | Exportar relatórios      |
| E04   | F06     | Cadastro de tutoriais    |
| E04   | F07     | Download de tutoriais    |

## User stories

Uma estória de usuário é uma curta e simples descrição de uma tarefa expressa na perspectiva da pessoa que deseja essa nova funcionalidade, normalmente um usuário ou cliente do sistema (Wiegers e Beatty, 2013).

Serão escritos da seguinte forma:

Eu, como um < TIPO DE USUÁRIO >, desejo < OBJETIVO > para que eu consiga < UMA RAZÃO >

| User story | Descrição                                                                                                                                         | Critérios de aceitação                                                                                                                                                                                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US01       | Eu, como usuário, desejo me cadastrar no sistema para eu conseguir usufruir de todas as funcionalidades do sistema                                | <ul>                   <li>Deve ser possivel inserir um novo usuário no sistema;</li> <li>Deve ser possivel editar um usuário já cadastrado;</li> <li>Deve ser possivel excluir um usuário já cadastrado;</li> </ul>                                                                                                   |
| US02       | Eu, como usuário, desejo acessar o sistema com minhas credenciais para que eu conseguir utilizar todas as funcionalidades do sistema              | <ul>                   <li>Deve ser possivel realizer a autenticação com credenciais previamentes cadastradas;</li> </ul>                                                                                                                                                                                              |
| US03       | Eu, como usuário, desejo cadastrar Chamados para que seja possivel fazer o controle e organizar atendimentos dos mesmos                           | <ul>                   <li>Deve ser possivel inserir um novo chamado no sistema;</li> <li>Deve ser possivel editar um chamado já registrado;</li> <li>Deve ser possivel excluir um chamado já registrado;</li> <li>Deve ser possivel listar todos os chamados;</li> <li>Deve ser possivel filtrar chamados;</li> </ul> |
| US04       | Eu, como (admin ?), gostaria de, ao final do meu dia, acessar um dashboard com um resumo dos chamados em determinados periodos.                   | <ul><li> Deve ser possível inserir informações sobre o arquivo enviado (título, descrição, etc...).</li> <li>Deve ser possível inserir textos puros (não arquivos) e links ao invés de um arquivo.</li></ul>                                                                                                           |
| US05       | Eu, como usuario, gostaria de aplicar diversos filtros sobre o dashboard para melhorar a vizualização dos dados                                   | <ul><li> Ter filtros de intervalo de datas</li><li> Ter filtros por região</li><li> Ter filtros por pessoas</li></ul>                                                                                                                                                                                                  |
| US06       | Eu, como usuario, gostaria de gerar e exportar relatorios a partir dos dados (filtrados ou não) do dashboard                                      | <ul><li>Ter um botão unico e visível</li></ul>                                                                                                                                                                                                                                                                         |
| US07       | Eu, como usuário, gostaria de fazer o upload de arquivos e textos de tutoriais para que possam ser consultados posteriormente em caso de dúvidas. | <ul><li> Deve ser possível fazer o upload de arquivos de texto (txt, pdf, docx, etc...).</li> <li> Deve ser possível inserir informações sobre o arquivo enviado (título, descrição, etc...).</li> <li>Deve ser possível inserir textos puros (não arquivos) e links ao invés de um arquivo.</li></ul>                 |
| US08       | Eu, como usuário, gostaria de fazer a remoção de tutoriais que cadastrei anteriormente.                                                           | <ul><li> Deve existir uma caixa de confirmação na exclusão de um tutorial.</li><li>Deve ser simples como clicar em um botão de remover próximo à listagem do tutorial.</li></ul>                                                                                                                                       |
| US09       | Eu, como usuário, gostaria de poder editar informações sobre os tutoriais já cadastrados para manter suas informações atualizadas.                | <ul><li> Deve ser editado em uma tela semelhante ou igual a de cadastro de tutoriais.</li><li> Deve ser possível editar o arquivo enviado mantendo as informações cadastradas (descrição, etc...)</li><li> Deve ser possível editar as informações cadastradas mantendo o arquivo enviado.</li></ul>                   |
| US010      | Eu, como usuário, gostaria de listar os tutoriais cadastrados anteriormente para que possa baixa-los.                                             | <ul><li> Deve ser possível filtrar pela descrição (se existente) e título.</li><li> Deve possuir paginação.</li></ul>                                                                                                                                                                                                  |
| US011      | Eu, como usuário, gostaria de baixar os tutorias que cadastrei anteriormente para poder revê-los.                                                 | <ul><li> Deve ser simples como clicar em um botão de baixar próximo à listagem do tutorial.</li></ul>                                                                                                                                                                                                                  |
<h1>Pontuação: Não calculada ainda.</h1>

## Referências

[1] REHKOPF, Max. Histórias de usuários com exemplos e template. Atlassian. Disponível em: aqui. Acesso em: 17 de Agosto de 2021.

[2] VENTURA, Plínio. Epic, Feature e User Story (Épico, Funcionalidade e História de Usuário). Até o momento. Disponível em: aqui. Acesso em: 17 de Agosto de 2021.