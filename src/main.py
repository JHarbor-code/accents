import os
from pathlib import Path
import subprocess

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, AppIndicator3



base_path = Path(__file__).resolve().parent.parent

image_path = base_path / "assets" / "reindeer.png"


def copy(text: str):
    session = os.environ.get("XDG_SESSION_TYPE", "").lower()

    if session == "x11":
        subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.encode("utf-8"),
            check=True,
        )
    elif session == "wayland":
        subprocess.run(
            ["wl-copy"],
            input=text.encode("utf-8"),
            check=True,
        )
    else:
        raise RuntimeError(f"Session graphique inconnue: {session!r}")


def e_aigu(_):
    copy("é")


def e_grave(_):
    copy("è")


def e_circ(_):
    copy("ê")


def e_trema(_):
    copy("ë")


def a_accent(_):
    copy("à")


def i_circ(_):
    copy("î")


def i_trema(_):
    copy("ï")


def on_quit(_):
    Gtk.main_quit()


def build_menu():
    menu = Gtk.Menu()

    items = [
        ("é", e_aigu),
        ("è", e_grave),
        ("ê", e_circ),
        ("ë", e_trema),
        ("à", a_accent),
        ("î", i_circ),
        ("ï", i_trema),
    ]

    for label, callback in items:
        item = Gtk.MenuItem(label=label)
        item.connect("activate", callback)
        item.show()
        menu.append(item)

    separator = Gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)

    quit_item = Gtk.MenuItem(label="Exit")
    quit_item.connect("activate", on_quit)
    quit_item.show()
    menu.append(quit_item)

    return menu


indicator = AppIndicator3.Indicator.new(
    "accents",
    "applications-system",
    AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
)

indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
indicator.set_menu(build_menu())

if os.path.isfile(image_path):
    indicator.set_icon_full(str(image_path), "accents")

Gtk.main()