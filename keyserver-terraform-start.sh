#!/bin/bash
sudo apt-get update
sudo apt-get install -y docker.io
gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin us-east1-docker.pkg.dev
docker run -dit -p 1234:1234 --name fennel-keyserver us-east1-docker.pkg.dev/whiteflag-0/fennel-docker-registry/fennel-keyserver:latest
docker exec -it fennel-keyserver sh
./opt/app/build-dev.sh