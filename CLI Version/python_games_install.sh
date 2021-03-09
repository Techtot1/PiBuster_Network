#!/bin/bash -e

wget "https://github.com/KenT2/python-games/tarball/master" -O python_games.tar.gz

ln -sf pip3 /usr/bin/pip-3.2

install -v -o pi -g pi -d /home/pi/python_games
tar xvf python_games.tar.gz -C /home/pi/python_games --strip-components=1
chown pi:pi /home/pi/python_games -Rv
chmod +x /home/pi/python_games/launcher.sh

install -v -o pi -g pi -d "/home/pi/Documents"
install -v -o pi -g pi -d "/home/pi/Documents/BlueJ Projects"
install -v -o pi -g pi -d "/home/pi/Documents/Greenfoot Projects"
install -v -o pi -g pi -d "/home/pi/Documents/Scratch Projects"
mkdir -p /usr/share/doc/BlueJ/
mkdir -p /usr/share/doc/Greenfoot/
mkdir -p /usr/share/scratch/Projects/Demos/
rsync -a --chown=pi:pi /usr/share/doc/BlueJ/ "/home/pi/Documents/BlueJ Projects"
rsync -a --chown=pi:pi /usr/share/doc/Greenfoot/ "/home/pi/Documents/Greenfoot Projects"
rsync -a --chown=pi:pi /usr/share/scratch/Projects/Demos/ "/home/pi/Documents/Scratch Projects"

#Alacarte fixes
install -v -o pi -g pi -d "/home/pi/.local"
install -v -o pi -g pi -d "/home/pi/.local/share"
install -v -o pi -g pi -d "/home/pi/.local/share/applications"
install -v -o pi -g pi -d "/home/pi/.local/share/desktop-directories"
