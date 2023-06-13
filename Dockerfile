FROM ubuntu:latest

RUN apg-get update && apt-get install -y \
    python3.10 \ 
    python3-pip \
    git 

