# django-api

## PT-BR

Implementação de uma simples API em `django`, com intuíto de aprender como o framework funciona.

### Tecnologias utilizadas 
-	 Python
-	Django Rest Framework

### Como rodar o programa
- `Acesse o diretório base do projeto no terminal`
- `cd django_api/`
- `python3 manage.py migrate`
- `python3 manage.py runserver`

### Testando a API

- `Acesse o link disponibilizado em seu terminal: http://127.0.0.1:8000/products`
	- Pode ser testado pelo navegador (abre uma view da API), ou pelo POSTMAN 

### Campos de 'Product'
- `name = string (max = 80)`
- `price = float`
-  `active = boolean` 
- `code = int`

### Rotas possíveis

- `/products/`
	- GET
		- Retorna todos os dados criados da tabela
	- POST
		- Cria um novo dado na tabela
	- DELETE
		- Deleta todos os dados da tabela	
- `/products/id`
	- GET
		- Retorna o dado pertencente a aquele id
	- DELETE
		- Deleta o dado pertencente a aquele id
	- PUT
		- Atualiza o dado pertencente a aquele id
- `/products/get-active`
	- Retorna todos os dados que possuam o campo `active = True` 


