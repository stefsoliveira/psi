# psi

## Prerequisites
This project uses pipenv to manage the dependencies and some build steps
in order to keep track of specific versions.

Please make sure you have installed:
* [pipenv](https://pipenv.pypa.io/en/latest/)
* [pyenv](https://github.com/pyenv/pyenv)

## Install all dependencies
```bash
pipenv run install --dev
```

## Run tests
To run all the tests:
```bash
pipenv run test
```

### Run unit-tests
```bash
pipenv run unit-tests
```

### Run integration-tests
```bash
pipenv run integration-tests
```

## Run linter
```bash
pipenv run linter
```
