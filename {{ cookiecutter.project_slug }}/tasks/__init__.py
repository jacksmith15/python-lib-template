from invoke import Collection

from tasks.changelog_check import changelog_check
from tasks.lint import lint
from tasks.publish import publish
{% if cookiecutter.package_type == "docker" -%}
from tasks.run import run
{% endif -%}
from tasks.test import coverage, test
from tasks.typecheck import typecheck
from tasks.verify import verify

namespace = Collection(
    changelog_check,
    coverage,
    lint,
    publish,
    {%- if cookiecutter.package_type == "docker" %}
    run,
    {% endif %}
    test,
    typecheck,
    verify,
)
