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

## Infos

Le script réinitialise les variables d'environnement `GTK_PATH`, `GIO_MODULE_DIR` et `LD_LIBRARY_PATH` pour éviter les conflits gtk. 

##  Requirements 

Le script est basé sur python3.

### OS : 

Le script utilise la librairie python pystray pour affichier une icone dans la system-tray.
Le backend gtk est utilisé, ce qui implique d'installer les dépendances gtk (sinon erreur `No module named 'gi'`) 

```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

### PIP 

* pillow : 10.2.0
* pystray : 0.19.5

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

