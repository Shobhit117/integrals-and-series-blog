Title: When is the group of units in the integers modulo n cyclic?
Date: 2020-12-12 13:22:20 +0000
Modified: 2025-11-10 06:10:03 +0000
Slug: the-group-of-units-in-the-integers-modulo-n
Author: Shobhit Bhatnagar
Category: Number Theory
Tags: abstract-algebra, number-theory
Summary: A proof of the classification of integers whose multiplicative group of units is cyclic.
Status: published
WordPress_ID: 793

We begin with the multiplicative group of units modulo an integer. By [Bezout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity) that the integers co-prime to $n$ from the set $\{0,1,\cdots, n-1\}$ form a group under multiplication modulo $n$. This group is denoted by $(\mathbb{Z}/n\mathbb{Z})^*$ and its order is given by the [Euler's Totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function): $\varphi(n) = |(\mathbb{Z}/n\mathbb{Z})^*|$. 

## The classification

Gauss showed that $(\mathbb{Z}/n\mathbb{Z})^*$ is a cyclic group if and only if $n=1,2,4,p,p^k$ or $2p^k$, where $p$ is an odd prime and $k > 0$. It is very easy to verify this for $n=1,2$ and $4$, as one can simply list out all positive integers less than and co-prime to $n$. So, we will only focus on proving that $(\mathbb{Z}/n\mathbb{Z})^*$ is cyclic for the remaining three cases.

**Theorem 1:**  $(\mathbb{Z}/p\mathbb{Z})^*$ is cyclic if $p$ is a prime.

**Proof:**  Let $d_1, d_2, \cdots , d_r$ be all the possible orders of the elements of $(\mathbb{Z}/p\mathbb{Z})^*$. Let $e=\text{lcm}(d_1, d_2, \cdots, d_r)$ and factor $e=p_1^{a_1} p_2^{a_2}\cdots p_k^{a_k}$ as a product of distinct prime powers. By the definition of $\text{lcm}$, for each $p_i^{a_i}$ there is some $d_j$ divisible by it. Since the $d_j$'s are orders of elements of $(\mathbb{Z}/p\mathbb{Z})^*$, there is an element $x_i$ whose order is $p_i^{a_i} t$. Then, the element $y_i = x_i^t$ has order $p_i^{a_i}$. Hence, $y_1 y_2\cdots y_k$ has order $e$. Thus, we have found an element of order $e$. Therefore, $e|p-1$. But the polynomial $x^e-1$ has $p-1$ roots $(\text{mod }p)$. Since $\mathbb{Z}/p\mathbb{Z}$ is a field, any polynomial of degree $e$ cannot have more than $e$ roots. Therefore, $p-1\leq e$ and we deduce that $e=p-1$. Thus, we have found an element of order $p-1$.

**Theorem 2:**  $(\mathbb{Z}/p^a \mathbb{Z})^*$ is cyclic for any $a\geq 1$ if $p$ is an odd prime.

**Proof:** For $a=1$, we are done by Theorem 1. Let $g$ be a primitive root $(\text{mod }p)$. We first find a $t$ such that $(g+pt)^{p-1}\not\equiv 1 \; (\text{mod }p^2)$. If $g^{p-1}\not\equiv 1 \; (\text{mod }p^2)$, then we can take $t=0$. Otherwise, we can choose $t=1$. Indeed, we have $(g+p)^{p-1}\equiv 1+p(p-1)  g^{p-2} \not \equiv 1 \; (\text{mod }p^2)$. Let $g+pt$ have order $d\; (\text{mod }p^a)$. Then, $d|p^{a-1} (p-1)$. Since $g$ is a primitive root modulo $p$, $(p-1) | d$. So, $d=p^{r-1} (p-1)$ for some $r\leq a$. We also know that $(g+pt)^{p-1} = 1+p s$ where $p\nmid s$. Thus,

$$
\begin{aligned}
(g+pt)^{p(p-1)} &= (1+ps)^{p} \\
&= \sum_{i=0}^{p} \binom{p}{i} (ps)^i  \\
&\equiv 1+p^2 s \; (\text{mod }p^3)
\end{aligned}
$$

By induction, it follows that

$$
(g+pt)^{p^{b-1}(p-1)} \equiv 1+p^b s \; (\text{mod }p^{b+1})
$$

Now, $g+pt$ has order $d=p^{r-1}(p-1)\; (\text{mod } p^a)$ which implies $(g+pt)^{p^{r-1}(p-1)} \equiv 1 \; (\text{mod }p^a)$. But then $1+p^r s \equiv 1 \; (\text{mod } p^{r+1})$ if $r\leq a-1$, which implies $p | s$, a contradiction. Thus, $r=a$.

**Theorem 3:** $(\mathbb{Z}/2p^a \mathbb{Z})^*$ is cyclic for any $a\geq 1$ if $p$ is an odd prime.

**Proof:** This follows immediately from Theorem 2 and the [Chinese remainder theorem](https://math.stackexchange.com/questions/1659507/chinese-remainder-theorem-induces-a-unit-group-isomorphism).

## Why there are no other cases

Suppose first that $n$ has two distinct odd prime factors, $p$ and $q$. Choosing a sign independently modulo each prime power and applying the Chinese remainder theorem gives at least four solutions of $x^2\equiv1\pmod n$. A cyclic group has at most two elements whose square is the identity, so its unit group cannot be cyclic.

If $4\mid n$ and an odd prime divides $n$, the same argument applies by choosing signs independently modulo the power of $2$ and the odd part. Finally, if $8\mid n$, the four residues $1,-1,1+2^{a-1},-1+2^{a-1}$ are distinct square roots of $1$ modulo $2^a$ for $a\geq3$; the Chinese remainder theorem again transfers this obstruction to $n$.

The only remaining possibilities are $1,2,4,p^a$, and $2p^a$ with $p$ odd, exactly the cases already proved.

## References

- M. Ram Murty. *Problems in analytic number theory*. Springer New York, 01-Nov-2008
