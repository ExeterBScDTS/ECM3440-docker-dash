#!/bin/sh

# If you are using a local install of Kubernetes you might need
# alias kubectl='microk8s kubectl'
# See https://microk8s.io/

SERVICE_BUS_CONNECTION=<CONNECTION STRING>
SERVICE_BUS_TOPIC="soil"
SERVICE_BUS_SUBSCRIPTION="S1"

kubectl create secret generic ecm3440 \
  --from-literal=SERVICE_BUS_CONNECTION=${SERVICE_BUS_CONNECTION} \
  --from-literal=SERVICE_BUS_TOPIC=${SERVICE_BUS_TOPIC} \
 --from-literal=SERVICE_BUS_SUBSCRIPTION=${SERVICE_BUS_SUBSCRIPTION}

