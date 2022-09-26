# ECM3440-docker-dash
Python dash dashboard with Docker

## Overview

This repository contains a teaching example of the use of Docker for cloud deployment of a simple dashboard.
It might possible to use the code here as a starting point for incremental (agile) development of a useable product.

### Building and testing

Local build

```sh
> python3.10 -m venv .venv
```

```sh
(.venv) > cd code
(.venv) > pip install --upgrade pip
(.venv) > pip install -r requirements.txt
```

Github Actions

### Deployment

To deploy containers best practice is to 'push' the containers to a 'registry' from the development system (your laptop), then 'pull' to the hosting system - such as a Kubernetes cluster. Do consider appropriate tags for your releases.

<https://docs.docker.com/engine/reference/commandline/push/>


## Resources

<https://www.docker.com/products/docker-hub/>

### VS Code extensions

Python

Docker
