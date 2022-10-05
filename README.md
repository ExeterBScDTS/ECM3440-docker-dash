# ECM3440-docker-dash

Python dash dashboard with Docker

## Overview

This repository contains a teaching example of the use of Docker for cloud deployment of a simple dashboard.

## Building and testing

### Local build

```sh
> python3.10 -m venv .venv
```

```sh
(.venv) > cd code
(.venv) > pip install --upgrade pip
(.venv) > pip install -r requirements.txt
```

### Github Actions

The basic ```docker-image.yml``` workflow looks like this.

```yml
name: Docker Image CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:

  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag my-image-name:$(date +%s)
```

For a full CI/CD pipeline the resulting image will need to be saved, typically by 'pushing' to a 'registry'.

## Deployment

To deploy containers best practice is to 'push' the containers to a 'registry' from the build (or development) system, then 'pull' to the hosting system - such as a Kubernetes cluster. Do consider appropriate tags for your releases.

<https://docs.docker.com/engine/reference/commandline/push/>

Here's where this example is pushed to

<https://hub.docker.com/repository/docker/msaunby/ecm3440-dash>

The current workflow is set up to only push when a version of the code is tagged using git.

e.g.

```
git tag rel-0.1 main

git push origin rel-0.1
```

## Resources

<https://www.docker.com/products/docker-hub/>


## Tutorials

<https://dash.plotly.com/introduction>

<https://docs.docker.com/ci-cd/github-actions/>

<https://azure.github.io/kube-labs/1-github-actions.html>
