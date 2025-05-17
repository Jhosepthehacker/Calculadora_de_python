#!/bin/bash
# Saludo
echo "Hola Bienvenido O Bienvenida a Calculadora."
# Salto de línea
echo ""
# Título
printf -e "\e[31m #--------------------------------#"
printf -e "\e[33m #          Calculadora           #"
printf -e "\e[34m #--------------------------------#"
# Salto de línea y restablecer colores
echo -e "\e[0m"
# Entrada de datos
read -p "¿Quiéres Ejecutar Calculadora.py Para Calcular :)?: " respuesta
# Comprobando la respuesta del usuario
if [[ "$respuesta" == "si" ]]; then
     echo -e "\e[32m Ejecutando Calculadora.py ^_^"
     sleep 2
     exit 1
     apt install python3
     python3 Calculadora.py
else
        echo -e "\e[34m Saliendo, Operación Terminada."
fi
