from click.testing import CliRunner

from cookiecutter_project_upgrader.cli import main


def invoke(arguments):
    runner = CliRunner()
    return runner.invoke(main, arguments)


def invoke_successful(arguments):
    result = invoke(arguments)

    if result.exit_code:
        raise result.exception


def invoke_failing(arguments):
    result = invoke(arguments)

    if not result.exit_code:
        raise RuntimeError("Unexpected success:\n{}".format(result.stdout))


def test_cli():
    invoke_successful(["--help"])

    invoke_failing(["--context-file", "./non-existing-file.py"])
