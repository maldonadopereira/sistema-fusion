# Fusion
- Página Web com Django utilizando conceitos de Class Based Views, baseado no template Fusion, com bootstrap 4.
- Criado com base em conhecimentos adquiridos no curso Programação Web com Python e Django Framework: Essencial, na plataforma Udemy:

Template disponível em: 
 - https://usebootstrap.com/theme/fusion-free-lite


## Dependências

- asgiref==3.5.0
- dj-static==0.0.6
- Django==4.0.4
- django-stdimage==5.3.0
- gunicorn==20.1.0
- Pillow==9.1.0
- psycopg2-binary==2.9.3
- sqlparse==0.4.2
- static3==0.7.0

## Instalação

1. clonar o repositório em algum diretório escolhido:
```bash
git clone https://github.com/maldonadopereira/fusion.git
```

2. Criar uma venv, no exemplo a seguir será utilizado o pipenv:
```bash
pipenv shell
```

3. Instalar as dependências:
```bash 
pipenv sync 
```

4. Sincronize a base de dados:

```bash
python manage.py migrate
```

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

```bash
python manage.py runserver
```