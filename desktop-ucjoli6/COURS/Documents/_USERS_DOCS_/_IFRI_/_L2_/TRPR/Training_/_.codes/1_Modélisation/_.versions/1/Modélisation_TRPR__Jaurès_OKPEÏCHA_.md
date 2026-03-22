

# Modélisation et Formulation de problèmes de recherche
---
<!-- Chargement de KaTeX et Mermaid -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body);"></script>

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
</script>
<!-- $$ -->


## Exercice 1: *Problème des Missionnaires et Cannibales*

>a. Modélisation du problème

Soit les lettres M et C représentants respectivement missionnaires et cannibales
Soit G et D (gauches et droites)

- *Espace des états*:   
    - 3 missionnaires sur la rive G et 3 cannibales sur la rive D, et inversement;  <!-- $ 2 states $ -->
    - tous les missionnaires et cannibales sur l'une des rives (G ou D);    <!-- $ 2 states $ -->
    - 3 missionnaires sur la rive G et 1 ou 2 cannibale(s) sur la rive D, et inversement;   <!-- $ 2 states $ -->
    - Une barque vide positionnée au niveau des premiers passagers

- *Actions possibles*: - Embarquer au plus deux personnes dont: 2 M; 2 C; 1 M et 1 C; 1 M; 1 C;

- *Objectif(s)*: - Faire passer tous (cannibales et missionnaires) à l'autre rive

- *Coûts des actions* (**aléatoires**):
  - Toute action minimisant les traversées vaudrait 1, autrement 0;
  - Le non respect de la condition ($nbrMissionnaires \ge nbrCannibales$) annule tout les coûts ($c = 0$);

- *Description des transitions d'états*:    

    - Le nombre de missionnaires ou de cannibales varie entre 0 et 3 sur les deux rives
    - Un retour de la barque, sur une rive, implique toujours d'avoir un conducteur <!-- nautonier -->
    - En cas de mixture sur l'une des rives, un nombre supérieur de cannibale ($nCa > nMiss$) implique l'arrêt du système du à une mauvaise combinaison

- *Critère d'optimalité*:   
    - Faire traverser deux cannibales en premier


>b. Représentation sous forme de graphe

*Informations sur le graphe*:   Soit 
- [(*rive gauche*); (*rive droite*)]    ->  [(..., $G$); (..., $D$)];
- $M_g$ et $M_d$ respectivement missionnaire(s) étant (avant l'action) à gauche et à droite;
- $C_g$ et $C_d$ respectivement cannibale(s) étant (avant l'action) à gauche et à droite;
- $\vec{G}$ et $\vec{D}$ respectivement aller en direction de la gauche et droite;
    - ex.: relations    ($2M_d$, $\vec{G}$) et  ($1M_g$, $1C_g$, $\vec{D}$)

<!--
```mermaid
graph TD;
```
-->
<!-- A[["[(0,G); (3M,3C,D)]"]] --|>|"<span>(1C,G)</span>"| A; B & C -.-> X[X];-->
```mermaid
graph TD;
    Init[["[(0,G); (3M,3C,D)]"]];
    Goal["[(3M,3C,G); (0,D)]"];
    fi["✅"]; X["❌"];
    Goal -.-> fi;

    Init -.->|"<span>(2M,G)</span>"| B["[(2M,G); (1M,3C,D)]"] -.-> X;
    Init -.->|"<span>(1M,G)</span>"| C["[(1M,G); (2M,3C,D)]"] -.-> X;

    Init -->|"<span>(1C,G)</span>"| µF["[(1C,G); (3M,2C,D)]"] -->|"<span>(1C,D)</span>"| Init;
    Init -->|"<span>(2C,G)</span>"| D["[(2C,G); (3M,1C,D)]"] -->|"<span>(2C,D)</span>"| Init;

    D -->|"<span>(1C,D)</span>"| F["[(1C,G); (3M,2C,D)]"] -->|"<span>(1C,G)</span>"| D;

    Init -->|"<span>(1C,1M,G)</span>"| E["[(1M,1C,G); (2M,2C,D)]"] -->|"<span>(1C,1M,D)</span>"| Init;

    E -->|"<span>(1C,D)</span>"| C;

    E -->|"<span>(1M,D)</span>"| F -->|"<span>(1M,G)</span>"| E;

    F -->|"<span>(1C,1M,G)</span>"| G["[(1M,2C,G); (2M,1C,D)]"] -.-> X;
    F -->|"<span>(2M,G)</span>"| H["[(2M,1C,G); (1M,2C,D)]"] -.-> X;

    F -->|"<span>(2C,G)</span>"| I["[(3C,G); (3M,D)]"] -->|"<span>(2C,D)</span>"| F;
    
    I -->|"<span>(1C,D)</span>"| dD;
    
    dD["[(2C,G); (3M,1C,D)]"] -->|"<span>(1C,G)</span>"| I;
    dD -->|"<span>(1M,G)</span>"| G;
    dD -->|"<span>(1C,1M,G)</span>"| J["[(1M,3C,G); (2M,D)]"] -.-> X;

    dD -->|"<span>(2M,G)</span>"| K["[(2M,2C,G); (1M,1C,D)]"] -->|"<span>(2M,D)</span>"| dD;

    K -->|"<span>(2C,D)</span>"| B;
    K -->|"<span>(1C,D)</span>"| H;
    K -->|"<span>(1M,D)</span>"| G;

    K -->|"<span>(1C,1M,D)</span>"| eE["[(1M,1C,G); (2M,2C,D)]"] -->|"<span>(1C,1M,G)</span>"| K;

    eE -->|"<span>(2C,G)</span>"| J;
    eE -->|"<span>(1C,G)</span>"| G;
    eE -->|"<span>(1M,G)</span>"| H;

    eE -->|"<span>(2M,G)</span>"| L["[(3M,1C,G); (2C,D)]"] -->|"<span>(2M,D)</span>"| eE;

    L -->|"<span>(1M,D)</span>"| H;
    L -->|"<span>(1C,1M,D)</span>"| B;

    L -->|"<span>(1C,D)</span>"| Y["[(3M,G); (3C,D)]"] -->|"<span>(1C,G)</span>"| L;

    Y -->|"<span>(2C,G)</span>"| M["[(3M,2C,G); (1C,D)]"] -->|"<span>(2C,D)</span>"| Y;
    
    M -->|"<span>(2M,D)</span>"| G;
    M -->|"<span>(1C,1M,D)</span>"| H;

    M -->|"<span>(1M,D)</span>"| kK["[(2M,2C,G); (1M,1C,D)]"] -->|"<span>(1M,G)</span>"| M;
    M -->|"<span>(1C,D)</span>"| lL["[(3M,1C,G); (2C,D)]"] -->|"<span>(1C,G)</span>"| M;

    kK -->|"<span>(1C,1M,G)</span>"| Goal;
    kK -->|"<span>(1C,G)</span>"| N["[(2M,3C,G); (1M,D)]"] -.-> X;
    
    lL -->|"<span>(2C,G)</span>"| Goal;

```


---

## Exercice 2: *Un jeu de séduction*

>1.1. Formulation du problème de recherche:

- *Etats Initiaux*: 
    - *e1*: **[M, M, M, [V], F, F, F]**
    - *e2*: 

- *Actions possibles*:  
    - ***act1***: Une personne (homme ou femme) peut aller sur une chaise vide adjacente.

    - ***act2***: Une personne peut sauter une ou deux personnes pour aller sur une chaise vide.

- *Objectifs de test*:  
    - Mettre des femmes et hommes côte à côte : **[..., M, F, ...]**
    - Obtenir la configuration **[[V], M, F, M, F, M, F]**

- *Coûts des actions*:  
    - *act1*: coût = **1**

    - *act2*: 
        - **1** ->  1 déplacement;
        - **2** ->  2 déplacements;

>1.2. Deux autres configurations pour l'état final:

- Configuration 1:  **[M, F, M, F, M, F, [V]]**

- Configuration 2:  **[M, F, F, M, M, F, [V]]**


---

##

<!--
{ [(M, M, M, C, C, C, G); ()] | } { __(2C_<>)__>{ { [(M, M, M, C, G); (C, C, D)] | } { || { [(); ()] | } {  __()__>  { [(); ()] | }

---
m f m m v f f

- m f m f m f v

- m f f m m f v
---
- direction de la barque
- nbr de missionnaires ou cannibales sur A et/ou B
-->
---
<!--
# UML example

```plantuml
@startuml
Bob -> Alice : hello
@enduml
```
-->
<!--
Here is a simple flow chart:

```mermaid
graph TD;
    A--|>B;
    A--|>C;
    B--|>D;
    C--|>D;
```
-->
<!--
```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```
-->
