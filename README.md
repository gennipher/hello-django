# Meu Hello World com Django

...


# Desenvolvimento
## Depdenencias

- [python3](https://www.python.org/downloads/)
- [virtualenv](https://virtualenv.pypa.io/)

### virtualenv

Setup

```sh
virtualenv .venv
```

Entrando no .venv

```sh
# Com fish
. .venv/bin/activate.fish

# Com bash
source .venv/bin/activate
```

### Banco de dados

(ainda não é usado)

```sh
docker run --name hello-postgres -p 5432:5432 -e POSTGRES_PASSWORD=root -d postgres:11
```

### Servidor

```sh
python manage.py runserver
```

### Criando uma aplicação

```sh
(.venv) ~/hello-django/hello$ python manage.py startapp <nome_do_diretorio>
```

### Criando tabelas para nosso modelo no banco de dados

```sh
#Adicionando novo modelo ao banco de dados
(myvenv) ~/djangogirls$ python manage.py makemigrations <nome_do_diretorio


# Aplicando o arquivo de migração ao banco de dados
python manage.py migrate blog
```

### Django.admin / Criando um superusuario (superuser)

Acessar

```
#Entrar na pasta e importar o modelo
blog/admin.py

#Iniciar o servidor web e ir para http://localhost/admin
python manage.py runserver

#Para fazer login, precisa criar um superusuário (superuser)
python manage.py createsuperuser

#Inserir nome de usuário, email e senha.
#Fazer login com as credenciais de superusuário.
```

### Configurando no PythonAnywhere

* Criar conta:
  Acessar: www.pythonanywhere.com e criar conta "Begginer";
* Criar Token de API:
  Selecionar a guia 'API Token' e clicar em 'Create a new API Token';
* Ir para a Dashboard do PythonAnywhere clicando na logo e clicar em 'Bash'

```sh
#Na linha de comando do PythonAnywhere
pip3.6 install --user pythonanywhere

#Executar a ferramenta para configurar a aplicação a partir do GitHub automaticamente
pa_autoconfigure_django.py https://github.com/<your-github-username>/nome-do-repositorio.git
```
