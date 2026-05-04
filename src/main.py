import os

os.environ["PYSTRAY_BACKEND"] = "gtk"

os.environ.pop("GTK_PATH", None)
os.environ.pop("GIO_MODULE_DIR", None)
os.environ.pop("LD_LIBRARY_PATH", None)


import pystray
from PIL import Image
import sys

import subprocess



try: 
    base_path = sys._MEIPASS

except Exception:
    base_path = os.path.abspath("")

image_path = os.path.join(base_path, "./assets/reindeer.png")


if os.environ.get("XDG_SESSION_TYPE") == "x11":

  def copy(text: str):

      subprocess.run(

          ["xclip", "-selection", "clipboard"],

          input=text.encode(),

          check=True

      )



elif os.environ.get("XDG_SESSION_TYPE") == "wayland":

  def copy(text):

      subprocess.run(

          ["xclip", "-selection", "clipboard"],

          input=text.encode(),

          check=True

      )

image = Image.open(image_path)

print(pystray.Icon.HAS_MENU)





def on_quit():

    sys.exit()

def e_aigu():

    copy("é")



def e_grave():

    copy("è")



def e_circ():

    copy("ê")

    

def e_trema():

    copy("ë")



def a_accent():

  copy("à")



def i_trema():

    copy("ï")



def i_circ():

    copy("î")





icon = pystray.Icon("accents", image, "accents", 

                    menu=pystray.Menu(

    pystray.MenuItem("é", 

                     e_aigu),

    pystray.MenuItem("è", 

                     e_grave),

    pystray.MenuItem("ê", 

                     e_circ),

    pystray.MenuItem("ë", 

                     e_trema),   

    pystray.MenuItem("à", 

                     a_accent),

    pystray.MenuItem("î", 

                     i_circ),  

    pystray.MenuItem("ï", 

                     i_trema),          

    pystray.MenuItem("Exit", on_quit)))







icon.run()




