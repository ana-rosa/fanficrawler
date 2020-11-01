# fanficrawler

O fanficrawler é um sistema que visa realizar a raspagem de dados do site fanfiction.net usando Scrapy e uma aplicação web usando Django que consome o csv dos dados raspados, inserindo-os em um banco de dados para disponibilizá-los.

## Como usar

Para intalar as dependências, execute o seguinte comando:
```
$ pip install -r requirements.txt
```

Para rodar o crawler e raspar os metadados das fanfics, exportando para um arquivo CSV, execute:
```
$ scrapy crawl ffnet -t csv -o ficteste.csv
```


