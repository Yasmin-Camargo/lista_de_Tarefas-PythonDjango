# Lista de Tarefas - Python Django - TreinaWeb
Projeto utilizando o framework Django.

## Instalação

### Criar um ambiente virtual
```bash
python -m venv .venv

.venv\Scripts\activate
```

### Instalar o Django
```bash
pip install django
```

### Criar um projeto Django
```bash
django-admin startproject setup .
```

### Criar uma aplicação Django
```bash
python manage.py startapp todos
```

## Executando 
```bash
python manage.py runserver
```

## Migrações
Define que uma tabela tem que ser criada no banco de dados.

### criar migração
```bash
python manage.py makemigrations
```

### aplicar a migração
```bash
python manage.py migrate
```

## Boas práticas
Não deixar infomações expostas no arquivo settings.py, isolar configurações: 
```bash
pip install python-decouple
```

Converter string de padrão de conexão Django:
```bash
pip install dj-database-url
```

Auto formatação do códgo: 
```bash
pip install black

black .
```

#### automatizar: 

Ctrl + Shift + P, selecione Workspace Settings (JSON)
```bash
{ 
"editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "editor.defaultFormatter": "ms-python.black-formatter"
}
```


# Tópicos abordados
- Criando estrutura base de um projeto Django e entendendo fluxo de execução
- Modelos, views e migrações
- Isolando configurações do projeto e configuração de formatação de código com black
- Criação das páginas, templates, listagem e consultas no banco de dados
- Cadastro de tarefas utilizando class based views
- Django crispy forms para gerar formulários de forma automatizada
- Herança de templates para reaproveitamento de código
- Update de informações
