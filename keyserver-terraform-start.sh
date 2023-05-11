#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io
gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin us-east1-docker.pkg.dev
docker run -dit -p 1235:1235 --name fennel-keyserver us-east1-docker.pkg.dev/whiteflag-0/fennel-docker-registry/keyserver:latest
docker exec -it fennel-keyserver /opt/app/build-dev.sh
