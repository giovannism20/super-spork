Para utilizar este projeto você vai precisar da versão 3.12.3 e do CURL.

Estando no repositório do projeto execute:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

E então:
```
fastapi dev app/main.py
```

Para vizualizar a documentação no Swagger:
http://127.0.0.1:8000/docs

Com o processo do FastAPI executando em segundo plano é possível realizar as operações de CRUD (Create, Read, Update e Delete).

Para criar tarefa:
```
curl -X POST http://127.0.0.1:8000/todos
    -H 'Content-Type: application/json'
    -d '{
            "title":"Título da Tarefa",
            "description.":"Descrição da Tarefa"
        }'
```

Para listar tarefa:
```
curl -X GET http://127.0.0.1:8000/todos
```

Para obter tarefa por ID:
```
curl -X GET http://127.0.0.1:8000/todos/{id}
```

Para atualizar tarefa por ID:
```
curl -X PUT http://127.0.0.1:8000/todos/{id}
    -H 'Content-Type: application/json'
    -d '{
            "title":"Novo Título da Tarefa",
            "description.":"Nova Descrição da Tarefa"
        }'
```

Para deletar tarefa por ID:
```
curl -X DELETE http://127.0.0.1:8000/todos/{id}
```
