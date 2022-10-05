# Deploying container

## Kubernetes

### Local install

Not required, but can be useful when getting started.

<https://microk8s.io/docs/getting-started>

Even if you choose not to install on your laptop, it's worth reading the tutorials to get a better idea of how to use kubernetes.

### Secrets

<https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/>

It's tempting when developing locally to hard code passwords, port numbers, paths, etc. Don't do this!

```sh
$ kubectl create secret generic mysecret \
  --from-literal=username=fred \
  --from-literal=password='Pa55w0rd'

# Check that secret has been created
$ kubectl get secrets

# Print out the secret, base64 encoded 
$ kubectl get secret mysecret -o jsonpath='{.data}' 
```

For more info see

<https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables>


### Deploy

```sh
$ kubectl apply -f kube-dash.yml
```

Note imagePullPolicy can be IfNotPresent, Always, Never <https://kubernetes.io/docs/concepts/containers/images/>

Check deployment status with

```sh
$ kubectl get pods

$ kubectl get services
```

If there is an error, check log with

```sh
$ kubectl logs ecm3440-dash-<ID>

$ kubectl describe pod  ecm3440-dash-<ID>
```

Discover endpoints with

```sh
$ kubectl describe services ecm3440-dash-service
```

Other useful commands

```sh

$ kubectl scale --replicas=0 deployment ecm3440-dash

$ kubectl delete service ecm3440-dash-service

```
