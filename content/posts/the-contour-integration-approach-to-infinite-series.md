Title: A contour integration approach to infinite series
Date: 2020-07-14 20:12:16 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: the-contour-integration-approach-to-infinite-series
Author: Shobhit Bhatnagar
Category: Uncategorized
Tags: 
Summary: A contour-integral approach to an infinite trigonometric series, with an application of equidistribution.
Status: published
WordPress_ID: 398

We will evaluate the trigonometric series $\sum_{n=0}^\infty \frac{\cot\left(\frac{2n+1}{2}\pi\sqrt{2} \right)}{(2n+1)^3}$ by integrating a meromorphic function around a sequence of expanding squares. The residues encode the desired sum, while equidistribution helps us choose a useful subsequence of contours. Define the meromorphic function

$$
f(z) = \frac{\pi \tan(\pi z)\tan(\pi z \theta)}{z^3}
$$

where the parameter $\theta$ is a positive irrational number. Let $C_N$ denote the positively oriented square with vertices $(N+1)(1+i),\; (N+1)(-1+i),\; (N+1)(-1-i)$ and $(N+1)(1-i)$. The irrationality of $\theta$ ensures that no pole on the real axis lies on the boundary of this square.

### Estimating the contour integral

Put $m=N+1$. We will estimate the horizontal and vertical sides separately. We use the elementary identities

$$
|\tan(u+iv)|^2
=\frac{\sin^2u+\sinh^2v}{\cos^2u+\sinh^2v}
$$

and, whenever $\tan u$ is finite,

$$
|\tan(u+iv)|^2
=\frac{\tan^2u+\tanh^2v}
{1+\tan^2u\,\tanh^2v}.
$$

The first identity, including its limiting cases when $\cos u=0$, shows that for $v\neq0$,

$$
\tanh|v|\leq|\tan(u+iv)|\leq\coth|v|,
$$

and, if $u$ is fixed while $v$ varies,

$$
|\tan(u+iv)|\leq\max\{1,|\tan u|\}.
$$

For the second bound, put $a=\tan^2u$ and $s=\tanh^2v$. Then the square of the modulus is $(a+s)/(1+as)$, which lies between $a$ and $1$ as $s$ ranges from $0$ to $1$. This proves the claimed estimate.

On either horizontal side, write $z=x\pm im$ with $-m\leq x\leq m$. Since $|z|\geq m$, we have

$$
|\tan(\pi z)|\leq\coth(\pi m),
\qquad
|\tan(\pi\theta z)|\leq\coth(\pi\theta m).
$$

The combined length of the two horizontal sides is $4m$. Therefore,

$$
\int_{\text{horizontal sides}}|f(z)|\,|dz|
\leq
\frac{4\pi}{m^2}\coth(\pi m)\coth(\pi\theta m).
$$

On either vertical side, write $z=\pm m+iy$ with $-m\leq y\leq m$. Because $m$ is an integer,

$$
|\tan(\pi z)|=|\tan(\pm m\pi+i\pi y)|
=|\tanh(\pi y)|\leq1.
$$

Set

$$
T_m:=|\tan(\pi m\theta)|.
$$

The second consequence of the tangent identity gives

$$
|\tan(\pi\theta(\pm m+iy))|
\leq\max\{1,T_m\}.
$$

Again $|z|\geq m$, and the two vertical sides have combined length $4m$, so

$$
\int_{\text{vertical sides}}|f(z)|\,|dz|
\leq\frac{4\pi}{m^2}\max\{1,T_m\}.
$$

Combining the four sides yields the explicit estimate

$$
\begin{aligned}
\left|\int_{C_N} f(z)\,dz\right|
&\leq\int_{C_N}|f(z)|\,|dz|\\
&\leq\frac{4\pi}{m^2}
\left(
\max\{1,T_m\}
+\coth(\pi m)\coth(\pi\theta m)
\right).
\end{aligned}
$$

### Choosing the contours by equidistribution

It remains to keep $T_m$ away from the poles of the tangent. By [Weyl's equidistribution theorem]({filename}/posts/weyls-equidistribution-theorem.md), the fractional parts $\{m\theta\}$ are equidistributed in $[0,1)$. In particular,

$$
\lim_{M\to\infty}
\frac{1}{M}
\#\left\{1\leq m\leq M:\{m\theta\}\in
\left[0,\frac14\right]\right\}
=\frac14.
$$

Thus there are infinitely many integers $m$ for which $\{m\theta\}\in[0,1/4]$. Enumerate them as an increasing sequence $m_1<m_2<\cdots$. Since tangent has period $\pi$,

$$
T_{m_k}
=|\tan(\pi\{m_k\theta\})|
\leq1.
$$

Let $N_k=m_k-1$. Substituting this bound into the contour estimate gives

$$
\left|\int_{C_{N_k}}f(z)\,dz\right|
\leq\frac{4\pi}{m_k^2}
\left(1+\coth(\pi m_k)\coth(\pi\theta m_k)\right).
$$

Because $m_k\to\infty$ and both hyperbolic cotangents tend to $1$, the expression on the right is asymptotic to $8\pi/m_k^2$. Hence

$$
\lim_{k\to \infty}\int_{C_{N_k}} f(z)\; dz = 0.
$$

On the other hand, the residue theorem gives

$$
\frac{1}{2\pi i}\int_{C_{N_k}} f(z)\,dz
= \substack{\displaystyle \operatorname{Res} \\ z=0}f(z)
+ \sum_{|i+\frac12|<m_k}
\substack{\displaystyle \operatorname{Res} \\ z=\frac{2i+1}{2}}f(z)
+ \sum_{|j+\frac12|<\theta m_k}
\substack{\displaystyle \operatorname{Res} \\ z=\frac{2j+1}{2\theta}}f(z).
$$

A simple calculation gives the following residues:

$$
\begin{aligned}
\substack{\displaystyle \text{Res} \\ z=0}f(z) &= \pi^3 \theta \\
\substack{\displaystyle \text{Res} \\ z=\frac{2n+1}{2}}f(z)  &= -8\frac{\tan\left(\frac{\pi \theta}{2}(2n+1) \right)}{(2n+1)^3}, \quad n\in \{0,1,2,\cdots\}\\
\substack{\displaystyle \text{Res} \\ z=\frac{2n+1}{2\theta}}f(z)  &= -8\theta^2 \frac{\tan\left(\frac{\pi}{2\theta}(2n+1) \right)}{(2n+1)^3} , \quad n\in \{0,1,2,\cdots\}
\end{aligned}
$$

The nonzero poles occur in pairs $z$ and $-z$, and the two residues in each pair are equal. Letting $k\to\infty$ in the residue identity therefore gives the following relation, provided the two series converge:

$$
\sum_{n=0}^\infty \frac{\tan\left(\frac{\pi \theta}{2}(2n+1) \right)}{(2n+1)^3} + \theta^2 \sum_{n=0}^\infty \frac{\tan\left(\frac{\pi}{2\theta}(2n+1) \right)}{(2n+1)^3} = \frac{\pi^3 \theta}{16}
$$

Equidistribution was used only to choose contours on which the boundary integral is small; by itself it does not guarantee convergence of the two series. For the value needed here, $\theta=\sqrt2+1$, convergence presents no problem. A quadratic irrational is badly approximable, so there is a constant $c>0$ such that

$$
|q\theta-p|\geq\frac{c}{q}
$$

for all integers $p$ and positive integers $q$. The same is true of $1/\theta=\sqrt2-1$. Consequently, the tangent factors in the two series are $O(2n+1)$, even when their arguments approach a pole. After division by $(2n+1)^3$, the summands are $O((2n+1)^{-2})$, and both series converge absolutely.

Finally, substitute $\theta=\sqrt2+1$. Since $2n+1$ is odd and $1/\theta=\sqrt2-1$, periodicity gives

$$
\tan\left(\frac{\pi\theta}{2}(2n+1)\right)
=\tan\left(\frac{\pi}{2\theta}(2n+1)\right)
=-\cot\left(\frac{\pi\sqrt2}{2}(2n+1)\right).
$$

Moreover,

$$
\frac{\theta}{1+\theta^2}
=\frac{1}{\theta+\theta^{-1}}
=\frac{1}{2\sqrt2}.
$$

The relation above therefore reduces to

$$
\boxed{\sum_{n=0}^\infty \frac{\cot\left(\frac{2n+1}{2}\pi\sqrt{2} \right)}{(2n+1)^3} = -\frac{\pi^3}{32\sqrt{2}}}
$$
