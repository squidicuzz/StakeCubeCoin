
Debian
====================
This directory contains files used to package sccd/scc-qt
for Debian-based Linux systems. If you compile sccd/scc-qt yourself, there are some useful files here.

## scc: URI support ##


scc-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install scc-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your scc-qt binary to `/usr/bin`
and the `../../share/pixmaps/scc128.png` to `/usr/share/pixmaps`

scc-qt.protocol (KDE)

