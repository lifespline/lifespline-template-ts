"""
`invoke <https://www.pyinvoke.org/>`_ is the project's task runner. The tasks are defined at ``tasks.py``.
"""
from invoke import task
import os
import sys
from pathlib import Path

docs_docker_image = 'samples_ts_docs'
docs_docker_image_path = 'docs/sphinx/Dockerfile.debug'
docs_debug_container_name = 'samples_ts_docs'
sphinx_server_default_port = '8000'
docker_host_sphinx_server_default_port = '8001'

@task
def docs(ctx, step='sphinx-build', port=docker_host_sphinx_server_default_port, verbose=False):
    """Documentation ops.

    Build ``--step sphinx-build``
    -----------------------------

    Builds the docs and checks for WARNINGS or ERRORS. If none occurs, the docs are published to the repo.

    Build ``--step docker-build --port PORT``
    -----------------------------------------

    Builds the docker image and runs the container to debug the docs with a contaneirized sphinx server listenning on 0.0.0.0:``port``.

    Debug ``--step debug --port PORT``
    ----------------------------------

    Start a debugging local sphinx python server in a docker container.

    Stop ``--step stop``
    ----------------

    Stop the local debugging container with a sphinx python server.

    :param step: _description_, defaults to 'build'
    :type step: str, optional
    :param verbose: _description_, defaults to False
    :type verbose: bool, optional
    """
    if step == 'sphinx-build':

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

        # rebuild image and container
        cmd = f"""
        docker build \
            -t {docs_docker_image} \
            -f {docs_docker_image_path} \
            docs/sphinx

        docker stop {docs_debug_container_name}
        docker rm {docs_debug_container_name}

        docker run \
            --rm -d \
            --name {docs_debug_container_name} \
            -p 0.0.0.0:{port}:{sphinx_server_default_port} \
            {docs_docker_image}
        """
        if verbose:
            res = ctx.run(cmd)
        else:
            res = ctx.run(cmd, hide='both')

        print('build: OK')

    if step == 'docker-build':
        # build image if it doesn't exist locally already
        cmd = f"""
        if [[ "$(docker images -q {docs_docker_image} 2> /dev/null)" == "" ]]; then
            docker build \
                -t {docs_docker_image} \
                -f {docs_docker_image_path} \
                docs/sphinx
        fi
        """
        ctx.run(cmd)

        # run container it it doesn't exist locally already
        cmd = f"""
        if [[ "docker container inspect -f '{{{{.State.Running}}}}' {docs_debug_container_name}" != "true" ]]; then
            docker run \
                --rm -d \
                --name {docs_debug_container_name} \
                -p 0.0.0.0:{port}:{sphinx_server_default_port} \
                {docs_docker_image}
        fi
        """
        ctx.run(cmd)

    if step == 'stop':
        ctx.run(f'docker stop {docs_debug_container_name}')

    if step == 'publish':
        docs(ctx,  step='sphinx-build', port=port)
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

