#!/bin/bash
# Turtles all the way down
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

exec docker run \
    --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ${DIR}:/project \
    six8/dockerfactory:0.1 \
    /project/Dockerfactory.yml