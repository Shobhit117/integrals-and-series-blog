Title: Ramanujan's Master Theorem: Part I
Date: 2020-07-02 12:38:30 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: ramanujans-master-theorem-part-i
Author: Shobhit Bhatnagar
Category: Uncategorized
Tags: 
Summary: Use Ramanujan's master theorem to connect power-series coefficients with Mellin transforms of Bessel functions.
Status: published
WordPress_ID: 286

Ramanujan's master theorem (RMT) connects the coefficients of a power series with a Mellin transform. We will use this connection to evaluate integrals involving one Bessel function and a product of two Bessel functions.

## The master-theorem principle

Suppose that $f(z)$ has the expansion

$$
f(z) = \sum_{n=0}^\infty \frac{\varphi(n)}{n!}(-z)^n
$$

Under suitable analytic continuation and growth hypotheses on the coefficient function $\varphi$, the master theorem gives, in a strip where the integral converges,

$$
\int_0^\infty x^{s-1} f(x)\; dx = \Gamma(s) \varphi(-s)
$$

The hypotheses matter: the values $\varphi(n)$ at nonnegative integers alone do not determine $\varphi(-s)$, and a local power series does not justify integrating term by term over the entire positive axis. Here we use the principle to derive the Bessel identities; for a discussion of its hypotheses, see [González, Moll, and Schmidt](https://www.math.tulane.edu/~vhm/papers_html/ram-feynman.pdf).

## A single Bessel function

One application is the following Mellin transform:

$$
\begin{equation}\label{ramanujans-master-theorem-part-i-eq-1}
\int_0^\infty x^{\sigma-1} J_\nu (x) \; dx = \frac{2^{\sigma-1}\Gamma\left(\frac{\sigma+\nu}{2}\right)}{\Gamma\left(\frac{2-\sigma+\nu}{2} \right)} \; ,\quad  -\nu < \sigma < \frac{3}{2}
\end{equation}
$$

where $J_\nu (x)$ is the Bessel function of the first kind.

Indeed, $J_\nu(x)$ has the following series expansion around $x=0$:

$$
J_\nu(x) =\sum_{n=0}^\infty \frac{(-1)^n }{n! \Gamma(n+\nu+1)}\left(\frac{x}{2} \right)^{\nu+2n}
$$

Hence, we may apply the RMT to the function $x^{-\nu/2}J_\nu(2\sqrt{x})$ to obtain:

$$
\int_0^\infty x^{s-\nu/2-1} J_\nu(2\sqrt{x}) dx=\frac{\Gamma(s)}{\Gamma(\nu+1-s)}
$$

Now, one can perform the substitutions $x=t^2/4$ and $s=\frac{\sigma+\nu}{2}$ to transform the above integral into the integral of equation $\eqref{ramanujans-master-theorem-part-i-eq-1}$.

It turns out that a similar approach also works for the product $J_\nu (x) J_\mu(x)$. First, we need to compute its series expansion. This can be done by multiplying the individual series expansions and rearranging/grouping certain terms.

$$
\begin{equation}\label{ramanujans-master-theorem-part-i-eq-2}
\begin{aligned}
J_{\nu}(x)J_{\mu}(x) &= \left(\sum_{n=0}^\infty \frac{(-1)^n }{n! \Gamma(n+\nu+1)}\left(\frac{x}{2} \right)^{\nu+2n}\right) \left(\sum_{m=0}^\infty \frac{(-1)^m }{m! \Gamma(m+\nu+1)}\left(\frac{x}{2} \right)^{\nu+2m} \right) \\
&= \sum_{n=0}^\infty \sum_{m=0}^\infty \frac{(-1)^{n+m} x^{\nu+\mu+2(m+n)}}{2^{\nu+\mu+2(m+n)}} \cdot \frac{1}{m! n!\Gamma(n+\nu+1)\Gamma(m+\mu+1)} \\
&= \sum_{r=0}^\infty \frac{(-1)^{r} x^{\nu+\mu+2r}}{2^{\nu+\mu+2r}}\sum\limits_{\substack{0\leq m,n \leq r \\ m+n=r}}\frac{1}{m! n!\Gamma(n+\nu+1)\Gamma(m+\mu+1)} \\
&= \sum_{r=0}^\infty \frac{(-1)^{r} x^{\nu+\mu+2r}}{2^{\nu+\mu+2r} r! \Gamma(r+\nu+1)\Gamma(r+\mu+1)}\sum\limits_{\substack{0\leq m,n \leq r \\ m+n=r}}\binom{r}{m,n} \left(\prod_{i=m+1}^r  (\nu+i)\right) \left(\prod_{j=n+1}^r (\mu+j)\right) \\
&= \sum_{r=0}^\infty \frac{(-1)^{r} x^{\nu+\mu+2r}}{2^{\nu+\mu+2r} r! \Gamma(r+\nu+1)\Gamma(r+\mu+1)}\sum _{n=0}^r\binom{r}{n}(\nu +r)^{\underline{n}}(\mu +r)^{\underline{r-n}} \\
&= \sum_{r=0}^\infty \frac{(-1)^{r} x^{\nu+\mu+2r}}{2^{\nu+\mu+2r} r! \Gamma(r+\nu+1)\Gamma(r+\mu+1)} (\nu +\mu+2r)^{\underline{r}} \\
&= \sum_{r=0}^\infty \frac{(-1)^{r} \Gamma(\nu+\mu+2r+1)}{ r! \Gamma(r+\nu+1)\Gamma(r+\mu+1)\Gamma(\mu+\nu+r+1)} \left( \frac{x}{2}\right)^{\nu+\mu+2r} \quad \; 
\end{aligned}
\end{equation}
$$

To simplify the inner summation, we used the binomial theorem for falling factorials.

Therefore, applying RMT to the function $x^{-\frac{\nu+\mu}{2}}J_{\nu}(2\sqrt{x})J_{\mu}(2\sqrt{x})$, gives us:

$$
\int_0^\infty x^{s-\frac{\nu+\mu}{2}-1} J_{\nu}(2\sqrt{x})J_{\mu}(2\sqrt{x}) \; dx = \frac{\Gamma(s)\Gamma(\nu+\mu+1-2s)}{\Gamma(\nu+1-s)\Gamma(\mu+1-s)\Gamma(\nu+\mu+1-s)}
$$

Finally, make the substitutions $x=t^2/4$ and $s=\frac{\sigma+\nu+\mu}{2}$ in the above integral to get:

$$
\begin{equation}\label{ramanujans-master-theorem-part-i-eq-3}
\boxed{ \int_0^\infty x^{\sigma-1}J_\nu(x)J_\mu(x)\; dx = \frac{2^{\sigma-1} \Gamma\left(\frac{\nu+\mu+\sigma}{2} \right)\Gamma\left(1-\sigma\right)}{\Gamma\left(\frac{\nu-\mu-\sigma}{2} +1\right)\Gamma\left(\frac{\mu-\nu-\sigma}{2} +1\right)\Gamma\left(\frac{\nu+\mu-\sigma}{2} + 1\right)} } \quad \;
\end{equation}
$$

The above equation holds provided that the condition $-(\nu+\mu)< \sigma < 1$ is satisfied.
