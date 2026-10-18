---
tags: ai_generated
---
# elo-system
python implementation of the elo system

## Structure
Deux versions du même outil : classer une collection par duels successifs, avec un score qui évolue dans le temps.
- `python/` : première version, en Python avec une interface customtkinter. Compilée en exe « Elo Sorter » par `compiler.py` (PyInstaller, sortie dans `python/releases/`). À lancer depuis `python/`, car les chemins de `config.py` sont relatifs.
- `godot/` : deuxième version, en Godot 4.6, avec un calcul Glicko plus poussé. Voir [`godot/README.md`](godot/README.md).

Projet cousin : [`manual-sorting`](../manual-sorting), pour un tri définitif à l'instant T.

# Links

documentation for customtkinter :
https://customtkinter.tomschimansky.com/documentation/utility-classes
