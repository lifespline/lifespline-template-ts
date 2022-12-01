"""
`invoke <https://www.pyinvoke.org/>`_ is the project's task runner. The tasks are defined at ``tasks.py``.
"""
from invoke import task
import os
import sys
from pathlib import Path

@task
def docs(ctx, step='build', verbose=False):
    """Documentation ops.

    Build ``-s | -s build``
    -----------------------

    Builds the docs and checks for WARNINGS or ERRORS. If none occurs, the docs are published to the repo.

    Start ``-s start``
    ------------------

    Start the sphinx local python server.

    Stop ``-s stop``
    ----------------

    Stop the sphinx local python server.
    TODO: the server stops but the task runner raises an error.

    :param step: _description_, defaults to 'build'
    :type step: str, optional
    :param verbose: _description_, defaults to False
    :type verbose: bool, optional
    """
    if step == 'build':
        cmds = [
            "cd docs/sphinx",
            "make html",
        ]

        if verbose:
            res = ctx.run(';'.join(cmds))
        else:
            res = ctx.run(';'.join(cmds), hide='both')

        if 'WARNING' in res.stdout:
            sys.exit("There seems to be a WARNING in the build process. Please fix it before publishing the docs. Add the flag '--verbose' to see the stdout.")
        elif res.stderr:
            sys.exit("There seems to be an ERROR in the build process. Add the flag '--verbose' to see the stderr.")

        print('build: OK')

    if step == 'start':
        docs(ctx,  step='build')
        cmds = [
            "cd docs/sphinx/_build/html",
            "python -m http.server"
        ]

        print('localhost start: OK')
        print('Hosting sphinx server at localhost:8000')
        print("'inv docs -s stop' to shutdown")
        if verbose:
            res = ctx.run(';'.join(cmds))
        else:
            res = ctx.run(';'.join(cmds), hide='both')

    if step == 'stop':
        cmds = [
            'sudo kill -9 $( pgrep -f "python -m http.server" )'
        ]

        if verbose:
            res = ctx.run(';'.join(cmds))
        else:
            res = ctx.run(';'.join(cmds), hide='both')
        print('localhost stop: OK')

    if step == 'publish':
        docs(ctx,  step='build')
        cmds = [
            "cp -a docs/sphinx/_build/html/. docs/sphinx",
            "cd docs/sphinx"
            "make clean",
            "cd ../..",
            "git add docs",
            "git commit -m \"doc: publish\"",
            "git push"
        ]

        if verbose:
            res = ctx.run(';'.join(cmds))
        else:
            res = ctx.run(';'.join(cmds), hide='both')

        print('remote publish: OK')

    if step == 'clean':
        cmds = [
            "cd docs/sphinx",
            "make clean",
            "cd ..",
            "rm -rf _downloads",
            "rm -rf _images",
            "rm -rf src",
            "rm -rf .buildinfo",
            "rm -rf _sources",
            "rm -rf _static",
            "rm -rf genindex.html",
            "rm -rf index.html",
            "rm -rf objects.inv",
            "rm -rf search.html",
            "rm -rf searchindex.js",
            "rm -rf py-modindex.html",
        ]

        print('local clean: OK')
