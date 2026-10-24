Title: Evaluating very nasty logarithmic integrals: Part III
Date: 2020-09-07 18:58:20 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: evaluating-very-nasty-logarithmic-integrals-part-iii
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: euler-sums, polylogarithm
Summary: The third part uses complex contours to evaluate logarithmic integrals involving inverse trigonometric functions.
Status: published
WordPress_ID: 679

This third part uses complex contours to evaluate logarithmic integrals involving inverse trigonometric functions. We continue the numbering and use results from [part 1]({filename}/posts/evaluating-very-nasty-logarithmic-integrals-part-i.md) and [part 2]({filename}/posts/evaluating-very-nasty-logarithmic-integrals-part-ii.md). The contour diagrams below show the paths used in each argument.

## Integral #5

The first integral that we will evaluate in this post is the following:

$$
I_1 = \int_0^1 \frac{\log^2(x) \arctan(x)}{1+x^2}dx
$$

Of course, one can use brute force methods to find a closed-form antiderivative in terms of polylogarithms. Instead, a more elegant solution is possible by contour integration.

We'll integrate the principal branch of $f(z) = \frac{\arctan(z)}{1+z^2}\left(\text{arctanh}^2(z) + \frac{\pi^2}{16} \right)$ around the following contour:

![Quarter-circle contour in the first quadrant, with indentations at 1 and i]({static}/images/contour.webp)

where

- $\gamma_{3,\epsilon}$ is an arc parameterized by $e^{it}$, where $\arctan\left(\frac{\epsilon \sqrt{4-\epsilon^2}}{2-\epsilon^2} \right)\leq t \leq \frac{\pi}{2} - \arctan\left(\frac{\epsilon \sqrt{4-\epsilon^2}}{2-\epsilon^2} \right)$.
- $\gamma_{2,\epsilon}$ and $\gamma_{4,\epsilon}$ are circular indents of radius $\epsilon$ around the branch points at $z=1$ and $z=i$, respectively.
- $\gamma_{1,\epsilon}$ is a straight line joining $0$ and $1-\epsilon$.
- $\gamma_{5,\epsilon}$ is a straight line joining $(1-\epsilon)i$ and $0$.

Note that $f$ is analytic on $|z| < 1$. It is easy to see that

$$
\begin{aligned}
\lim_{\epsilon\to 0^+} \int_{\gamma_{2,\epsilon}}f(z)\; dz &= 0 \\
\lim_{\epsilon\to 0^+} \int_{\gamma_{4,\epsilon}}f(z)\; dz &= 0
\end{aligned}
$$

On $\gamma_{1,\epsilon}$, we have

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-1}
\begin{aligned}
\lim_{\epsilon\to 0^+} \int_{\gamma_{1,\epsilon}} f(z)\; dz &= \int_0^1\frac{\arctan(x)}{1+x^2}\left(\text{arctanh}^2(x) + \frac{\pi^2}{16} \right)dx \\
&= \int_0^1\frac{\arctan(x) \text{arctanh}^2(x) }{1+x^2}dx +  \frac{\pi^2}{16} \frac{\arctan^2(x)}{2}\Big|_0^1 \\
&= \frac{1}{4}\int_0^1 \frac{\arctan\left(\frac{1-x}{1+x} \right)\log^2(x)}{1+x^2}dx +  \frac{\pi^4}{512} \quad \left(x\mapsto \frac{1-x}{1+x} \right) \\
&= \frac{1}{4}\int_0^1 \frac{\left(\frac{\pi}{4}-\arctan(x) \right)\log^2(x)}{1+x^2}dx +  \frac{\pi^4}{512} \\
&= -\frac{I_1}{4} +\frac{\pi}{16}\int_0^1 \frac{\log^2(x)}{1+x^2}dx +\frac{\pi^4}{512} \\
&= -\frac{I_1}{4} + \frac{3\pi^4}{512}
\end{aligned}
\end{equation}
$$

Here, we used the fact that $\int_0^1 \frac{\log^2(x)}{1+x^2}dx = \frac{\pi^3}{16}$. Similarly, on $\gamma_{5,\epsilon}$ we have

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-2}
\begin{aligned}
\lim_{\epsilon\to 0^+} \int_{\gamma_{5,\epsilon}} f(z) \; dz &= \int_i^0 \frac{\arctan(x)}{1+x^2}\left(\text{arctanh}^2(x) + \frac{\pi^2}{16} \right)dx \\
&= \int_0^1 \frac{\text{arctanh}(x)}{1-x^2}\left(\frac{\pi^2}{16}-\arctan^2(x) \right)dx \quad \left(x\mapsto i x \right) \\
&= \int_0^1\frac{\arctan(x) \text{arctanh}^2(x) }{1+x^2}dx \quad (\text{IBP}) \\
&= -\frac{I_1}{4}+\frac{\pi^4}{256} 
\end{aligned}
\end{equation}
$$

For the integral over $\gamma_{3,\epsilon}$, we will take advantage of the following identities:

$$
\begin{aligned}
\arctan(e^{i\theta}) &= \frac{\pi}{4}+\frac{i}{2} \log\left(\frac{1+\tan \frac{\theta}{2}}{1-\tan \frac{\theta}{2}} \right), \quad 0\leq \theta \leq \frac{\pi}{2} \\
\text{arctanh}(e^{i\theta}) &= -\frac{1}{2}\log \left(\tan\frac{\theta}{2} \right)+\frac{i\pi}{4}, \quad 0\leq \theta \leq \frac{\pi}{2}\\
\end{aligned}
$$

We have

$$
\begin{aligned}
\lim_{\epsilon\to 0^+} \int_{\gamma_{3,\epsilon}}f(z) \; dz &= i \int_0^{\frac{\pi}{2}}f(e^{i\theta}) e^{i\theta} \; d\theta \\
&= \frac{i}{2} \int_0^{\frac{\pi}{2}}\frac{\left( \frac{\pi}{4}+\frac{i}{2} \log\left(\frac{1+\tan \frac{\theta}{2}}{1-\tan \frac{\theta}{2}} \right)\right)\left( -\frac{i\pi}{4}\log \left(\tan\frac{\theta}{2} \right)+\frac{1}{4}\log^2\left(\tan \frac{\theta}{2} \right) \right)}{\cos \theta}d\theta
\end{aligned}
$$

The real part of the above integral is

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-3}
\begin{aligned}
\text{Re}\left[\lim_{\epsilon\to 0^+} \int_{\gamma_{3,\epsilon}}f(z) \; dz \right] &= \int_0^\frac{\pi}{2} \frac{\frac{1}{16}\log^2\left(\tan\frac{\theta}{2} \right)\log\left(\frac{1-\tan \frac{\theta}{2}}{1+\tan \frac{\theta}{2}} \right)+\frac{\pi^2}{32}\log\left(\tan\frac{\theta}{2} \right)}{\cos \theta} d\theta \\
&= \int_0^1 \frac{\frac{1}{8}\log^2\left(u \right)\log\left(\frac{1-u}{1+u} \right)+\frac{\pi^2}{16}\log\left(u \right)}{1-u^2} du \quad \left(u= \tan\frac{\theta}{2} \right) \\
&= -\frac{1}{8} \int_0^1 \frac{\log^2(u)\log\left(\frac{1+u}{1-u}\right)}{1-u^2} + \frac{\pi^2}{16}\left(-\frac{\pi^2}{8} \right) \\
&= \frac{1}{16}\int_0^1 \frac{\log(u) \log^2\left(\frac{1-u}{1+u} \right)}{u}du - \frac{\pi^4}{128} 
\end{aligned}
\end{equation}
$$

Using the results from [part 1]({filename}/posts/evaluating-very-nasty-logarithmic-integrals-part-i.md), we get

$$
\begin{aligned}
\int_0^1 \frac{\log(u)\log^2\left(\frac{1-u}{1+u} \right)}{u}du &= \frac{7}{4}\int_0^1 \frac{\log(u)\log^2(1-u)}{u}du + 2\int_0^1 \frac{\log(u)\log^2(1+u)}{u}du \\
&= \frac{7}{4}\left(2\zeta(4) - 2\sum_{n=1}^\infty \frac{H_n}{n^3} \right)+2\left(2\text{Li}_4(-1)+2\sum_{n=1}^\infty\frac{(-1)^{n+1} H_n}{n^3} \right) \\
&= -\frac{7\pi^4}{144}+4\sum_{n=1}^\infty \frac{(-1)^{n+1}H_n}{n^3}
\end{aligned}
$$

By Cauchy's integral theorem, the sum of $\eqref{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-1}$, $\eqref{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-2}$ and $\eqref{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-3}$ is equal to zero. Therefore,

$$
\begin{aligned}
&\; -\frac{I_1}{2} + \frac{5\pi^4}{512}+\frac{1}{16}\left(-\frac{7\pi^4}{144}+4 \sum_{n=1}^\infty \frac{(-1)^{n+1}H_n}{n^3}\right)-\frac{\pi^4}{128} = 0 \\
&\implies I_1 = -\frac{5\pi^4}{2304}+\frac{1}{2}\sum_{n=1}^\infty (-1)^{n+1}\frac{H_n}{n^3} \\
&\implies I_1 = -\frac{5\pi^4}{2304}+\frac{1}{2}\left(\frac{11\pi^4}{360}+\frac{\pi^2}{12}\log^2(2)-\frac{\log^4(2)}{12} -\frac{7}{4}\log(2)\zeta(3)-2\text{Li}_4\left(\frac{1}{2} \right)\right) \\
&\implies \boxed{I_1 = \frac{151 \pi ^4}{11520}+\frac{\pi ^2}{24}  \log ^2(2)-\frac{\log ^4(2)}{24} -\frac{7}{8} \zeta (3) \log (2)-\text{Li}_4\left(\frac{1}{2}\right)}
\end{aligned}
$$

Refer to [this post]({filename}/posts/an-alternating-euler-sum.md) for the evaluation of $\sum_{n=1}^\infty (-1)^{n+1}\frac{H_n}{n^3}$.

## Integral #6

The next integral that we'll evaluate is

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-4}
I_2 = \int_0^1 \frac{\log^3(x) \arctan(x)}{1+x^2}dx
\end{equation}
$$

Using the transformation $x\mapsto \frac{1}{x}$, we write the integral as:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-5}
\begin{aligned}
I_2 &= -\int_1^\infty\frac{\log^3(x)\left(\frac{\pi}{2}-\arctan(x) \right)}{1+x^2}dx 
\end{aligned}
\end{equation}
$$

Adding up equations $\eqref{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-4}$ and $\eqref{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-5}$ and dividing both sides by 2 gives us:

$$
\begin{aligned}
I_2 &=  -\frac{\pi}{4}\int_1^\infty \frac{\log^3(x)}{1+x^2}dx + \frac{1}{2}\int_0^\infty \frac{\log^3(x) \arctan(x)}{1+x^2}dx\\
&= \frac{\pi}{4}\int_0^1 \frac{\log^3(x)}{1+x^2}dx + \frac{1}{2}\int_0^\infty \frac{\log^3(x) \arctan(x)}{1+x^2}dx
\end{aligned}
$$

Note that

$$
\begin{aligned}
\int_0^1 \frac{\log^3(x)}{1+x^2}dx &= \sum_{n=0}^\infty (-1)^n \int_0^1 x^{2n}\log^3(x) \; dx \\
&= -6\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^4} \\
&= -6\beta(4)
\end{aligned}
$$

So, we have

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-6}
I_2 = - \frac{3\pi}{2}\beta(4) + \frac{1}{2}\int_0^\infty \frac{\log^3(x) \arctan(x)}{1+x^2}dx
\end{equation}
$$

To evaluate the integral in the above equation, we will use the Feynman technique. Define the function $F:[0,\infty) \to \mathbb{R}$ as
$F(s) = \int_0^\infty \frac{\log^3(x)\arctan(s x)}{1+x^2}dx$. Now, we have

$$
F'(s) = \int_0^\infty \frac{x \log^3(x)}{(1+x^2)(1+s^2 x^2)}dx
$$

Before evaluating $F'(s)$, we will evaluate the simpler integral $\int_0^\infty \frac{x \log(x)}{(1+x^2)(1+s^2 x^2)}dx$. To do this, integrate the principal branch of $g(z) = \frac{z\log^2(-z)}{(1+z^2)(1+s^2 z^2)}$ around the following "key hole" contour:

![Indented contour used for the second logarithmic integral]({static}/images/contour1.webp)

where:

- $\gamma_{1,\epsilon, R}$ is a line joining the points $\sqrt{R^2-\epsilon^2}-i\epsilon$ and $-i\epsilon$.
- $\gamma_{2,\epsilon, R}$ is a line joining the points $i\epsilon$ and $\sqrt{R^2-\epsilon^2}+i\epsilon$.
- $\gamma_{3,\epsilon}$ is parameterized by $\epsilon e^{-i t}$ where $\frac{\pi}{2} \leq t \leq \frac{3\pi}{2}$.
- $\gamma_{4,R}$ is parameterized by $R e^{i t}$ where $\arctan\left(\frac{\epsilon}{\sqrt{R^2-\epsilon^2}} \right) \leq t \leq 2\pi - \arctan\left(\frac{\epsilon}{\sqrt{R^2-\epsilon^2}} \right)$.

As $\epsilon\to 0^+$ and $R\to \infty$, the integrals along $\gamma_{3,\epsilon}$ and $\gamma_{4,R}$ tend to 0. Therefore, we are only left with the integrals above and below the branch cut. The residues of $g(z)$ at it's poles is given by:

$$
\begin{aligned}
\mathop{\text{Res}}\limits_{z=i} \; g(z) &= -\frac{\pi^2}{8(1-s^2)} \\
\mathop{\text{Res}}\limits_{z=-i} \; g(z) &= -\frac{\pi^2}{8(1-s^2)} \\
\mathop{\text{Res}}\limits_{z=i/s} \; g(z) &= -\frac{\left(\log(s)+\frac{i\pi}{2} \right)^2}{2(1-s^2)} \\
\mathop{\text{Res}}\limits_{z=-i/s} \; g(z) &= -\frac{\left(\log(s)-\frac{i\pi}{2} \right)^2}{2(1-s^2)}
\end{aligned}
$$

Now, the residue theorem gives us:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-7}
\begin{aligned}
\int_0^\infty \frac{x\left((\log (x)-i\pi)^2 - (\log (x)+i\pi)^2 \right)}{(1+x^2)(1+s^2 x^2)}dx &= 2i\pi \Big(\mathop{\text{Res}}\limits_{z=i} \; g(z)+ \mathop{\text{Res}}\limits_{z=-i}\; g(z) + \mathop{\text{Res}}\limits_{z=i/s}\; g(z) \\ &\quad + \mathop{\text{Res}}\limits_{z=-i/s}\; g(z) \Big) \\
\implies -4i\pi \int_0^\infty \frac{x\log(x)}{(1+x^2)(1+s^2 x^2)}dx &= -2i\pi \frac{\log^2(s)}{1-s^2} \\
\implies \int_0^\infty \frac{x\log(x)}{(1+x^2)(1+s^2 x^2)}dx &= \frac{\log^2(s)}{2(1-s^2)} 
\end{aligned}
\end{equation}
$$

To evaluate $F'(s)$, we integrate the principal branch of $h(z) = \frac{z \log^4(-z)}{(1+z^2)(1+s^2 z^2)}$ around the same contour. This time, the residues are:

$$
\begin{aligned}
\mathop{\text{Res}}\limits_{z=i} \; h(z) &= \frac{\pi^4}{32(1-s^2)} \\
\mathop{\text{Res}}\limits_{z=-i} \; h(z) &= \frac{\pi^4}{32(1-s^2)} \\
\mathop{\text{Res}}\limits_{z=i/s} \; h(z) &= -\frac{\left(\log(s)+\frac{i\pi}{2} \right)^4}{2(1-s^2)} \\
\mathop{\text{Res}}\limits_{z=-i/s} \; h(z) &= -\frac{\left(\log(s)-\frac{i\pi}{2} \right)^4}{2(1-s^2)}
\end{aligned}
$$

The residue theorem gives us:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-8}
\begin{aligned}
\int_0^\infty \frac{x\left((\log (x)-i\pi)^4 - (\log (x)+i\pi)^4 \right)}{(1+x^2)(1+s^2 x^2)}dx &= 2i\pi \Big(\mathop{\text{Res}}\limits_{z=i} \; h(z)+ \mathop{\text{Res}}\limits_{z=-i}\; h(z) + \mathop{\text{Res}}\limits_{z=i/s}\; h(z) \\ &\quad + \mathop{\text{Res}}\limits_{z=-i/s}\; h(z) \Big) \\
\implies -8i\pi \int_0^\infty \frac{x\left(\log^3(x) -\pi^2 \log(x) \right)}{(1+x^2)(1+s^2 x^2)}dx &= 2i\pi \frac{\frac{3\pi^2}{2}\log^2(s)-\log^4(s)}{1-s^2} \\
\implies \int_0^\infty \frac{x\log^3(x)}{(1+x^2)(1+s^2 x^2)}dx &= \frac{\pi^2\log^2(s)+2\log^4(s)}{8(1-s^2)} 
\end{aligned}
\end{equation}
$$

Note that we used equation $\eqref{evaluating-very-nasty-logarithmic-integrals-part-iii-eq-7}$ to the get the above result. We can now calculate our original integral as follows:

$$
\begin{aligned}
I_2 &= -\frac{3\pi}{2}\beta(4) + \frac{1}{2}\int_0^1 F'(s) ds \\
&= -\frac{3\pi}{2}\beta(4) + \frac{1}{2}\int_0^1 \frac{\pi^2\log^2(s)+2\log^4(s)}{8(1-s^2)} ds \\
&= -\frac{3\pi}{2}\beta(4) + \frac{\pi^2}{16}\int_0^1\frac{\log^2(s)}{1-s^2}ds+\frac{1}{8}\int_0^1 \frac{\log^4(s)}{1-s^2} ds \\
&= -\frac{3\pi}{2}\beta(4) + \frac{\pi^2}{16}\sum_{k=0}^\infty\int_0^1 s^{2k}\log^2(s)ds+\frac{1}{8}\sum_{k=0}^\infty\int_0^1 s^{2k}\log^4(s) ds \\
&= -\frac{3\pi}{2}\beta(4) + \frac{\pi^2}{8}\sum_{k=0}^\infty\frac{1}{(2k+1)^3}+3\sum_{k=0}^\infty\frac{1}{(2k+1)^5} \\
&= \boxed{-\frac{3\pi}{2}\beta(4) + \frac{7\pi^2}{64}\zeta(3) +\frac{93}{32}\zeta(5)}
\end{aligned}
$$

Interestingly, $I_2$ can be reduced into an Euler sum which can be evaluated using contour integration.
