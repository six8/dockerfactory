Dockerfactory
=============

Control the context of your docker builds.

Dockerfactory makes ``docker build`` easier by using a config file
(``Dockerfactory.yml``) instead of command line arguments to build.
``Dockerfactory.yml`` also lets you specify the build context so you can pick and
choose the exact directories or files that get added to your Docker build
context.


Dockerfactory.yml
-----------------

.. code-block:: yaml

    # Automatically tag built images
    tag: six8/dockerfactory
    # Can override the Dockerfile
    dockerfile: ./Dockerfile.prod
    # Most `docker build` parameters work (use '_' instead of '-')
    force_rm: True
    memory: 100m
    context:
      # Relative directories are relative to Dockerfactory.yml
      # Must specify current directory if you want it. Dockerfactory
      # does not assume you want the current directory.
      .: /
      # Dockerfactory allows paths outside of current directory
      ../foobar:/foobar

See `docker build <https://docs.docker.com/engine/reference/commandline/build/>`_
for full set of parameters.


Usage
-----

You can either install as a Python package with ``pip install dockerfactory`` or
run as a docker image.

.. code-block:: shell

    docker run -it --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v ${PWD}:/project \
        six8/dockerfactory:0.1 \
        /project/Dockerfactory.yml

.. code-block:: shell

    Dockerfactory building:
      With command: docker build --force-rm --memory 100m --no-cache --tag six8/dockerfactory:0.1 -
      With Dockerfile: /project/Dockerfile
      With context:
        - /project: /

    Sending build context to Docker daemon 97.28 kB
    ....
