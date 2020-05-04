# Boxa entre cavallers

La “boxa entre cavallers” es lleugerament més educada que la tradicional. En aquest tipus de boxa els contendents es claven cops però ho fan de forma ordenada

![Combat](combat.png)

El combat consisteix en anar repetint el mateix procés:

- Primer pica un mentre l’altre es protegeix
- Després pica el segon mentre el primer es protegeix

El combat acaba quan un dels dos cau perquè ha rebut molts cops en llocs desprotegits

## Cops i protecció

Cada boxejador pot picar en quatre llocs diferents del seu contrincant.

![Cops](https://raw.githubusercontent.com/XavierSala/Boxa/master/atacs-boxa.png "On pot rebre?")

Les proteccions que pot fer un boxejador són perfectes. Això vol dir que si rep un cop en una protecció no rebrà cap mal.

Desafortunadament el que es protegeix només pot protegir tres llocs. Això vol dir que sempre pot rebre un cop en un lloc desprotegit

## Activitat: El combat

Es demana que desenvolupeu, fent servir orientació a objectes, un programa que permeti simular el funcionament del combat de boxa entre cavallers i el vagi radiant per pantalla.

```text
    Ex.
    $ java -jar Boxa-1.0-SNAPSHOT.jar
    MatxacaCaps(5) cop bloquejat per DestrossaPilotes(5)
    DestrossaPilotes(5) cop bloquejat per MatxacaCaps(5)
    MatxacaCaps(5) cop bloquejat per DestrossaPilotes(5)
    DestrossaPilotes(5) cop bloquejat per MatxacaCaps(5)
    MatxacaCaps(5) cop al cap de DestrossaPilotes(4)
    DestrossaPilotes(4) cop bloquejat per MatxacaCaps(5)
    MatxacaCaps(5) cop bloquejat per DestrossaPilotes(4)
    DestrossaPilotes(4) cop bloquejat per MatxacaCaps(5)
    MatxacaCaps(5) cop al costat dret de DestrossaPilotes(3)
    DestrossaPilotes(3) cop al costat esquerra de MatxacaCaps(4)
    MatxacaCaps(4) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop bloquejat per MatxacaCaps(4)
    MatxacaCaps(4) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop bloquejat per MatxacaCaps(4)
    MatxacaCaps(4) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop a la panxa de MatxacaCaps(3)
    MatxacaCaps(3) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop bloquejat per MatxacaCaps(3)
    MatxacaCaps(3) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop al costat esquerra de MatxacaCaps(2)
    MatxacaCaps(2) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop bloquejat per MatxacaCaps(2)
    MatxacaCaps(2) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop a la panxa de MatxacaCaps(1)
    MatxacaCaps(1) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop bloquejat per MatxacaCaps(1)
    MatxacaCaps(1) cop bloquejat per DestrossaPilotes(3)
    DestrossaPilotes(3) cop bloquejat per MatxacaCaps(1)
    MatxacaCaps(1) cop al costat esquerra de DestrossaPilotes(2)
    DestrossaPilotes(2) cop bloquejat per MatxacaCaps(1)
    MatxacaCaps(1) cop al costat esquerra de DestrossaPilotes(1)
    DestrossaPilotes(1) cop bloquejat per MatxacaCaps(1)
    MatxacaCaps(1) cop bloquejat per DestrossaPilotes(1)
    DestrossaPilotes(1) cop bloquejat per MatxacaCaps(1)
    MatxacaCaps(1) cop bloquejat per DestrossaPilotes(1)
    DestrossaPilotes(1) cop bloquejat per MatxacaCaps(1)
    MatxacaCaps(1) cop bloquejat per DestrossaPilotes(1)
    DestrossaPilotes(1) cop al costat dret de MatxacaCaps(0)
    MatxacaCaps(0) està KO!
```

    Ha guanyat en DestrossaPilotes
