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
