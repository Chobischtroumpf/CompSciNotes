---
title: Packet loss
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> Une **queue** (aussi appelée buffer) précédant un lien dans un buffer a une capacité finie.
>
> Un paquet arrivant dans une queue pleine est **dropped** (perdu).
>
> Un paquet perdu peut être retransmis par le nœud précédent, par le système source, ou pas du tout.

> [!tip]+ Remarque
> La perte de paquets se produit lorsque la zone d'attente (buffer) est saturée. Les paquets en cours de transmission ne sont pas affectés, mais tout nouveau paquet arrivant alors que le buffer est plein sera perdu.
