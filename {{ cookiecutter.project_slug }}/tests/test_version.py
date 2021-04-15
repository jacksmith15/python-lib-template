import pytest
import toml

import changelog
import {{ cookiecutter.package_name }} as package


def test_version_matches_pyproject():
    with open("pyproject.toml", "r") as file:
        pyproject = toml.loads(file.read())
    assert pyproject["tool"]["poetry"]["version"] == package.__version__


@pytest.mark.xfail(strict=True, reason="No release has yet been made")
def test_version_matches_changelog():
    log = changelog.load_from_file("CHANGELOG.md")
    assert log.latest_version == package.__version__
