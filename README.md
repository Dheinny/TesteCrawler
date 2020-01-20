## Criar a imagem do Docker e subir os serviços
1) docker-compose build crawler
2) docker-compose up db_client

## Criar banco e tabelas
1) Entrar em um client mysql com as seguintes variáveis:
    localhost = 127.0.0.1
    user = root
    password = password
2) rodar o dump que está em teste/crawler/db/queries/dump.sql

## Executar o crawler:
1) Entrar no container através do comando:
    docker-compose run --rm crawler bash
2) De dentro do container, entrar na pasta WebCrawler
    >> cd WebCrawler
3) Executar o scrapy para fazer o crawler:
    >> scrapy runspider WebCrawler/spider/Sympla
