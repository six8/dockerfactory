#!/bin/bash
# Turtles all the way down
exec docker run -it \
    --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ${PWD}:/project \
    six8/dockerfactory:0.1 \
    /project/Dockerfactory.yml