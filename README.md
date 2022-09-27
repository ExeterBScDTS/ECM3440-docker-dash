# ECM3440-docker-dash
Python dash dashboard with Docker

## Overview

This repository contains a teaching example of the use of Docker for cloud deployment of a simple dashboard.
It might possible to use the code here as a starting point for incremental (agile) development of a useable product.

### Building and testing

#### Local build

```sh
> python3.10 -m venv .venv
```

```sh
(.venv) > cd code
(.venv) > pip install --upgrade pip
(.venv) > pip install -r requirements.txt
```

#### Github Actions

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

### Deployment

To deploy containers best practice is to 'push' the containers to a 'registry' from the build (or development) system, then 'pull' to the hosting system - such as a Kubernetes cluster. Do consider appropriate tags for your releases.

<https://docs.docker.com/engine/reference/commandline/push/>


## Resources

<https://www.docker.com/products/docker-hub/>

### VS Code extensions

Python

Docker

## Tutorials

<https://azure.github.io/kube-labs/1-github-actions.html>

<https://nicwortel.nl/blog/2022/05/27/continuous-deployment-to-kubernetes-with-github-actions>

<https://docs.github.com/en/actions/publishing-packages/publishing-docker-images>