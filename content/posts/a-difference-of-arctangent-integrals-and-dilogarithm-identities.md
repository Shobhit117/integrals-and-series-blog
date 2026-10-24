Title: A difference of arctangent integrals and dilogarithm identities
Date: 2026-10-24 10:11 +0530
Slug: a-difference-of-arctangent-integrals-and-dilogarithm-identities
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: logarithmic-integrals, polylogarithm, fourier-series, trigonometric-integrals
Summary: Poisson-kernel series expansions and two-variable dilogarithm relations evaluate a difference of arctangent integrals.
Status: published

In this post we use Poisson-kernel Fourier series and two-variable dilogarithm identities to prove the identity

$$
\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} \arctan\left(\sqrt{3}\tan\theta\right)\,d\theta - \int_{0}^{\frac{\pi}{6}} \arctan\left(\sqrt{3}\tan\theta\right)\,d\theta = \frac{\pi^2}{12},
$$

and then derive an additional dilogarithm relation at $\rho = 2-\sqrt{3}$ from Hill's two-variable functional equation.

## Expanding a parameterized integral in a Fourier series

Let $I$ denote the expression on the left-hand side. The substitution $\sqrt{3}\tan \theta = \tan \varphi$ (so $\sqrt{3}\sec^2\theta\,d\theta = \sec^2\varphi\,d\varphi$, which simplifies to $d\theta = \frac{\sqrt{3}}{2}\frac{d\varphi}{1+\frac{1}{2}\cos(2\varphi)}$) transforms $I$ into

$$
I = \frac{\sqrt{3}}{2}\left( \int_{\frac{\pi}{3}}^{\frac{\pi}{2}}\frac{\varphi}{1+\frac{1}{2}\cos(2\varphi)}\,d\varphi - \int_{0}^{\frac{\pi}{4}}\frac{\varphi}{1+\frac{1}{2}\cos(2\varphi)}\,d\varphi \right).
$$

For $0 \leq \phi \leq \frac{\pi}{2}$, consider the generalized integral

$$
I(\phi) = \frac{\sqrt{3}}{2}\int_{0}^{\phi}\frac{\varphi}{1+\frac{1}{2}\cos(2\varphi)}\,d\varphi.
$$

Using the Poisson kernel identity

$$
1+2\sum_{k=1}^\infty x^k \cos(k\theta) = \frac{1-x^2}{1-2x\cos(\theta) + x^2}, \qquad |x|<1,
$$

with $x = -\rho$, where $\rho = 2-\sqrt{3} = \tan\left(\frac{\pi}{12}\right)$ satisfies $\frac{2\rho}{1+\rho^2} = \frac{1}{2}$ and $\frac{1-\rho^2}{1+\rho^2} = \frac{\sqrt{3}}{2}$, we deduce that

$$
\frac{1}{1+\frac{1}{2}\cos(2\varphi)} = \frac{2}{\sqrt{3}}\left(1+2\sum_{k=1}^\infty (-1)^k \rho^k \cos(2k\varphi) \right).
$$

Integrating term by term on $[0, \phi]$ using integration by parts gives

$$
\begin{aligned}
I(\phi) &= \int_0^\phi \varphi \left( 1+2\sum_{k=1}^\infty (-1)^k \rho^k \cos(2k\varphi) \right)d\varphi \\
&= \frac{\phi^2}{2} + 2\sum_{k=1}^\infty (-1)^k \rho^k \int_0^\phi \varphi \cos(2k\varphi)\,d\varphi \\
&= \frac{\phi^2}{2} + 2\sum_{k=1}^\infty (-1)^k \rho^k \left[\frac{\phi \sin(2k\phi)}{2k}-\frac{1-\cos(2k\phi)}{4k^2} \right] \\
&= \frac{\phi^2}{2} - \phi \sum_{k=1}^\infty (-1)^{k+1}\frac{\rho^k\sin(2k\phi)}{k} + \frac{1}{2}\sum_{k=1}^\infty (-1)^{k+1} \frac{1-\cos(2k\phi)}{k^2}\rho^k \\
&= \frac{\phi^2}{2} - \phi \arctan\left(\frac{\rho \sin(2\phi)}{1+\rho\cos(2\phi)} \right) + \frac{1}{2}\sum_{k=1}^\infty (-1)^{k+1} \frac{1-\cos(2k\phi)}{k^2}\rho^k,
\end{aligned} \tag{1}
$$

where the last step uses the Fourier sine series

$$
\sum_{k=1}^\infty (-1)^{k+1}\frac{x^k}{k}\sin(k\theta) = \arctan\left(\frac{x \sin(\theta)}{1+x\cos(\theta)}\right), \qquad |x| \leq 1.
$$

## Evaluating $I(\phi)$ at $\frac{\pi}{2}$, $\frac{\pi}{3}$, and $\frac{\pi}{4}$

Recall the dilogarithm $\operatorname{Li}_2(z) = \sum_{k=1}^\infty \frac{z^k}{k^2}$ and Legendre's chi function

$$
\chi_2(z) = \sum_{k=0}^\infty \frac{z^{2k+1}}{(2k+1)^2} = \frac{1}{2}\bigl(\operatorname{Li}_2(z) - \operatorname{Li}_2(-z)\bigr) = \operatorname{Li}_2(z) - \frac{1}{4}\operatorname{Li}_2(z^2),
$$

where the last equality follows from the duplication identity $\operatorname{Li}_2(z) + \operatorname{Li}_2(-z) = \frac{1}{2}\operatorname{Li}_2(z^2)$. Using $\rho = 2-\sqrt{3} = \tan\left(\frac{\pi}{12}\right)$, we evaluate equation (1) at our three angles:

- At $\phi = \frac{\pi}{2}$: $\sin(\pi) = 0$ and $1-\cos(k\pi)$ is $2$ for odd $k$ and $0$ for even $k$, so

$$
I\left(\frac{\pi}{2}\right) = \frac{\pi^2}{8}+\chi_2(\rho). \tag{2}
$$

- At $\phi = \frac{\pi}{3}$: $\frac{\rho\sin(2\pi/3)}{1+\rho\cos(2\pi/3)} = \frac{(2-\sqrt{3})\frac{\sqrt{3}}{2}}{1 - \frac{2-\sqrt{3}}{2}} = 2-\sqrt{3} = \tan\left(\frac{\pi}{12}\right)$, so the arctangent equals $\frac{\pi}{12}$ and $\frac{\phi^2}{2} - \phi\frac{\pi}{12} = \frac{\pi^2}{36}$. For the cosine sum, $1-\cos\left(\frac{2k\pi}{3}\right)$ equals $\frac{3}{2}$ when $3 \nmid k$ and $0$ when $3 \mid k$, giving

$$
I\left(\frac{\pi}{3}\right) = \frac{\pi^2}{36}+\frac{1}{12}\operatorname{Li}_2\left(-\rho^3\right) -\frac{3}{4}\operatorname{Li}_2(-\rho). \tag{3}
$$

- At $\phi = \frac{\pi}{4}$: $\frac{\rho\sin(\pi/2)}{1+\rho\cos(\pi/2)} = \rho = \tan\left(\frac{\pi}{12}\right)$, so $\frac{\phi^2}{2} - \phi\frac{\pi}{12} = \frac{\pi^2}{96}$, while separating odd and even $k$ in $1-\cos\left(\frac{k\pi}{2}\right)$ gives

$$
I\left(\frac{\pi}{4}\right) = \frac{\pi^2}{96}+\frac{1}{2}\chi_2(\rho)-\frac{1}{4}\chi_2\left(\rho^2\right). \tag{4}
$$

Expanding $\chi_2$ and $\operatorname{Li}_2(-z)$ in terms of $\operatorname{Li}_2$ at positive powers of $\rho$ via $\operatorname{Li}_2(-z) = \frac{1}{2}\operatorname{Li}_2(z^2) - \operatorname{Li}_2(z)$, we obtain

$$
\begin{aligned}
I &= I\left(\frac{\pi}{2}\right)-I\left(\frac{\pi}{3}\right)-I\left(\frac{\pi}{4}\right) \\
&= \frac{25\pi^2}{288} + \left[-\frac{1}{4}\operatorname{Li}_2(\rho)+\frac{1}{2}\operatorname{Li}_2(\rho^2)+\frac{1}{12}\operatorname{Li}_2(\rho^3)-\frac{1}{16}\operatorname{Li}_2(\rho^4)-\frac{1}{24}\operatorname{Li}_2(\rho^6) \right].
\end{aligned} \tag{5}
$$

## Completing the proof with dilogarithm identities

To show that $I = \frac{\pi^2}{12}$, it remains to prove that

$$
-\frac{1}{4}\operatorname{Li}_2(\rho)+\frac{1}{2}\operatorname{Li}_2(\rho^2)+\frac{1}{12}\operatorname{Li}_2(\rho^3)-\frac{1}{16}\operatorname{Li}_2(\rho^4)-\frac{1}{24}\operatorname{Li}_2(\rho^6) = -\frac{\pi^2}{288}. \tag{6}
$$

Let $\operatorname{Li}_2(x,\theta) = \operatorname{Re}\operatorname{Li}_2(xe^{i\theta})$. We use two classic identities from Lewin's *Polylogarithms and Associated Functions*:

$$
\begin{aligned}
\operatorname{Li}_2 \left(\tan a, \frac{\pi}{2}-2a \right) &= a^2 +\frac{3}{4}\operatorname{Li}_2(\tan^2 a) -\frac{1}{8}\operatorname{Li}_2(\tan^4 a), \\
\operatorname{Li}_2\left(x,\frac{\pi}{3}\right) &= \frac{1}{6} \operatorname{Li}_2(-x^3) -\frac{1}{2}\operatorname{Li}_2(-x).
\end{aligned}
$$

Setting $a = \frac{\pi}{12}$ and $x = \tan\left(\frac{\pi}{12}\right) = \rho$ makes the left-hand sides of both identities equal to $\operatorname{Li}_2\left(\rho, \frac{\pi}{3}\right)$. Equating their right-hand sides and expanding $\operatorname{Li}_2(-\rho)$ and $\operatorname{Li}_2(-\rho^3)$ via the duplication formula gives

$$
\begin{aligned}
\frac{1}{6}\operatorname{Li}_2(-\rho^3)-\frac{1}{2}\operatorname{Li}_2(-\rho) &= \frac{\pi^2}{144} + \frac{3}{4}\operatorname{Li}_2(\rho^2)-\frac{1}{8}\operatorname{Li}_2(\rho^4) \\
\implies \frac{1}{12}\operatorname{Li}_2(\rho^6)-\frac{1}{6}\operatorname{Li}_2(\rho^3) -\frac{1}{4}\operatorname{Li}_2(\rho^2) +\frac{1}{2} \operatorname{Li}_2(\rho) &= \frac{\pi^2}{144} + \frac{3}{4}\operatorname{Li}_2(\rho^2)-\frac{1}{8}\operatorname{Li}_2(\rho^4).
\end{aligned} \tag{7}
$$

Dividing equation (7) by $-2$ and rearranging terms immediately produces equation (6), completing the proof that $I = \frac{\pi^2}{12}$.

## Bonus: An identity from Hill's two-variable relation

Another attractive dilogarithm identity at $\rho = 2-\sqrt{3}$ follows from Hill's two-variable relation:

$$
\operatorname{Li}_2(xy) = \operatorname{Li}_2(x) + \operatorname{Li}_2(y) + \operatorname{Li}_2\left(-x\left(\frac{1-y}{1-x}\right) \right)+\operatorname{Li}_2\left(-y\left(\frac{1-x}{1-y}\right)\right)+\frac{1}{2}\log^2\left(\frac{1-x}{1-y}\right).
$$

Substitute $x = -y = e^{-i\frac{\pi}{4}}\frac{\sqrt{3}-1}{\sqrt{2}}$. Then $\frac{1-x}{1+x} = ix = e^{i\frac{\pi}{4}}\frac{\sqrt{3}-1}{\sqrt{2}}$ and $ix^2 = \rho$, so

$$
\begin{aligned}
\operatorname{Li}_2(-x^2) &= \operatorname{Li}_2(x) + \operatorname{Li}_2(-x) + \operatorname{Li}_2(i)+\operatorname{Li}_2(ix^2)+\frac{1}{2}\log^2(ix) \\
\implies \operatorname{Li}_2(i\rho) &= \frac{1}{2}\operatorname{Li}_2(-i\rho)+ \operatorname{Li}_2(i) + \operatorname{Li}_2(\rho) +\frac{1}{2}\log^2\left(e^{i\frac{\pi}{4}}\frac{\sqrt{3}-1}{\sqrt{2}} \right).
\end{aligned}
$$

Using $\operatorname{Re}\operatorname{Li}_2(\pm i\rho) = \frac{1}{4}\operatorname{Li}_2(-\rho^2) = \frac{1}{8}\operatorname{Li}_2(\rho^4) - \frac{1}{4}\operatorname{Li}_2(\rho^2)$, $\operatorname{Re}\operatorname{Li}_2(i) = -\frac{\pi^2}{48}$, and $\frac{\sqrt{3}-1}{\sqrt{2}} = \sqrt{\rho}$, extracting the real part of the above equation yields

$$
\frac{\operatorname{Li}_2(\rho^4)}{16}-\frac{\operatorname{Li}_2(\rho^2)}{8} -\operatorname{Li}_2(\rho) = -\frac{5\pi^2}{96}+\frac{1}{8}\log^2(\rho).
$$

