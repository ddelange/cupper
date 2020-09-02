=======
History
=======

1.0.0 (2019-03-22)
------------------

* First release on PyPI.

1.1.0 (2019-03-24)
------------------

* Ask for some options interactively if within interactive shell.

1.2.0 (2020-08-02)
------------------

* Move interactive mode behind -i flag.
* Add -p flag to push the branch on successful update.
* Add -e flag to exclude git pathspecs from the update.
* Do not run pre-commit hooks on the update commit.
* Expose -h flag in addition to --help.
* Finish with non-zero exit status if there are no changes to be made (for shell piping).
