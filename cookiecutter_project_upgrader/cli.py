import click
import json
import os
from pathlib import Path
from typing import Optional

from cookiecutter_project_upgrader.logic import update_project_template_branch


@click.command()
@click.option('--context-file', '-c', type=click.Path(file_okay=True, readable=True, allow_dash=True),
              default="docs/cookiecutter_input.json", help="Default: docs/cookiecutter_input.json")
@click.option('--branch', '-b', default="cookiecutter-template", help="Default: cookiecutter-template")
@click.option('--merge-now', '-m', type=bool, default=None,
              help="Execute a git merge after a successful update, default: ask if interactive, otherwise false.")
@click.option('--push-template-branch-changes', '-p', type=bool, default=None,
              help="Push changes to the remote Git branch on a successful update, "
                   "default: ask if interactive, otherwise false.")
@click.option('--exclude', '-e', type=str, default=None,
              help="Git pathspecs to exclude files")
def main(context_file: str, branch: str,
         merge_now: Optional[bool],
         push_template_branch_changes: Optional[bool],
         exclude: str):
    """Upgrade projects created from a Cookiecutter template"""
    context = _load_context(context_file)
    project_directory = os.getcwd()
    update_project_template_branch(context,
                                   project_directory,
                                   branch,
                                   merge_now,
                                   push_template_branch_changes,
                                   exclude)


def _load_context(context_file: str):
    context_str = Path(context_file).read_text(encoding="utf-8")
    context = json.loads(context_str)
    return context
