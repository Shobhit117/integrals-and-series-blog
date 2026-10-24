Title: Eisenstein's Proof of Quadratic Reciprocity
Date: 2020-01-25 16:47:43 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: eisensteins-proof-of-quadratic-reciprocity
Author: Shobhit Bhatnagar
Category: Number Theory
Tags: number-theory, abstract-algebra
Summary: Eisenstein's trigonometric proof of quadratic reciprocity, starting with Euler's criterion and Gauss's lemma.
Status: published
WordPress_ID: 21

Eisenstein's proof of quadratic reciprocity turns a question about quadratic residues into a symmetry between two products of sines. We will first establish Euler's criterion and Gauss's lemma, then use them to identify the sign of that product.

**Definition:** For an odd prime $p$, the Legendre symbol $\left(\frac{a}{p}\right)$ records whether $a$ is a nonzero square modulo $p$; it is zero when $p$ divides $a$.

$$
\left(\frac{a}{p}\right) = \begin{cases}0 \quad \text{if }p|a \\ 1 \quad \text{if }a\text{ is a quadratic residue modulo }p \\ -1 \quad \text{if }a\text{ is a quadratic non-residue modulo }p\end{cases}
$$

**Theorem (Quadratic Reciprocity Law):** If $p$ and $q$ are distinct odd primes, then the quadratic reciprocity theorem states that the congruences

$$
\begin{aligned} x^2 \equiv q \quad (\text{mod }p) \\ x^2 \equiv p \quad (\text{mod }q) \end{aligned}
$$

are both solvable or both unsolvable unless both $p$ and $q$ leave the remainder $3$ when divided by $4$. Written symbolically,

$$
\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{(p-1)(q-1)/4}
$$

We will start by proving two important results about quadratic residues that will be useful later on.

**Lemma 1:** Let $n\not\equiv 0 \;(\text{mod }p)$. Then $n$ is a quadratic residue modulo $p$ iff $n^{\frac{p-1}{2}}\equiv 1 \; (\text{mod }p)$.

**Proof:** Fermat's little theorem tells us that $n^{p-1}\equiv 1 \;(\text{mod }p)$ whenever $p \not| n$. Since,

$$
n^{p-1}-1\equiv (n^{\frac{p-1}{2}}-1)(n^{\frac{p-1}{2}}+1)\equiv 0 \; (\text{mod }p)
$$

we have $n^{\frac{p-1}{2}}\equiv \pm 1\; (\text{mod }p)$. Therefore, it suffices to prove that $n$ is a quadratic residue modulo $p$ if and only if $n^{\frac{p-1}{2}}\equiv 1 \; (\text{mod }p)$.

Suppose that $\left(\frac{n}{p} \right)=1$. Then, there is an integer $x$ such that $n\equiv x^2 \; (\text{mod p})$. Now, we have

$$
n^{\frac{p-1}{2}}\equiv x^{p-1} \equiv 1 \equiv \left(\frac{n}{p} \right) \; (\text{mod }p)
$$

Conversely, assume that $n^{\frac{p-1}{2}}\equiv 1 \; (\text{mod }p)$. Let $g$ be a primitive root of $p$. Then, we have $n\equiv g^k \; (\text{mod }p)$ for some integer $k$. Since $n^{\frac{p-1}{2}}\equiv g^{\frac{k(p-1)}{2}} \equiv 1 \; (\text{mod }p)$, the order of $g$ must divide the exponent $\frac{k(p-1)}{2}$. Therefore, $p-1 | \frac{k(p-1)}{2}$ and thus $k$ is an even integer. Let's say $k=2j$ for some integer $j$. Then, we have

$$
n \equiv g^k \equiv g^{2j} \equiv (g^j)^2 \; (\text{mod }p)
$$

This proves that $n$ is a quadratic residue modulo $p$.

**Lemma 2 (Gauss's Lemma):** For any odd prime $p$, let $a$ be an integer that is co-prime to $p$. Consider the integers

$$
S = \left\{ a,\ 2a,\ 3a,\cdots, \frac{p-1}{2}a \right\}
$$

and their least positive residues modulo $p$. Let $n$ be the number of these residues that are greater than $p/2$. Then

$$
\left(\frac{a}{p}\right)=(-1)^n
$$

**Proof:** Since $p\not | a$, none of the integers in $S$ are congruent to 0 and no two of them are congruent to each other modulo $p$. Let $r_1, \cdots, r_m$ be the residues modulo $p$ smaller than $\frac{p}{2}$, and let $s_1, \cdots, s_n$ be the residues modulo $p$ greater than $\frac{p}{2}$. Then $m+n=\frac{p-1}{2}$ and the integers

$$
r_1, \cdots, r_m, p-s_1, \cdots , p-s_n
$$

are all positive and less than $\frac{p}{2}$. Now, we will prove that no two of these integers are equal. Suppose that for some choice of $i$ and $j$ we have $p-s_i = r_j$. We can choose integers $u$ and $v$, with $1 \leq u,v \leq \frac{p-1}{2}$ and satisfying

$$
\begin{aligned}
s_i &\equiv u a \; (\text{mod }p) \\
r_j &\equiv v a \; (\text{mod }p)
\end{aligned}
$$

Now, we have

$$
s_i+r_j \equiv a(u+v) \equiv p \equiv 0 \; (\text{mod }p)
$$

This implies that $u+v \equiv 0 \; (\text{mod }p)$. However, this is not possible because $1\leq u+v \leq p-1$. Thus, we have proven that the numbers $r_1,\cdots, r_m, p-s_1, \cdots p-s_n$ are simply a rearrangement of the integers $1,2,\cdots, \frac{p-1}{2}$. Their product is equal to $\left(\frac{p-1}{2} \right)!$. Therefore,

$$
\begin{aligned}
\left(\frac{p-1}{2}\right)! &= r_1 \cdots r_m (p-s_1)\cdots (p-s_n) \\
&\equiv (-1)^n r_1 \cdots r_m s_1\cdots s_n \; (\text{mod }p) \\
&\equiv (-1)^n a\cdot 2a\cdots \left(\frac{p-1}{2}\right)a \; (\text{mod }p) \\
&\equiv (-1)^n a^{\frac{p-1}{2}} \left( \frac{p-1}{2}\right)! \; (\text{mod }p)
\end{aligned}
$$

The $\left( \frac{p-1}{2}\right)!$ term can be cancelled from both sides as $p\not| \left( \frac{p-1}{2}\right)!$. In other words, we have $a^{\frac{p-1}{2}}\equiv (-1)^n \; (\text{mod }p)$. This completes the proof of Gauss's lemma.

We are now ready to prove the Quadratic reciprocity theorem.

## Proof of the Quadratic Reciprocity Theorem:

Using the periodicity properties of $\sin$ and Gauss's lemma, it is easy to verify the following result:

**Lemma:** Let $p$ and $q$ be distinct odd primes and let $A = \left\{ \alpha\in \mathbb{Z} | 1\leq \alpha \leq \frac{p-1}{2}\right\}$ be a half system modulo $p$. Then,

$$
\begin{equation}\label{eisensteins-proof-of-quadratic-reciprocity-eq-1}
\left(\frac{q}{p}\right) = \prod_{\alpha\in A}\frac{\sin\left(\frac{2\pi}{p}q\alpha\right)}{\sin\left(\frac{2\pi}{p}\alpha\right)}
\end{equation}
$$

We start by examining the right hand side of equation $\eqref{eisensteins-proof-of-quadratic-reciprocity-eq-1}$. The addition theorem for trigonometric functions yields $\sin 2\alpha = 2\sin\alpha\cos\alpha$ and $\sin 3\alpha = \sin\alpha(3-4\sin^2\alpha)$. Induction shows that $\sin q\alpha = \sin\alpha P(\sin\alpha)$ for all odd $q\geq 1$, where $P\in \mathbb{Z}[X]$ is a polynomial of degree $q-1$ and highest coefficient $(-4)^{\frac{q-1}{2}}$. After factoring out the leading coefficient, there are rational coefficients $a_i$ such that

$$
\begin{aligned}\frac{\sin qz}{\sin z} &= (-4)^{\frac{q-1}{2}} \left( (\sin z)^{q-1}+a_{q-2} (\sin z)^{q-2}+\cdots + a_0 \right) \\ &= (-4)^{\frac{q-1}{2}} \psi(X), \quad \text{where }X=\sin z\end{aligned}
$$

Since $\phi(z)=\frac{\sin qz}{\sin z}$ is an even function, so is $\psi(X)$, hence all coefficients of odd powers of $X$ vanish. Now $\phi(z)$ has zeros $\left\{ \pm \frac{2\pi}{q}\beta, \ 1\leq \beta \leq \frac{q-1}{2}\right\}$. Since $\psi$ is monic of degree $q-1$, we may write

$$
\psi(X) = \prod_{\beta\in B}\left(X^2-\sin^2\frac{2\pi\beta}{q} \right)
$$

where $B=\left\{1,\cdots,\frac{q-1}{2} \right\}$ is a half system modulo $q$. Replacing $X$ by $\sin z$, we get

$$
\begin{equation}\label{eisensteins-proof-of-quadratic-reciprocity-eq-2}
\frac{\sin qz}{\sin z} = (-4)^{\frac{q-1}{2}} \prod_{\beta\in B }\left( \sin^2z -\sin^2\frac{2\pi\beta}{q}\right)
\end{equation}
$$

Put $z=\frac{2\pi\alpha}{p}$ in equation $\eqref{eisensteins-proof-of-quadratic-reciprocity-eq-2}$ and plug the result into equation $\eqref{eisensteins-proof-of-quadratic-reciprocity-eq-1}$.

$$
\begin{equation}\label{eisensteins-proof-of-quadratic-reciprocity-eq-3}
\begin{aligned} \left(\frac{q}{p}\right) &= \prod_{\alpha\in A} (-4)^{\frac{q-1}{2}} \prod_{\beta\in B} \left( \sin^2\frac{2\pi\alpha}{p} -\sin^2\frac{2\pi\beta}{q}\right)\\ &= (-4)^{\frac{q-1}{2} \frac{p-1}{2}} \prod_{\alpha\in A}\prod_{\beta\in B} \left( \sin^2\frac{2\pi\alpha}{p} -\sin^2\frac{2\pi\beta}{q}\right) \end{aligned}
\end{equation}
$$

Exchanging $p$ and $q$ on the right side of $\eqref{eisensteins-proof-of-quadratic-reciprocity-eq-3}$ give rise to factor of $(-1)^{(p-1)(q-1)/4}$. Therefore,

$$
\begin{equation}\label{eisensteins-proof-of-quadratic-reciprocity-eq-4}
\left(\frac{q}{p}\right) = (-1)^{(p-1)(q-1)/4}\left(\frac{p}{q}\right)
\end{equation}
$$

which is the quadratic reciprocity law.

## References

- Lemmermeyer, Franz. "Reciprocity Laws: From Euler to Eisenstein". New York, Springer, 2000
- Burton, David M. "Elementary Number Theory". New Delhi, Tata McGraw-Hill Publishing Company Limited, May 1 2006
