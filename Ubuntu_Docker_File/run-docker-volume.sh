#!/bin/bash

docker volume create ubuntu-img-volume-1
docker run -it -v /Home-Dir:/usr/docker-container/ ubuntu-img-1