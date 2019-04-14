# Flask Playground

[![Build Status](https://travis-ci.org/willianantunes/flask-playground.svg?branch=master)](https://travis-ci.org/willianantunes/flask-playground)
[![Maintainability](https://api.codeclimate.com/v1/badges/ac42632e5d323914c5a4/maintainability)](https://codeclimate.com/github/willianantunes/flask-playground/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ac42632e5d323914c5a4/test_coverage)](https://codeclimate.com/github/willianantunes/flask-playground/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

---

As the name says, it's a playground project to see some power of [Flask](https://github.com/pallets/flask).

## Details

It's based on [GitHub GraphQL API v4](https://developer.github.com/v4/). Try it out on:

- https://developer.github.com/v4/explorer/

To get your keys:

- https://developer.github.com/v4/guides/forming-calls/#authenticating-with-graphql

## Preparing your dev environemnt

This project uses `pipenv`, so you must have it (see how [here](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today)). [It is the recommended tool to work with dependency management by python.org](https://packaging.python.org/guides/tool-recommendations/).

At the root of project, issue the following command:

    pipenv install --dev --ignore-pipfile

The option `--ignore-pipfile` is used to guarantee that you get the dependencies from the versions presented in `Pipfile.lock`. Thus it will make sure you get the same stuff as me :)

## Running it

Do not forget to update `WA_GITHUB_API_TOKEN` with your API Token.

Execute the following command:

    pipenv run python init.py

Or if you prefer:

    docker-compose up

## Tests

You can run directly with `pytest`

    pipenv run pytest

Or with `tox`:

    pipenv run tox

## References

- [Flask Web Development: Developing Web Applications with Python](https://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1449372627)
    - https://github.com/miguelgrinberg/flasky
    - https://github.com/miguelgrinberg/oreilly-intro-to-flask-video
    - https://github.com/miguelgrinberg/oreilly-flask-apis-video
- [Fluent Python: Clear, Concise, and Effective Programming](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008)
    - https://github.com/fluentpython
