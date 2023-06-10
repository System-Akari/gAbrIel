#!/bin/bash

# Actualizar e instalar paquetes en Ubuntu
sudo apt-get update && sudo apt-get install -y \
    python3.10 \
    python3-pip \
    virtualenv \
    git

rm -rf gAbriel    

virtualenv gAbriel 

cd gAbriel 

git init 

git remote add origin https://github.com/System-Akari/gAbrIel.git



echo "Script ejecutado con exito"