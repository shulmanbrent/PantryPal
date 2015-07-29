#!/bin/bash

# image name
__image=shulmanbrent/heroku_django

# build image
docker build -t $__image .
