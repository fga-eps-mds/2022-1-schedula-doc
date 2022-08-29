# Como Contribuir

## Issues

Verifique se já não existe uma issue que trata do mesmo problema.
A issue deve ser clara no título e descrição.
Adicione labels que representam o tipo de artefato que deve ser desenvolvido.
As issues devem apresentar a estrutura segundo o template.

`<título da tarefa>`

## Branchs

As branchs devem ser criadas a partir da branch principal e corresponder a alguma das issues.
Devem ser nomeadas, sem acentos e underlines (_) ao invés de espaço seguindo a estrutura:

`<numero_da_issue>`_`<título simplificado da issue fonte>`

## Commits

Os commits devem ter títulos significativos.
Com a seguinte estrutura:

`<descrição pequena e concisa>`

Se o commit teve mais de um autor deve possuir co-autor.

```bash
$ git commit -m "<descrição pequena e concisa>.


Co-authored-by: name <name@example.com>
Co-authored-by: another-name <another-name@example.com>"
```

## Pull requests

O título e o comentário devem ser claros.
O pull request deve ser relacionado a alguma issue.
Adicione labels que representem o tipo de artefato.
Cada pull request deve possuir ao menos dois revisores.
Cada revisor deve comentar uma checklist com seus critérios de revisão e se foram aprovados.

`#<número_da_issue>` `<título da issue fonte>`.

## Testando a wiki localmente

### Pre-Requisitos

  - Python 3.x
  - MkDocs
  - mkdocs-material

    [Como instalar](https://squidfunk.github.io/mkdocs-material/getting-started/)


### Como rodar

  - Executar o comando: `mkdocs serve`
  - Abrir o navegador e acessar a URL: `http://localhost:8000`

    Obs: Após a instalação, caso o comando __mkdocs__ não seja reconhecido, talvez seja necessário reiniciar o perfil do usuário ou até mesmo o computador.
