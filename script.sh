#!/bin/bash

# Actualizar e instalar paquetes en Ubuntu
sudo apt-get update && sudo apt-get install -y \
    python3.10 \
    python3-pip \
    virtualenv \
    git

# Por si ya existe una carpeta llamada gAbrIel
rm -rf gAbriel    

sudo virtualenv gAbriel 

cd gAbriel 

source bin/activate

git init 

git remote add origin https://github.com/System-Akari/gAbrIel.git

git config pull.rebase true

git pull origin master

git pull

echo "Script ejecutado con exito"