---
title: Questions théoriques
authors: Alessandro Dorigo
tags:
  - Proba
  - Stats
---

# Statistiques
## 1. Définir la notion
#### 1.1 D’estimateur
Un estimateur d'un paramètre $\theta$ est une statistique dont les valeurs se situent dans l'espace des paramètres $\Theta$.
#### 1.2 D’estimateur sans biais
Un estimateur est dit sans biais si son espérance est égale au paramètre recherché. Plus formellement:
$$\mathbb{E}[\hat{\theta}] = \theta \quad \forall \theta \in \Theta$$
#### 1.3 Montrer que la moyenne arithmétique empirique est sans biais pour l’espérance
La moyenne arithmétique empirique est définie comme:
$$\bar{X} := \frac{1}{n} \sum_{i=1}^n X_i$$
Avec $X_1, \dots, X_n$ i.i.d. et $\mathbb{E}[X_i] = \mu$.

Pour montrer qu'elle est sans biais pour l’espérance:
$$\mathbb{E}[\bar{X}] = \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E}[X_i] = \mu$$
## 2. Définir la variance empirique d’un échantillon $X_1,\dots, X_n$ et étudier son biais
La variance empirique est définie comme:
$$s^2 := \frac{1}{n} \sum_{i=1}^n (X_i - \bar{X})^2$$

Avec $X_1, \dots, X_n$ i.i.d. , $\text{Var}(X_i) = \sigma^2$ et $\mathbb{E}[X_i] = \mu$.

Étudions son biais:
$$\begin{aligned}
\mathbb{E}[s^2]
&= \mathbb{E} \left[\frac{1}{n} \sum_{i=1}^n X_i^2 \right] - \mathbb{E}[\bar{X}^2] \\
&= \mathbb{E}[X_i^2] - (\text{Var}(\bar{X}) + \mathbb{E}[\bar{X}]^2) \\
&= \text{Var}(X_1) + \mathbb{E}[X_1]^2 - (\text{Var}(\bar{X} + \mathbb{E}[\bar{X}])^2) \\
&= \sigma^2 + \mu^2 - \frac{\sigma^2}{n} - \mu^2 = \frac{n - 1}{n} \sigma^2 < \sigma^2
\end{aligned}$$

On trouve que la variance empirique est un estimateur biaise de $\sigma^2$. Pour corriger cela, il faut multiplier par l'inverse:
$$S^2 := \frac{n}{n - 1} s^2$$
et donc on a
$$\mathbb{E}[S^2] = \mathbb{E} \left[\frac{n}{n - 1} s^2 \right] = \frac{n}{n - 1} \mathbb{E}[s^2] = \sigma^2$$
## 3. Définir
#### 3.1 L’écart quadratique moyen (EQM) d’un estimateur
L'EQM d'un estimateur représente l'erreur moyenne quadratique entre $\hat{\theta}$ et $\theta$. Plus formellement:
$$\text{EQM}(\hat{\theta}) = \mathbb{E}[(\hat{\theta} - \theta)^2]$$
#### 3.2 Quel est le lien entre l’EQM et la variance de l’estimateur?
L’EQM est la variance augmentée du carré du biais:
$$\begin{aligned}
\text{EQM}(\hat{\theta})
&= \mathbb{E}[(\hat{\theta} - \mathbb{E}[\hat{\theta}] + \mathbb{E}[\hat{\theta}] - \theta)^2] \\
\vdots \\
&= \text{Var}(\hat{\theta}) + (\mathbb{E}[\hat{\theta}] - \theta)^2 \\
&= \text{Var}(\hat{\theta}) + \text{Biais}(\hat{\theta})^2
\end{aligned}$$
#### 3.3 Peut-on trouver un estimateur à EQM minimal?
Oui, un estimateur a EQM minimal peut être trouvé en définissant la notion d'estimateur efficace, qui stipule que si son biais est nul et sa variance atteint uniformément la borne de Cramér-Rao, alors il est efficace.
$$\text{Var}_\theta(\hat{\theta}) = \frac{1}{\mathcal{I}(\theta)}, \quad \forall \theta \in \Theta$$
## 4. Définir
#### 4.1 Les notions de risque de première et seconde espèce d’un test
L'erreur de première espèce consiste à rejeter $H_0$ alors qu'elle est correcte:

Le risque, noté $\alpha$, est défini comme:
$$\mathbb{P}_\theta[RH_0] = \mathbb{P}_\theta[\phi(\mathbf{X}) = 1] = \mathbb{E}_\theta[\phi]$$

L'erreur de seconde espèce consiste à ne pas rejeter $H_0$ alors qu'elle est fausse:

Le risque, noté $\beta$, est défini comme:
$$\mathbb{P}_\theta[NRH_0] = 1 - \mathbb{P}_\theta[\phi(\mathbf{X}) = 1] = 1 - \mathbb{E}_\theta[\phi]$$
#### 4.2 Qu’est-ce que le Principe de Neyman?
Le principe de Neyman consiste à construire un test qui contrôle le risque de première espèce en se limitant aux tests $\phi$ de niveau $\alpha$, c’est-à-dire aux tests satisfaisant la condition $\mathbb{E}_\theta[\phi] \leq \alpha, \quad \forall \theta \in H_0$, tout en minimisant le risque de seconde espèce $\beta$ en choisissant celui qui maximise la puissance uniformément sur $\theta \in H_1$.
## 5. Soient $X_1,\dots, X_n$ i.i.d. de loi normale de moyenne $\mu$ et de variance 4
#### 5.1 Pour tester que $\mu$ est plus petite que 0, quel test utiliseriez-vous?
#### 5.2 Quelle est la forme de sa courbe de puissance? Justifiez.
## 6. Soient $X_1,\dots, X_n$ i.i.d. de loi inconnue de moyenne $\mu$ et de variance $\sigma^2$ ($n$ plus grand que $30$)
#### 6.1 Pour tester que $\mu$ est différent de 0, quel test utiliseriez-vous?

#### 6.2 Quelle est la forme de sa courbe de puissance? Justifiez.
