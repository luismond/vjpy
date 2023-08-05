#!/bin/bash
sudo apt install pyqt5-dev-tools -y
sudo apt install imagemagick

#update libs
xmodmap -e "keycode 20 = underscore minus"
xmodmap -e "keycode 47 = colon semicolon"
xmodmap -e "keycode 48 = quotedbl apostrophe quotedbl apostrophe"
