[![Build Status](https://travis-ci.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.svg?token=JrMQr8Ynsmu5tphpTQ2p&branch=master)](https://travis-ci.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }})
# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

# Requirements
This package is currently tested for Python 3.6.

# Installation
This project is not currently packaged and so must be installed manually.

Clone the project with the following command:
```
git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git
```

Package requirements may be installed via `pip install -r requirements.txt`. Use of a [virtualenv](https://virtualenv.pypa.io/) is recommended.

# Development
1. Clone the repository: `git clone git@github.com:{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git && cd {{ cookiecutter.project_slug }}`
2. Install the requirements: `pip install -r requirements.txt -r requirements-test.txt`
3. Run `pre-commit install`
4. Run the tests: `bash run_test.sh -c -a`

This project uses the following QA tools:
- [PyTest](https://docs.pytest.org/en/latest/) - for running unit tests.
- [PyFlakes](https://github.com/PyCQA/pyflakes) - for enforcing code style.
- [MyPy](http://mypy-lang.org/) - for static type checking.
- [Travis CI](https://travis-ci.org/) - for continuous integration.
- [Black](https://black.readthedocs.io/en/stable/) - for uniform code formatting.

# License
This project is distributed under the MIT license.
