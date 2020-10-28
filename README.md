
# pontoTel.desafio.backend

Códigos relacionados ao desafio para uma vaga na PontoTel

##
**Autor**: Nivardo Albuquerque

## Resumo

API implementada em FLASK com banco de dados POSTGRES com orm SQLALCHEMY.


## Tecnlogias

* Validação com marshmallow.
* Python 3.7
* Framework Flask
* Mensageiria com zeromq
* Openapi 3.0
* YahooQuery para consulta de dados
* Migrações com o Alembic
* Pytest para testes automatizados


## Quickstart
Para rodar o serviço deve-se:
* Instalar as dependências
```
pip install -r requirements.txt
```

* Iniciar o zeromq
```
python3 -m app.components.zeromq
```

* Iniciar a API Flask
```
gunicorn app:app --bind 0.0.0.0:3000 --workers 3
```





### Testes
Para rodar os testes

```
STAGE=test pytest
```


