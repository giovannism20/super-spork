Para utilizar este projeto você vai precisar da versão 3.12.3 e do CURL.

Estando no repositório do projeto execute:
```python3 -m venv .venv```
```source .venv/bin/activate```
```python3 -m pip install -r requirements.txt```

E então:
```fastapi dev app/main.py```

Para vizualizar a documentação no Swagger:
http://127.0.0.1:8000/docs

Com o processo do FastAPI executando em segundo plano é possível realizar as operações de CRUD (Create, Read, Update e Delete).

Para criar:
```fastapi dev app/main.py```

Para ler:
```fastapi dev app/main.py```

Para atualizar:
```fastapi dev app/main.py```

Para deletar:
```fastapi dev app/main.py```
