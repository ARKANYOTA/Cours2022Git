---
vim: set ft=tex
title: Dérivées
created: '2021-09-21T06:56:41.054Z'
modified: '2021-09-29T07:54:21.149Z'
---


# Dérivées\_Connexité

Propriete: 2droites ont parralleles lorque que leur coefficient directeur sont egaux(que elle ont la meme pente)

## I) Composé de 2 fonctions

[...]

---

$u(x) = x²+3x+4$: fonction polynome de degré 2

$v(x) = \sqrt(x)$ 
$D_u$: ensemble de définition: $d_u=\R$
$D_v$: ensemble de définition de v: $d_v=\R+ = [0; +\infin[$


a) calculer  v(u(1))

D'abord u(1)= puis v(u(1) = v(9) = \sqrt{8} = 2\sqrt{2}

b) Déterminer le signe de u(x):

signe de $x² + 3x + 4$: On $a: a=1; b=3; c=4$, On calcule $\Delta = b² - 4ac = 3²-4*1*1 = 9-16 = -7$
$\Delta = -7$

Conséquance? L'équation n'admet pas de solution 
Resutlat: $\forall x \in \R, u(x) = x² + 3x+4$ a le même signe que $a=1$

Donc: $\forall x \in \R, 0<u(x)$

c) Pour $x \in \R$, on peut donc calculer $v(u(x))$
$v(u(x))$ : Comment la calculer Dans l'expression $v(x) = \sqrt x$, on remplace x par u(x), on obtent alos:
 
$v(u(x)) = \sqrt{u(x)} =\sqrt{x²+3x+4}$

La fonction obtenue, f, définie pour $x \in \R$, par:
$f(x) = \sqrt{x²+3x+4}$ est appelée composée de u suivie de v et se note v: $v \circ u$

N°=2) 

$u(x)= exp(x) = e^x; v(x) = x²-1$: Reprendre les questions de l'ex 1

Rappels: exp: designe la fonction exponentielle

$e \in \R, exp(1) = e$

---
| $exp$ est define sur $\R$
| pour tt x \in \R, $0< e^x$
| $e⁰ = 1; e¹ = e$
| Pour $a \in \R, b \in \R$, 
| $e^{a+b} = e^a * e^b,\\ e^{-a} = \frac{1}{e^a} \\e^{a-b} = \frac{e^a}{e^b} \\(e^a)^{n} = e^{a*n}$ 
---
exp est dérivable sur \R
et pour x \in \R, $(exp)'(x) = exp(x)$ en particulier exp est strictement croissancet sur $\R$

$u(x)$ est definie sur $\R$

a) $v(u(1))$ D'abord $u(1) = e¹ = e$ puis $v(e)=e² -1$: $v(u(1))= e² -1$
b) $D_u = \R$ , $D_v = \R$; v étant un polynome de degré 2:
c) Pour $x \in \R, u(x) \in \R$ et la fonction x est définir sur $\R$
on peut donc calculer $v(u(x))$
$v(u(x)) = v(e^x) = (e^x)^2 -1 = e^{2x} -1$

BILAN: pour $x \in \R$, $(v \circ u)(x) = e^{2x} - 1$

d) pour x \in \R:
$(v \circ u)(x) = u(x(v)) = u(x²-1) = e^{x²-1}$

e) on a: $(u \circ v)(1) = e^{1^2-1}= e⁰ = 1$

soit $u(v(1)) = 1$

Les 2 nombres: $e^2 -1$ et $1$ sont differents donc $(v \circ u)(1) \neq (u \circ v)(1)$

---
| :warning: Attention: en général les 2 fonctions $v \circ u \neq u \circ v$
---

#### 2) Définition et Notation

Soit $u$ une fonction définie sur un intervalle $I$ (1)
et $v$ une fonction définie sur un intervalle $J$ (2)
telle que: 
$\forall x \in I, u(x) \in J$ (3)

La fonction définie sur l'intervalle $I$ par: pour $x \in I, f(x) = v(u(x))$ est appelée: fonction composée de la fonction $u$ suivie de la fonction $v$.
Et se note $f = v \circ u$

Shema de base pour comprendre la définition:

[...] (1)

#### 3) Dans la pratique
Dans certain cas, on devra décomposer, une fonction $f$ donnée sous la forme $v \circ u$ en précisant les fonction $u$ et $v$

Dans les exemples suivants, on ne se préocupe pas des ensembles de définitions.

N°1) 
$f(x) = \sqrt{3x^4+x^2+2}$

on pose $u = 3x^4+x^2+2$ et $v = \sqrt{x}$
On a $f(x) = \sqrt{u(x)} = v(u(x)) = (v \circ u)(x)$

Ainsi $f = v \circ u$

N°2)

$f(x) = e^{\frac{3x}{x-1}}$

On pose $u(x) = \frac{3x}{x-1}$ et $v(x) = e^{x}$

On a $f(x) = e^{u(x)} = v(u(x))$

Ainsi $f = v \circ u$, $D_f = \R -\{1\}$ 


#### 4) Dérivée d'une composée

##### a) Théorème:

| Soit $u$ une fontion dérivable sur un intervalle $I$
---
| Soit $v$ une fontion dérivable sur un intervalle $J$
| tellesque: pour tout $x \in I, v(x) \in J$
| On a: $v \circ u$ est dérivable sur $I$ 
| ET pour tout $x \in I$, $(v \circ v)'(x)$
| Se note $(v \circ u)' = (v' \circ u) * u'$


N°1:
$f(x) = \sqrt{3x^4+x^2+2}$

on a $u(x) = 3x^4+x^2+2$ , u est dérivable sur $I = \R$

Et $\forall x \in \R, u'(x) = 3*4x³ +2x= 12x³+2x$

Puis $v(x) = \sqrt{x}$ , v est dérivable sur $J = ]0+\infin[$

Et pour $x \in ]0; \infin[, v'(x) = \frac{1}{2\sqrt x}$

Puis il faut vérifier que:

pour $x \in \R$, $u(x) \in ]0; \infin[$
En effet, pour $x \in R$, $3x⁴+x²+2 \geq 2 >0$


<u>Que dit le théorème précédant?</u>

$f = v \circ u$ est dérivable sur $I = \R$ et
pour $x \in \R, f'(x) = v'(u(x))*u'(x)$


or $u'(x) = 12x³+2x$ et $v'(x) = \frac{1}{\sqrt x}$
donc, $v'(u(x)) = \frac{1}{2 \sqrt{u(x)}} = \frac{1}{2 \sqrt{3x⁴+x²+2}}$


Puis $f'(x) = \frac{12x³+2x}{2\sqrt{3x⁴+x²+2}} = \frac{x(6x²+1)}{\sqrt{3x⁴+x²+2}}$

On peut établir le tableau des varations de f
Signe de $f'(x)$ est le même que $x$

Exemple:
oOn a: $u(x) = \frac{3x}{x-1}$

u est une fonction rationelle, c'est a dire. quoitient de 2 fractions polynomes.

$I = D_u = \R/{1} = ]-oo; 1[ \cup ]1; +oo[$

u est dérivble sur I

pour $x \in I$, $[...]$

---

$f(x) = exp(3x/(x-1)) = e^{\frac{3x}{x-1}}$
on pose $u(x) = 3x/(x-1)$

u est dérivable sur $I = ]-\infin; 1[\cap]A;+\infin[$

et pour $x \in u'(x) = \frac{3(x-1)- 3x*1}{(x-1)^2}= \frac{3x-3- 3x}{(x-1)^2}$

| $u'(x) = \frac{-3}{(x-1)^2}$
---

on pose $v(x) = e^x$
$v$ est dérivable sur $J = \R$

et pour $x \in \R, v'(x) = e^x$

On verifie que:
pour tout $x \in I$, $u(x) \in J$ Soit pour tout $x \in ]-\infin; 1[\cap]A;+\infin[$ = $u(x) \in \R$

Que dit le théorème précédant?

La fonction $f = v \circ u$ est dérivable sur $I$
et pour $x \in I$

| $f'(x) = v'(u(x))$

Soit $f'(x) = exp(3x/x-1) * -3/(x-1)^2$

Bilan

| $f()$
---
[...] (Photo telephone avant le 28.09 surement le 27.09)

---




#### 5) CAS PARTICULIER, Du théorème précédant


$u$ désigne une fonction dérivable sur un intervalle $I$

Premier cas: $f = e^u = exp(u)$
D'abort pour $x \in I$, $f(x) = e^{u(x)} = exp(u(x))$
Etude de la dérivabilité de $f$:

On décompose $f$ comme une composée de 2 fonctions:

on pose $v = exp$
on a pour $x \in I, f(x) = exp(u(x)) = v(u(x))$
Donc $f = v \circ u$

On a:
(1): $u$ dérivable sur un intervalle $I$
(2): $v$ dérivable sur un intervalle $J = \R$
(3): pour tout $x \in  I, u(x) \in J$

D'apres le théoreme énonce au paragraphe 4:

$f = v \circ u$ est dérivable sur $I$

Et pour $x \in, f'(x) = v'(u(x)) * u'(x)$

on a $v'(x) = (\exp)'(x) = e^x$

Ainsi: pour $x \in I$, $f'(x) = \exp(u(x)) * u'(x) = u'(x)*e^{u(x)}$

| Propriété: $u$ est une fonction dérivable sur l'intervalle $I$
---
| on a: $e^u$ dérivable sur $I$ Et $(e^{u})' = u'e^u$

exemple: 

$f(x) = e^{2x^2-3x+4}$

étudier la dérivabilité de $f$

Je pose $u(x) = 2x²-3x+4$
$u$ est dérivable sur $I = \R$
on a $f = e^{u}$
Par propriété $f$ est dérivable sur $I = \R$ et pour $x \in \R, f'(x) = 2x²-3x+4$

$f'(x) = (4x-3)*e$

**Deuxième cas**: $f = \sqrt{u}$

$u$ est strictement positive et dérivable sur $I$

On pose $v(x) = \sqrt(x)$ on a $f v \circ o$
on peux affirmer , par application du théorème précédant du paragraphe 4 que:

Propriété:
$u$ est une fonction strictement positive et dérivable sur $I$

on a : $\sqrt{u}$ est dérivable sur $I$

ET : $(\sqrt{u})' = \frac{1}{2\sqrt u} \times u' =\frac{u'}{2\sqrt u}$

exemple: $f(x) = \sqrt{2x-2}$

Je pose $u(x) = 3x-2$

Signe de $u(x) = 3x-2$

| x |  -oo     2/3        =oo
|------|---------------------
|      |Signe - / +  de a
| 3x-2 |   -    0     +
a = 3

u est dérivable et strictement positive sur $I = ]2/3; +\infin[$
S'apres la proprité

$f = \sqrt{u}$ est dérivable sur I

| ET : $f'(x) = \frac{u'(x)}{2\sqrt{u(x)}} = \frac{3}{2\sqrt{3x-2}}$
---


Troisieme cas: 
$f = u^n$

$n \in \N^*$

$u$ est un fonction dérivable sur un intervalle $I$ on pose $v(x) = x^n$
ON peux affirmer, par l'application du théorème précédant du paragraphe 4 que:

Propriété:

$u$ est une fonction sur un onstervalle $I$

On a $u^n$ est dérivable sur $I$

| ET : $(u^n)' = nu(n-1) \times u'$
---

exemple; $f(x) = (x²-2x)⁴, \;\;;  I=\R$

On pose $u(x) = x^2-2x$
On a $f = u^4$
u est dérivable sur $I=\R$
Donc par propriété $f=u^4$ est dérivable sur $I = \R$

Et pour $x \in \R, f'(x) = 4x(x²-2x)*(2x-2)$

| $f'(x) = 4(2x-2)(x²-2x)³$
---

La formule précédante se généralise au cas ou n est un entier négatif, **mais** il faut supposer en plus que $u$ ne s'annule pas sur $I$.

---

### **Paragraphe 2:** Dérivées successives

#### 1) Dérivées seconde:

##### a) Définition:

Soit f une fonction dérivable, telle que $f'$ et aussi dérivable sur le même intervalle $I$
La fonction dérivée de $f'$, notes $(f')'= f''$ est appelées <u>dérivée seconde</u> de $f$

##### b) Propriété:
Le signe de $f''$ sur l'intervalle I rensigne sur le sens: le sens de varations de $f''$ sur l'intervalle $I$

Exemple: $f(x) = 2x^3-3x^2+5x+7, I= \R$

Calculer $f''(x)$

$x \in \R, f'(x) = 6x² -6x +5$
$f''(x) = 12x-6$

---

Exemple: 

> $f(x) = e^x -x -1$
> 1) Calculer $f'(x)$ et $f''(x)$
> 2) Etablir le sens de variation de f'(x) en indiquant f'(o)
> 1) Pour x \in \R: f'(x) = e^x -1 , f''(x)= e^x


$f(x) = e^x - x - 1; I = \R$

2) etablir le tableau de varatuion de f', en indiquand f'(0)
on sais que, $\forall x \in \R, 0 < e^x$

```table
x   | -oo 0 +oo
----------------
f''x| +   |  + |
f'x | /   0  / |
```

$f'(x) = e^0 -1= 1-1 = 0$
3a) déduire le signe de f'(x).
D'apres le tableau des varations précedent:

```
f'(x) - 0 +
```

b) on peut donner le tableau de carations

```
f'(x) - 0 +
---
f(x)  \ 0 /
```

$f(0) = e^0 -0-1 = 1-1=0$

Le minimum de f sur \R est f(0) = 0

donc: pour $x \in \R$, $0 \leq f(x)$
donc: pour $x \in \R$, $0 \leq e^x-x-1$
donc: pour $x \in \R$, $x+1 \leq e^x$

#### 2) Dérivées successives d'une fonction.

##### a) définition:
f est une fonction définie sur un intervalle $I$ et n $\in \N^*$

Lorsque on peut dériver successivement n fois la fonction $f$, on obtient la fonction dérivé d'ordre n de $f$

Elle se note $f^{(n)}$

A noter que: $f^{(n+1)} = f^{(n)}$'

##### b) exemples:

N°1) $f = exp$
on a pour $n \in \N^*, f^{(n)} = exp$

N°2)
$f(x) = 2x^3 - 7x^2 + 4x + 1$
pour $x \in \R$
$f'(x) = 6x^2 - 14x +4$
$f''(x) = 12x -14$
$f^{(3)}(x) = 13$
$f^{(4)}(x) = 0$

### III) Fonctions  convexes - Concaves

#### 1) définitions:

##### a) définitions 1:

[... 2 Shema figures 1]

On a $A(a; f(a))$ et $B(b; f(b))$
Le point M a pour cordonnées. $M(x; f(x)) \in C$
$N(x; Y_N) \in [A;B]$
$Y_N = m(x-a) + f(a)$
On donne une équation de la droite $(AB)$
Le point N est au dessus du point M revient à dire que $Y_M \leq Y_N$

(AB): y= mx+p

avec $m = \frac{y_B-y_A}{x_B-x_A} = \frac{f(x)-f(a)}{b-a}$

Cette droite passe par A(a; f(a))
Donc $y_A = mx_a +p$
Donc $f(a)= ma +p$

| Donc $f(a) - ma = p$
---
ENFIN: (AB): y = mx+f(a)-ma
(AB): y = m(x-a)+f(a)

Le point N d'abscisse x, situé sur le segment [AB] a pour ordonée $y_N = m(x-a)+f(a)$

Dire que le point N est au dessus que le point M, revient a dire que: $y_M \leq y_N$

---


Soit petit $f$, une fonction définie sur grand J et C la courbe represantaive de f sur I.
On dit que est convexe sur l'intervalle I, lorsque pour tt point A et B de la cource C le segemenet $[AB]$, situeé au dessus de l'arc de courbe [AB ...]

Commentaires:
- D'apres l'étude précédante pou tout $x \in [a;b]$
$f(x) \leq m(x-a) + f(x) avec m = \frac{f(b) - f(a)}{b-a}$
Soit k le mileu du segment $[AB]$

[... 3 Shema figure 2]

les cordonées de k sont $k(\frac{a+b}{2}; \frac{f(a)+f(b)}{2})$

Soit $L$ le point de C d'abscisse (a+b)/2 on a $Y_L = f(\frac{a+b}{2})$

On a L est en dessous de K

Donc $Y_L \leq Y_K$

Donc: $f(\frac{a+b}{2}) \leq \frac{f(a)+f(b)}{2}$

figure 2:
[... 4 Shema figure 2]

On dit que. la fonction est concave sur lintervale I, lorsque poiur tout point A et B de la Courbe C, le segment [AB]. est situé en sessous de l'arc de courve [AB...]
$\overset{\frown}{AB}$

AUTRE Définition: qui peut être considéré comme propriété
<u>Définition 2</u>: f est une fonction définie et dérivable sur un intervalle I
$C$ est la courbe represantative de f

[figure 1...def2]

f converse sur un intervalle I, lorsque pour tout pint A(a; f(a)) de C avec a \in I la tangente au point A à la courbe C est située en dessous de la courbe C, sur l'intervalle I

Signification
Soit a \in I et A(a; f(a)
T(a): y=f'(a)(x-a)+f(a)
T(a) est en dessous de C sur I signifie que pour tout x \in I, f'(a)(x-a)+f(a) \leq f(x)


[figure 1...def2]
f concave sur un intervalle I, lorsque pour tout pint A(a; f(a)) de C avec a \in I la tangente au point A à la courbe C est située en dessus de la courbe C, sur l'intervalle I

Signification
Soit a \in I et A(a; f(a)
T(a): y=f'(a)(x-a)+f(a)
T(a) est en dessous de C sur I signifie que pour tout x \in I, f'(a)(x-a)+f(a) \leq f(x)

Définiton 3: point d'infléxion à une courbe représentative

[figure3 ..def3]


Le point A de cordonée A(a, f(a)) est un point d'inflexion à la courbe C, lorsque la courbe C traverse la tanganteau point A

conséquances:
En abscice a d'un point d'intersection passe de concave à convexe ou bien de convexe à concave

2) exemple: cas de contion exp

[shema cas exp]

Soit a \in \R, A(a, e^a)
équation de la tangente au point d'abcisse a
T_A: y= e^a(x-a)+e^a
T_A: y=e^ax-e^aa+e^a

T_A represante la fonction affine de g

g(x) = e^ax-e^aa+e^a
exp est convexe sur \R

on va étudier le signe de exp(x)-g(x)
pour evaluer la position de C et T_A

On pose: h(x) = e^x -g(x)

Ainsi h(x) = e^x-(e^ax-e^aa+e^a)
h(x) = e^x-e^ax+e^a-e^a

on étudie le ense de varation de h sur R, pour pouvoir dpnner le signe de h(x) siur R

pour $x \in R, h'(x) = e^x-e^a*1$

