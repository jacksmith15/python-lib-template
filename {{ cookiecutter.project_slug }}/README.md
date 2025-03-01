# {{ cookiecutter.project_slug }}

## Installation

This project is not currently packaged and so must be installed manually.

Clone the project with the following command:

```
git clone https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.git
```

## Development

Install dependencies:

```shell
rye sync
```

Install pre-commit hooks

```shell
pre-commit install
```

Run tests:

```shell
rye run verify
```

# License

This project is distributed under the MIT license.
