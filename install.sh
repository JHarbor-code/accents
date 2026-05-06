#!/bin/bash
echo "Installation..."
echo "python3-gi..."
command -v python3-gi >/dev/null || sudo apt install -y python3-gi 
echo "gir1.2-gtk-3.0..."
command -v gir1.2-gtk-3.0 >/dev/null || sudo apt install -y gir1.2-gtk-3.0
echo "gir1.2-appindicator3-0.1..."
command -v gir1.2-appindicator3-0.1 >/dev/null || sudo apt install -y gir1.2-appindicator3-0.1
echo "libappindicator3-1..."
command -v libappindicator3-1 >/dev/null || sudo apt install -y libappindicator3-1
            

echo "presse papier..."
if [[ "$XDG_SESSION_TYPE" == "x11" ]]; then
    command -v xclip >/dev/null || sudo apt install -y xclip

elif [[ "$XDG_SESSION_TYPE" == "wayland" ]]; then
    command -v wl-copy >/dev/null || sudo apt install -y wl-clipboard

else
    echo "Erreur : environnement graphique inconnu ($XDG_SESSION_TYPE)"
    echo "Ce script nécessite X11 ou Wayland."
    exit 1
fi

echo "Installé avec succès ! Pour lancer le programme, exécuter run.sh"
