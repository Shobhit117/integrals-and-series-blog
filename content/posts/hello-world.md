Title: Simplification of Incomplete Beta Functions
Date: 2020-01-24 07:47:14 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: hello-world
Author: Shobhit Bhatnagar
Category: Elliptic Functions and Integrals
Tags: elliptic-integrals, elliptic-functions, beta-function
Summary: Two incomplete beta integrals, evaluated through substitutions and the addition formulas for the Weierstrass elliptic function.
Status: published
WordPress_ID: 1

We will evaluate two algebraic integrals by rewriting them as incomplete beta functions. The first yields to a pair of substitutions; the second leads to the addition and duplication formulas for the Weierstrass elliptic function.

$$
\begin{align}
\int_0^1\frac{dx}{\sqrt{1-x}\sqrt[6]{9-x}\sqrt[3]x}&=\frac\pi{\sqrt3} \label{hello-world-eq-1}\\
\int_0^1\frac{dx}{\sqrt{1-x}\sqrt[4]x\sqrt[4]{2-x\sqrt3}} &= \frac{2\sqrt{2}\pi}{3\sqrt[8]{3}} \label{hello-world-eq-2}
\end{align}
$$

These problems are from a [math.stackexchange.com](https://math.stackexchange.com/questions/541135/conjecture-int-01-frac-mathrm-dx-sqrt1-x-sqrt4x-sqrt42-x-sqrt) question posted by [Vladimir Reshetnikov](https://math.stackexchange.com/users/19661/vladimir-reshetnikov?tab=questions).

## Alternate forms

The equations $\eqref{hello-world-eq-1}$ and $\eqref{hello-world-eq-2}$ can be expressed in terms of the incomplete beta function using some elementary hypergeometric identities. This makes our problems equivalent to proving that

$$
\begin{align}
B\left(\frac{1}{9};\frac{1}{6},\frac{1}{3}\right) &= \frac{\sqrt{3}}{2^{\frac{4}{3}}\pi}\Gamma\left(\frac{1}{3}\right)^3 \label{hello-world-eq-3}\\
B\left(\frac{\sqrt{3}}{2};\frac{1}{4},\frac{1}{4}\right) &= \frac{2}{3\sqrt{\pi}}\Gamma\left(\frac{1}{4}\right)^2 \label{hello-world-eq-4}
\end{align}
$$

**Proof of $\eqref{hello-world-eq-3}$**

$$
B\left(\frac{1}{9};\frac{1}{6},\frac{1}{3}\right)  = \int_0^{\frac{1}{9}}x^{-\frac{5}{6}}\left( 1-x\right)^{-\frac{2}{3}} dx
$$

Substitute $x=\frac{y^3}{1+y^3}$ in the above integral to get

$$
B\left(\frac{1}{9};\frac{1}{6},\frac{1}{3}\right) =3\int_0^{\frac{1}{2}}\frac{1}{\sqrt{y+y^4}}dy
$$

We can now transform this integral into a beta integral using the substitution $y=\frac{1-z}{2+z}$.

$$
B\left(\frac{1}{9};\frac{1}{6},\frac{1}{3}\right)  =3\int_0^1\frac{1}{\sqrt{1-z^3}}dz = B\left( \frac{1}{3},\frac{1}{2}\right)=\frac{\sqrt{3}}{2^{\frac{4}{3}}\pi}\Gamma\left(\frac{1}{3}\right)^3
$$

This proves equations $\eqref{hello-world-eq-1}$ and $\eqref{hello-world-eq-3}$.

## Proof of $\eqref{hello-world-eq-4}$

The proof of integrals $\eqref{hello-world-eq-2}$ and $\eqref{hello-world-eq-4}$ is more involved. Using the substitution $x=\frac{4t^2}{1+4t^2}$, the integral transforms into the Weierstrass form:

$$
B\left(\frac{\sqrt{3}}{2};\frac{1}{4},\frac{1}{4}\right) =\int_0^{\frac{\sqrt{3}}{2}}x^{-\frac{3}{4}}(1-x)^{-\frac{3}{4}}dx=2\sqrt{2} \int_0^\alpha \frac{dt}{\sqrt{4t^3+t}}
$$

where $\alpha=\frac{\sqrt{3+2\sqrt{3}}}{2}$. Let $\wp(z)$ denote the Weierstrass Elliptic function with invariants $g_2=-1$ and $g_3=0$. $\wp(z)$ satisfies the differential equation:

$$
\wp'(z)^2=4\wp(z)^3+\wp(z)
$$

The half periods are $\omega_1=\frac{1+i}{4}L$ and $\omega_2=\frac{-1+i}{4}L$ where $L=\frac{1}{\sqrt{2\pi}}\Gamma\left(\frac{1}{4}\right)^2$ is the Lemniscate constant. Now, we can express our integral as follows:

$$
B\left(\frac{\sqrt{3}}{2};\frac{1}{4},\frac{1}{4}\right) =2\sqrt{2}\left(\wp^{-1}(0)-\wp^{-1}(\alpha) \right)
$$

Note that the following identity is easy to prove using the beta function:

$$
\int_0^\infty \frac{dt}{\sqrt{4t^3+t}}=\frac{1}{2\sqrt{2\pi}}\Gamma\left(\frac{1}{4}\right)^2=\frac{L}{2}
$$

Therefore, $\wp^{-1}(0)=\frac{L}{2}$. To prove the claim we only need to prove that $\wp\left(\frac{L}{6}\right)=\alpha$. Using the addition theorem of $\wp(z)$ and the fact that $\wp\left(\frac{L}{2}\right)=0$ we get:

$$
\begin{equation}\label{hello-world-eq-5}
\begin{aligned}
\wp\left(\frac{L}{6}\right) &= \wp\left(\frac{L}{2}-\frac{L}{3}\right)\\
&= \frac{1}{4}\left(\frac{\wp'\left(\frac{L}{3}\right)}{\wp\left(\frac{L}{3}\right)} \right)^2-\wp\left(\frac{L}{3}\right) \\
&= \frac{4\wp\left( \frac{L}{3}\right)^3+\wp\left(\frac{L}{3}\right)}{4\wp\left(\frac{L}{3}\right)^2}-\wp\left(\frac{L}{3}\right)\\
&= \frac{1}{4\wp\left(\frac{L}{3}\right)}
\end{aligned}
\end{equation}
$$

On the other hand, by the duplication theorem:

$$
\begin{equation}\label{hello-world-eq-6}
\begin{aligned} \wp\left(\frac{L}{3}\right)&= \frac{1}{4}\frac{\left(6\wp\left(\frac{L}{6}\right)^2+\frac{1}{2}\right)^2}{4\wp\left(\frac{L}{6}\right)^3+\wp\left(\frac{L}{6}\right)}-2\wp\left(\frac{L}{6}\right) \end{aligned}
\end{equation}
$$

Combine equations $\eqref{hello-world-eq-5}$ and $\eqref{hello-world-eq-6}$ to get:

$$
\frac{1+4\wp\left(\frac{L}{6}\right)^2}{\left(6\wp\left(\frac{L}{6}\right)^2+\frac{1}{2} \right)^2-32\wp\left(\frac{L}{6}\right)^4-8\wp\left(\frac{L}{6}\right)^2}=1 \\
\implies 16\wp\left(\frac{L}{6}\right)^4-24\wp\left(\frac{L}{6}\right)^2-3=0
$$

Since $\wp\left( \frac{L}{6}\right)$ is positive, we conclude that

$$
\wp\left(\frac{L}{6}\right)=\frac{\sqrt{3+2\sqrt{3}}}{2}
$$

This completes our proof of equation $\eqref{hello-world-eq-4}$ and $\eqref{hello-world-eq-2}$.
