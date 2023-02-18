Django Text to Html Convertor
=============

Setup
-------------

The first thing to do is to clone the repository:

```sh
$ git https://github.com/thistermeh/django_text_to_html_convertor.git
$ cd django_text_to_html_convertor
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv -p python3 texttohtmlenv
$ source ~/texttohtmlenv/bin/activate
```

Then install the dependencies:

```sh
(texttohtmlenv)$ pip3 install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:

```sh
(texttohtmlenv)$ python manage.py runserver
```
The convertor will be available at `http://127.0.0.1:8000/`.
