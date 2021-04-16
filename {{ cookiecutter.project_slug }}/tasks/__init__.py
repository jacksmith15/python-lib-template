from invoke import Collection

from tasks.changelog_check import changelog_check
from tasks.lint import lint
from tasks.release import build, release
{% if cookiecutter.package_type == "docker" -%}
from tasks.run import run
{% endif -%}
from tasks.test import coverage, test
from tasks.typecheck import typecheck
from tasks.verify import verify

namespace = Collection(
    build,
    changelog_check,
    coverage,
    lint,
    release,
    {%- if cookiecutter.package_type == "docker" %}
    run,
    {% endif -%}
    test,
    typecheck,
    verify,
)
