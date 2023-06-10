#!/bin/bash

# Actualizar e instalar paquetes en Ubuntu
sudo apt-get update && sudo apt-get install -y \
    python3.10 \
    python3-pip \
    virtualenv \
    git

# Por si ya existe una carpeta llamada gAbrIel
sudo virtualenv gAbriel 

sudo cd gAbriel 

sudo source bin/activate

sudo git init 

sudo git remote add origin https://github.com/System-Akari/gAbrIel.git

sudo git config pull.rebase true

sudo git pull origin master

sudo git pull

sudo echo "Script ejecutado con exito"