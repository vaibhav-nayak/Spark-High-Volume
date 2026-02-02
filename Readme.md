### Prerequities
- uv
- docker
- colima
- kubectl

### Setup
#### Setup kubernetes (provide edit role for default namespace)
```shell
just setup
```
#### Download Data and upload to minio
```shell
just download-upload
```
#### Run Spark in kubernetes
```shell
just build
just depoy
```