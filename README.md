## TL;DR 

Ce script permet d'afficher une icone dans la system tray qui contient un menu permettant de sélectionner des caractères accentués à copier dans le presse papier du système. 
use-case: clavier qwerty avec lequel on doit saiser des caractères accentués. 

Caractères supportés : 
* é
* è
* ê 
* ë
* à
* î
* ï

## Utilisation : 

La première utilisation, exécuter le script install.sh pour l'installation automatique des dépendances. 
```bash
bash install.sh
```

Ensuite, lancer le script via run.sh
```bash
bash run.sh
```

##  Requirements 

Le script est basé sur python3, GTK 3 pour l'interface graphique et AppIndicator3 pour la gestion de l'icône dans la system-tray. 

### OS : 

```bash
sudo apt install python3-gi gir1.2-gtk-3.0 gir1.2-appindicator3-0.1 libappindicator3-1
```

### Sous wayland : 

Le script utilise la librairie wl-clipboard (via subprocess) pour intéragir avec le presse-papier du système. Il est donc nécessaire d'installer wl-clipboard : 
```bash
# gestionnaire de paquet apt
sudo apt install wl-clipboard
```

### Sous x11

Le script utilise la librairie xclip (via subprocess) pour intéragir avec le presse-papier du système. Il est donc nécessaire d'installer xclip : 

```bash
# gestionnaire de paquet apt
sudo apt install xclip
```

