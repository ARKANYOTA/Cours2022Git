---
title: '# Chap 1 - P2'
created: 2021-12-19T18:25:02.376Z
modified: 2021-12-19T18:33:41.145Z
---

# # Chap 1 - P2 
## V. Congruence 
### 1. Définition 
Deux entiers &a& et &b& sont **congrus modulo n** (&n in NN&) si leur différence est un multiple de &n&. On écrit alors &a -= b (n)&.

$$
\begin{aligned}
  \boxed{ a \equiv b \iff b - a \in n ℤ}\\
             \boxed{ \iff n | b-a}
\end{aligned}
$$

Conséquence: tout entier &a& est congruent à son modulo &n&.
En effet, la divison euclienne de &a& par &n& s'écrit:

&a = nq + r&
&a - r = nq&
donc &n|a-r iff a -= r (n)&

### 2. Propriétés
Soit &a in ZZ, a -= a (n)&
(la relation est **réflexive**)

&a - a = 0 = 0 xx n&
donc &n | a-a => a -= a (n)&

Si &a,b& deux entiers:
$\boxed{\text{si } a ≡ b (n) ⇒ b ≡ a (n)}$

(la relation est **symétrique**)

> **Preuve**
> 
> &a -= b (n)&
  &=> n | b-a&
> &=> n | (b-a) xx -1&
> &=> n | a-b&
> &=> b -= a (n)&

Si &a, b, c& 3 entiers 
$\boxed{\text{Si } a ≡ b (n) \text{ et } b ≡ c (n)}$


