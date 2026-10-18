---
tags: ai_generated
---
# glicko-sorter

Projet Godot 4.6 (GDScript) pour classer une collection d'éléments par comparaisons deux à deux, avec un score de type **Glicko** (un Elo avec un indice de doute).

## Principe
- Chaque élément (`Sortable`) a un score, un doute et un historique de duels (`ContestResult`).
- Le doute remonte avec le temps passé sans duel (`GlickoBrain.compute_doubt_since_last_update`), jusqu'à `MAX_DOUBT` au bout de `FORGET_DAYS`.
- Une `Arena` regroupe les éléments, les répartit en `BattlePool` et calcule les résultats de tournoi.

## Structure
- `scripts/config.gd` (autoload `Config`) : paramètres du calcul (écart standard, doutes min/max, oubli).
- `scripts/classes/` : `Arena`, `BattlePool`, `ContestResult`, `Sortable`.
- `scripts/utils/` : `GlickoBrain` (calcul), `FileManager` (sauvegarde `.res`, import TSV, import d'un dossier d'images).
- `scenes/` : `the_root.tscn` (scène principale), `sortable_card` (carte affichée à gauche/droite), `tool.gd` (script de test).

## État
En cours. `tool.gd` charge une collection d'images de test depuis `D:/[02] Code/03 Sandbox/temp/glicko-sorter/Collection` et affiche deux éléments au hasard. Export TSV disponible (`Arena.export_tsv`).

## Liens
Reprise en Godot de [`elo-system`](../elo-system) (Python, exe « Elo Sorter », dans `06 Releases/elo-sorter`).
