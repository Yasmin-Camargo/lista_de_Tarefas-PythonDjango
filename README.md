# Lista de Tarefas - Python Django - TreinaWeb
Projeto utilizando o framework Django.

Tutorial utilizado: https://www.youtube.com/playlist?list=PLZ5WLsqE1WPGPA0Z0H1XB8P6UwgTHOSaf

# Tópicos Abordados
- Estruturação de um projeto Django e compreensão do fluxo de execução.
- Implementação de modelos, views e migrações de banco de dados.
- Isolamento das configurações do projeto e formatação automatizada do código com Black.
- Criação de páginas, templates e realização de consultas e listagens no banco de dados.
- Cadastro de tarefas utilizando Class-Based Views (CBVs).
- Utilização do Django Crispy Forms para a geração automatizada de formulários.
- Aplicação de herança de templates para reaproveitamento de código.
- Funcionalidades de atualização (Update) e exclusão (Delete) de informações.
- Implementação completa de um sistema CRUD (Create, Read, Update, Delete).
- Conclusão de tarefas e ordenação de itens cadastrados.

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



