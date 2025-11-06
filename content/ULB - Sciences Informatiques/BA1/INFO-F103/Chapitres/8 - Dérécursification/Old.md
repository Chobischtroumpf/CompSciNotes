---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

On parle de récursivité dans une fonction si, potentiellement, par appels imbriqués, plusieurs exemplaires de cette fonction peuvent simultanément être en cours de réalisation.
- Toute fonction récursive doit posséder un test d’arrêt permettant d’éviter de parcourir indéfiniment le cycle récursif.

- Si une fonction récursive utilise un grand nombre de paramètres, le code généré par le compilateur peut être moins efficace que sa version dérécursifiée.

La dérécursification est donc le processus qui, à partir d’un algorithme contenant des appels récursif, produit un algorithme équivalent où les appels récursifs sont supprimés.
- La sauvegarde et la restauration sont réalisés grâce à une pile;
- On empile pour sauvegarder et on dépile pour restaurer;
- La pile est une structure de données adéquate dans ce contexte, car on ignore le nombre, et donc la profondeur, des sauvegardes.
