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

### As URLs em Django

Abra o arquivo:
```sh
hello/urls.py
```

Você vai encontrar a URL do admin que visitou antes.
```sh
path('admin/', admin.site.urls),
```

Significa que para cada URL que começa com `admin/`, O Django encontra um view correspondente.

Crie um novo arquivo chamado `urls.py` no diretório `blog`.

```sh
#Importa do Django a função url e todas as views do aplicativo blog
from django.urls import path
from . import views

#Adicionar o primeiro padrão de URLs.
#Atribuir uma view chamada post_list à URL raiz.
#Este padrão faz com que o Django ignore o nome de domínio localhost que antecede o caminho completo da URL, informando que views.post_list e o lugar correto onde ir se alguém entra no site.
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

### Django Views

São funções Python que extraem informações do `model` criado e entrega a um `template`.

Abrir o arquivo `blog/views.py`:
```sh
from django.shortcuts import render

#Criar uma view simples:
def post_list(request):
    return render(request, 'blog/post_list.html', {})

#A função def chamada post_list que leva a solicitação e irá retornar o valor que recebe ao chamar outra função render que irá renderizar o modelo blo/post_list.html
```

### Primeiro Template

Criar um diretório chamado `templates` dentro do diretório `blog`.
Criar outro diretório chamado `blog` dentro do diretório `templates`.

```
blog
└───templates
    └───blog
```
Criar o arquivo `post_list.html` dentro do diretório `blog/templates/blog`.

Nesse `post_list.html` você pode editar do jeito que quiser, usando HTML, CSS, ...

### QuerySet

É um conjunto de busca. Em essência, é uma lista de objetos de um dado modelo.
Permite que leia os dados a partir de uma base de dados, filtre e ordene.

### Shell do Django

Abra o terminal:
```sh
(myvenv) ~/djangogirls$ python manage.py shell

#O resultado deve ser:
(InteractiveConsole)
>>>

#Esse é o console interativo do Django
#Vamos importar nosso modelo Post dentro de blog.models
>>> from blog.models import Post

#Vamos tentar mostrar todas as nossas postagens que criamos na interface do Django admin
>>> Post.objects.all()
<QuerySet [<Post: my post title>, <Post: another post title>]>
```

### Criando um objeto

```sh
#Criando um objeto Post no banco de dados:
>>> Post.objects.create(author=me, title='Sample title', text='Test')

#Vamos importar o modelo User:
>>> from django.contrib.auth.models import User

#Para consultar quais usuários temos no banco de dados:
>>> User.objects.all()
<QuerySet [<User: Ola>]>
#Vai imprimir o superusuário que criamos
>>> me = User.objects.get(username='jennifer')

#Agora podemos criar nosso post:
>>> Post.objects.create(author=me, title='Texto Simples', text='Test')
<Post: Texto Simple>

#Para ver se funcionou:
>>> Post.objects.all()
<QuerySet [<Post: my post title>, <Post: another post title>, <Post: Sample title>]>
```

### Filtrando objetos

Um recurso importante do QuerySet é poder filtrar.

```sh
#Se quisermos buscar todas as postagens escritas pelo usuário jennifer:
>>> Post.objects.filter(author=me)
<QuerySet [<Post: Sample title>, <Post: Post number 2>, <Post: Post number 3>, ...]>

#Se quisermos todos os posts que contenham a palavra title no campo title:
>>> Post.objects.filter(title__contains='title')
<QuerySet [<Post: Sample title>, <Post: 4th title of post>]>

#Pode pegar uma lista com todos os posts publicados, com uma published_date:
>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet []>
```

O post que criamos pelo console do Python ainda não foi publicado. Vamos publicá-lo:

```sh
#Buscar a instância do post que queremos publicar:
>>> post = Post.objects.get(title="Sample title")

#Publicar com método publish:
>>> post.publish()

#Agora buscar novamente a lista de posts publicados:

>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: Sample title>]>
```

### Ordenando objetos

```sh
#Ordenar as postagens pelo campo created_date:
>>> Post.objects.order_by('created_date')
<QuerySet [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]>

#Invertendo a ordem adicionando - no inicio:
>>> Post.objects.order_by('-created_date')
<QuerySet [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]>
```

### Consultas complexas com encadeamento de métodos

Alguns métodos em `Post.objects` retornam um QuerySet. Estes podem ser invocados em um QuerySey, que resultará em um novo QuerySet. Assim pode combinar seus efeitos encadeando eles juntos:

```sh
>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
<QuerySet [<Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>, <Post: Sample title>]>
```

`>>> exit() ` Para fechar o terminal

### Dados dinâmicos em templates

Em `blog/views.py`:

```sh
from django.shortcuts import render
from .models import Post
```

### QuerySet

Usamos para pegar os posts reais do modelo `Post`.

Adicionar:
```sh
from django.utils import timezone
```

Vamos colocar dentro do arquivo `blog.views.py` na função `def postlist(request)` o seguinte código._

```sh
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
```
Agora só falta passar a QuerySet `posts` para o template.

Criamos uma variável para nosso QuerySet `posts`.

Na função `render` temos um parâmetro `request`, que é tudo o que recebemos do usuário através da Internet, e um arquivo de template `blog/post_list.html`.

O último parâmetro `{}` é um lugar em que podemos acrescentar algumas coisas para o template usar. Precisamos nomear os parâmetros `{'posts': posts}`, onde o que está entre `''`é uma string.

Nosso `blog/views.py` vai ficar:

```sh
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
  posts = Post.objects.filter(published_date_lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html',{'posts': posts})
```

### Templates do Django

O Django vem com algumas tags de template, elas nos permitem transformar código similar a Python em código HTML.

Para mostrar uma variável em um template do Django, usamos chaves duplas com o nome da variável: `{{ posts }}`.


