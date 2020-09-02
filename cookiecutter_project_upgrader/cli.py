import click
import json
import os
from pathlib import Path
from typing import Optional, Tuple

from cookiecutter_project_upgrader.logic import update_project_template_branch


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option('--context-file', '-c', type=click.Path(file_okay=True, readable=True, allow_dash=True),
              default="docs/cookiecutter_input.json", help="Default: docs/cookiecutter_input.json")
@click.option('--branch', '-b', default="cookiecutter-template", help="Default: cookiecutter-template")
@click.option('--interactive', '-i', is_flag=True,
              help="Enter interactive mode. Default behaviour: skip questions, use defaults.")
@click.option('--merge-now', '-m', type=bool, default=None,
              help="Execute a git merge after a successful update, default: ask if interactive, otherwise false.")
@click.option('--push-template-branch-changes', '-p', type=bool, default=None,
              help="Push changes to the remote Git branch on a successful update, "
                   "default: ask if interactive, otherwise false.")
@click.option('--exclude', '-e', type=str, multiple=True,
              help='Git pathspecs to exclude from the update commit, e.g. -e "*.py" -e "tests/".')
def main(context_file: str, branch: str,
         interactive: bool, merge_now: Optional[bool],
         push_template_branch_changes: Optional[bool],
         exclude: Tuple[str, ...]):
    """Upgrade projects created from a Cookiecutter template"""
    context = _load_context(context_file)
    project_directory = os.getcwd()
    update_project_template_branch(context,
                                   project_directory,
                                   branch,
                                   merge_now,
                                   push_template_branch_changes,
                                   exclude,
                                   interactive)


def _load_context(context_file: str):
    try:
        context_str = Path(context_file).read_text(encoding="utf-8")
    except FileNotFoundError:
        click.echo(f"Context file not found at: {context_file}\n"
                   f"Make sure you are in the right directory")
        exit(1)
    context = json.loads(context_str)
    return context
