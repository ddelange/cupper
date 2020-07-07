=============================
Cookiecutter Project Upgrader
=============================


.. image:: https://img.shields.io/pypi/v/cookiecutter_project_upgrader.svg
  :target: https://pypi.python.org/pypi/cookiecutter_project_upgrader

.. image:: https://travis-ci.org/thomasjahoda/cookiecutter_project_upgrader.svg?branch=master
  :target: https://travis-ci.org/thomasjahoda/cookiecutter_project_upgrader
  :alt: CI Status

.. image:: https://readthedocs.org/projects/cookiecutter-project-upgrader/badge/?version=latest
  :target: https://cookiecutter-project-upgrader.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: https://codecov.io/gh/thomasjahoda/cookiecutter_project_upgrader/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/thomasjahoda/cookiecutter_project_upgrader
  :alt: Code Coverage




Upgrade projects created from a Cookiecutter template.


* Free software: MIT license
* Documentation: https://cookiecutter-project-upgrader.readthedocs.io.

Features
--------

Cookiecutter Project Upgrader allows upgrading projects that were created using Cookiecutter.

After a project has been created from a Cookiecutter template, changes made to the Cookiecutter template usually have to be applied manually to the project.
This tool automates this process.

When run the first time on a project, it creates a new branch from the first commit of the current branch (the oldest one). It then generates the project again using the latest version of the template and creates a new commit that contains the latest cookiecuttered code,


Usage: cookiecutter_project_upgrader [OPTIONS]

  Upgrade projects created from a Cookiecutter template

Options:
  -c, --context-file PATH         Default: docs/cookiecutter_input.json
  -b, --branch TEXT               Default: cookiecutter-template
  -i, --interactive               Enter interactive mode. Default behaviour:
                                  skip questions, use defaults.

  -m, --merge-now BOOLEAN         Execute a git merge after a successful
                                  update, default: ask if interactive,
                                  otherwise false.

  -p, --push-template-branch-changes BOOLEAN
                                  Push changes to the remote Git branch on a
                                  successful update, default: ask if
                                  interactive, otherwise false.

  -e, --exclude TEXT              Git pathspecs to exclude from the update
                                  commit, e.g. -e "*.py" -e "tests/".

  -h, --help                      Show this message and exit.



Preconditions
-------------

The tool requires a JSON file with context that matches the existing service.
This file can be created through Cookiecutter with the following contents:
::

    {{ cookiecutter | jsonify }}


You will need a recent version of git for this to work. (it needs --no-checkout on git worktree)


Auto-Completion
---------------
The script uses the `Click toolkit <https://github.com/pallets/click>`_.
Because the script uses Click, you can enable completion for Zsh and Bash.

For Bash, add the following to your `.bashrc` or some other profile initialization file.
`eval "$(_COOKIECUTTER_PROJECT_UPGRADER_COMPLETE=source cookiecutter_project_upgrader)"`

For Zsh, please read the `Click documentation <https://click.palletsprojects.com/en/7.x/bashcomplete/#activation>`_.


Credits
-------

The concept and some code is heavily based on https://github.com/senseyeio/cupper, with some changes
to use Click and some flags and default values to ease usage. Also cleanup has been done and automated tests have been added.

This package was created with Cookiecutter_ and the `thomasjahoda/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/thomasjahoda/cookiecutter
.. _`thomasjahoda/cookiecutter-pypackage`: https://github.com/thomasjahoda/cookiecutter-pypackage
