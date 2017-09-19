=================
Pyhton-Dotenv-Run
=================

Run command with environment variables populated by python-dotenv_.


Installation
============

If using Pipenv_::

    pipenv install --dev python-dotenv-run


Otherwhise::

    pip install python-dotenv-run


Instruction onwards assumes you use Pipenv_. If you do not, simply drop the
``pipenv run`` prefix in all commands.


Usage
=====

Say you have a Flask app in a file named ``webapp.py``::

    import flask

    app = flask.Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello World!"

Add a file named ``.env`` alongside with the project::

    FLASK_APP=webapp.py

After installing dependencies, you can run it like this::

    pipenv run dotenv-run flask run


.. _python-dotenv: https://github.com/theskumar/python-dotenv
.. _Pipenv: https://github.com/kennethreitz/pipenv
