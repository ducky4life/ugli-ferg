#!/bin/bash

git pull
docker stop ugli-ferg
docker build -t ugli-ferg:latest -f Dockerfile .
docker run --rm --name ugli-ferg ugli-ferg:latest
