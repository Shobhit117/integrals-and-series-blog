Title: Evaluating very nasty logarithmic integrals: Part II
Date: 2020-08-06 10:27:24 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: evaluating-very-nasty-logarithmic-integrals-part-ii
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: logarithmic-integrals, euler-sums, polylogarithm
Summary: The second part develops further logarithmic integral evaluations through polylogarithmic identities.
Status: published
WordPress_ID: 532

We continue the evaluations from [part 1]({filename}/posts/evaluating-very-nasty-logarithmic-integrals-part-i.md), keeping the integral numbering from that post. Here the resulting Euler sums lead us toward polylogarithmic identities rather than a direct residue calculation.

## Integral #3

We'll start by finding a closed form for the integral:

$$
I_1 = \int_0^1 \frac{\log^2(1+x^2)}{1+x^2}dx
$$

This integral can be reduced to Euler sums like our previous problem. But this time, the resulting Euler sums cannot be evaluated using the method of residues. Therefore, we'll have to use a different approach.

Let us first consider the following integral:

$$
I_2 = \int_0^1 \frac{\log^2(1+ix)}{1+x^2}dx
$$

Throughout this post, $\log$ denotes the principal branch of the logarithmic function defined by $\log z = \log|z| + i\text{arg}(z)$, with $-\pi < |\text{arg}(z)| \leq \pi$. We have

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-1}
\begin{aligned}
I_2 &= \frac{1}{2}\int_0^1\log^2(1+ix)\left(\frac{1}{1+ix}+\frac{1}{1-ix} \right)dx \\
&= \frac{\log^3(1+ix)}{6i}\Big|_0^1 + \frac{1}{2}\int_0^1 \frac{\log^2(1+ix)}{1-ix}dx \\
&= \frac{\log^3(1+i)}{6i} + \frac{i}{2}\int_{\frac{1}{2}}^{\frac{1-i}{2}}\frac{\log^2(2(1-x))}{x}dx \\
&= \frac{\log^3(1+i)}{6i} + \frac{i}{2}\int_{\frac{1}{2}}^{\frac{1-i}{2}}\frac{\log^2(1-x)+\log^2(2)+2\log(2)\log(1-x)}{x}dx \\
&= \frac{\log^3(1+i)}{6i}  + \frac{i\log^2(2)\log\left(1-i\right)}{2} + i\log(2) \left[\text{Li}_2\left(\frac{1}{2}\right)-\text{Li}_2\left(\frac{1-i}{2}\right) \right]  \\ &\quad + \frac{i}{2}\int_{\frac{1}{2}}^{\frac{1-i}{2}}\frac{\log^2(1-x)}{x}dx 
\end{aligned}
\end{equation}
$$

We can use [equation (2)]({filename}/posts/euler-sums-involving-square-of-harmonic-numbers.md) to evaluate $\int_{\frac{1}{2}}^{\frac{1+i}{2}}\frac{\log^2(1-x)}{x}dx$.

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-2}
\begin{aligned}
\int_{\frac{1}{2}}^{\frac{1-i}{2}}\frac{\log^2(1-x)}{x}dx &= \log^2\left( \frac{1+i}{2}\right)\log\left(\frac{1-i}{2}\right) + 2\log\left(\frac{1+i}{2} \right)\text{Li}_2\left(\frac{1+i}{2}\right) \\ &\quad -2\text{Li}_3\left(\frac{1+i}{2}\right) + \log^3(2) + 2\log(2)\text{Li}_2\left(\frac{1}{2}\right) + 2\text{Li}_3\left(\frac{1}{2} \right) 
\end{aligned}
\end{equation}
$$

To simplify $\text{Li}_2\left(\frac{1+i}{2} \right)$ and $\text{Li}_2\left(\frac{1-i}{2} \right)$, we can use the following Dilogarithm identity:

$$
\text{Li}_2(1-z) + \text{Li}_2\left(1-z^{-1} \right) = -\frac{1}{2}\log^2(z)
$$

This is easy to verify by differentiating both sides of the above equation with respect to $z$. Plugging in $z=\frac{1+i}{2}$ gives

$$
\begin{aligned}
\text{Li}_2\left(\frac{1-i}{2}\right) &= -\text{Li}_2(i) - \frac{1}{2}\log^2\left(\frac{1+i}{2}\right) = \frac{5\pi^2}{96}-\frac{\log^2(2)}{8}+i\left(-G + \frac{\pi}{8}\log(2)\right) \\
\text{Li}_2\left(\frac{1+i}{2}\right) &= \overline{\text{Li}_2\left(\frac{1-i}{2}\right)} = \frac{5\pi^2}{96}-\frac{\log^2(2)}{8}-i\left(-G + \frac{\pi}{8}\log(2)\right)
\end{aligned}
$$

Now, we have everything needed to simplify equation $\eqref{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-1}$. This is a cumbersome task so I will only present the final result:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-3}
\begin{aligned}
I_2 &= -\frac{3\pi^3}{128}- \frac{G \log(2) }{2} + \frac{7\pi \log^2(2)}{32} + i\Bigg( -\frac{ G \pi }{4} + \frac{7\pi^2 \log(2)}{192} + \frac{\log^3(2)}{48}+\frac{7}{8}\zeta(3) \\ &\quad - \text{Li}_3\left(\frac{1+i}{2} \right)\Bigg) 
\end{aligned}
\end{equation}
$$

To the best of my knowledge, $\text{Li}_3\left(\frac{1+i}{2} \right)$ can not be simplified further. So, we'll leave it as it is. We can now extract $I_1$ from the real part of $I_2$.

$$
\begin{aligned}
\text{Re }I_2 &= \int_0^1 \frac{\frac{1}{4}\log^2(1+x^2) - \arctan^2(x)}{1+x^2}dx \\
&= \frac{1}{4}\int_0^1 \frac{\log^2(1+x^2)}{1+x^2}dx - \frac{\arctan^3(x)}{3}\Big|_0^1 \\
&= \frac{1}{4}I_1 - \frac{\pi^3}{192}
\end{aligned}
$$

Therefore,

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-4}
\boxed{I_1 = -2G\log(2) - \frac{7\pi^3}{96} + \frac{7\pi \log^2(2)}{8} + 4\text{ Im }\text{Li}_3\left(\frac{1+i}{2} \right)}
\end{equation}
$$

Now, let's turn our attention to another integral:

$$
I_3 = \int_0^1 \frac{\log(x)\log(1+x^2)}{1+x^2}dx
$$

Notice that with the help of some algebra, we can write:

$$
I_3 = -\frac{1}{2}\int_0^1 \frac{\log^2\left(\frac{x}{1+x^2} \right)}{1+x^2}dx + \frac{1}{2}\int_0^1 \frac{\log^2(1+x^2)}{1+x^2}dx + \frac{1}{2}\int_0^1 \frac{\log^2(x)}{1+x^2}dx
$$

The leftmost integral can be dealt with the trigonometric substitution $x=\tan \theta$:

$$
\begin{aligned}
\int_0^1 \frac{\log^2\left(\frac{x}{1+x^2} \right)}{1+x^2}dx &= \int_0^{\frac{\pi}{4}} \log^2\left(\sin \theta \cos\theta \right) \; d\theta \\
&= \int_0^{\frac{\pi}{4}} \log^2\left(\frac{\sin(2\theta)}{2} \right)\; d\theta \\
&= \frac{1}{2}\int_0^{\frac{\pi}{2}}\log^2\left(\frac{\sin \theta}{2} \right)\; d\theta \\
&= \frac{1}{2}\lim_{s\to 1}\frac{d^2}{ds^2}\int_0^{\frac{\pi}{2}}\left(\frac{\sin\theta}{2} \right)^{s-1}d\theta \\
&= \frac{1}{2}\lim_{s\to 1}\frac{d^2}{ds^2}\left[\frac{2^{-s}\sqrt{\pi}\Gamma\left(\frac{s}{2}\right)}{\Gamma\left(\frac{1+s}{2} \right)} \right] \\
&= \frac{\pi^3}{48}+ \pi \log^2(2)
\end{aligned}
$$

The middle integral has already been evaluated. As for the rightmost integral, we have:

$$
\begin{aligned}
\int_0^1 \frac{\log^2(x)}{1+x^2}dx &= \sum_{n=0}^\infty (-1)^{n}\int_0^1 x^{2n}\log^2(x)\; dx \\
&= 2\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^3} \\
&= \frac{\pi^3}{16}
\end{aligned}
$$

This gives us

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-5}
\boxed{I_3 =-\frac{\pi^3}{64} -G \log(2) - \frac{\pi \log^2(2)}{16} +2 \text{ Im }\text{Li}_3\left(\frac{1+i}{2}\right)}
\end{equation}
$$

One can also evaluate $I_4 = \int_0^1\frac{\log(1+x^2)\arctan(x)}{x}dx$ by noting that

$$
I_4 = \text{Im}\int_0^1 \frac{\log^2(1+ix)}{x}dx = \text{Im}\int_0^{-i}\frac{\log^2(1-x)}{x}dx
$$

and using [equation (3)]({filename}/posts/euler-sums-involving-square-of-harmonic-numbers.md). The end result is:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-6}
\boxed{I_4 =-\frac{3\pi^3}{64}+G\log(2)-\frac{\pi \log^2(2)}{16}+2\text{ Im }\text{Li}_3\left(\frac{1+i}{2}\right) }
\end{equation}
$$

Using $I_3$ and $I_4$, we can evaluate $I_5 = \int_0^1 \frac{\log(x)\arctan(x)}{x(1+x^2)}dx$ as follows:

$$
\begin{aligned}
I_5 &= \int_0^1 \log(x)\arctan(x)\left(\frac{1}{x}-\frac{x}{1+x^2} \right) dx \\
&= \int_0^1 \frac{\log(x)\arctan(x)}{x}dx - \int_0^1 \frac{x\log(x)\arctan(x)}{1+x^2}dx \\
&= -\frac{1}{2}\int_0^1 \frac{\log^2(x)}{1+x^2}dx + \frac{1}{2} \int_0^1 \frac{\log(x)\log(1+x^2)}{1+x^2} dx + \frac{1}{2}\int_0^1 \frac{\log(1+x^2)\arctan(x)}{x}dx \quad (\text{IBP}) \\
&= -\frac{\pi^3}{32} + \frac{I_3 + I_4}{2} \\
&= -\frac{\pi^3}{16} - \frac{\pi \log^2(2)}{16} + 2\text{ Im }\text{Li}_3\left(\frac{1+i}{2}\right)
\end{aligned}
$$

On the other hand, we have:

$$
\begin{aligned}
I_5 &= \int_0^1 \log(x) \left(\sum_{n=0}^\infty (-1)^n \tilde{H}_n x^{2n} \right) dx\\ &= \sum_{n=0}^\infty (-1)^n \tilde{H}_n \int_0^1 x^{2n}\log(x) \; dx \\
&= -\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2} 
\end{aligned}
$$

where $\tilde{H}_n = \sum_{j=0}^n \frac{1}{2j+1}$. This gives us an interesting Euler sum:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-7}
\boxed{\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2} = \frac{\pi^3}{16} + \frac{\pi \log^2(2)}{16} - 2\text{ Im }\text{Li}_3\left(\frac{1+i}{2}\right)}
\end{equation}
$$

Of course, one can proceed in a similar manner to create more crazy integrals. The following problem is left as an exercise for the reader.

**Exercise 1:**  Using the method of residues, show that

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-8}
\sum_{n=0}^\infty \frac{(-1)^n\tilde{H}_n}{2n+1} = \frac{G}{2}+\frac{\pi \log(2)}{8}
\end{equation}
$$

## Integral #4

Many years ago, I encountered the following integral:

$$
I_6 = \int_0^1 \frac{x \arctan(x)\log(1-x^2)}{1+x^2}dx
$$

At that time, I couldn't find a solution to this problem. Hence, I ended up asking it on math.stackexchange.com. The answers that I received there involved evaluating complex logarithmic integrals by brute force. Recently, I discovered a much simpler way to solve it using the method of residues.

Let's start by breaking down $I_6$ into Euler sums.

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-9}
\begin{aligned}
I_6 &= \int_0^1 x\log(1-x^2) \left(\sum_{n=0}^\infty (-1)^n \tilde{H}_n x^{2n+1} \right)dx \\
&= \sum_{n=0}^\infty (-1)^n \tilde{H}_n \int_0^1 x^{2n+2}\log(1-x^2) dx \\
&= \sum_{n=0}^\infty (-1)^{n+1} \tilde{H}_n \left(\frac{\psi_0\left(n+\frac{5}{2} \right)+\gamma}{2n+3} \right) \\
&= \sum_{n=0}^\infty (-1)^{n+1}\left(\tilde{H}_{n+1}-\frac{1}{2n+3} \right)\left(\frac{-2\log(2)+2\tilde{H}_{n+1}}{2n+3} \right) \\
&= \sum_{n=0}^\infty (-1)^n \left(\tilde{H}_{n}-\frac{1}{2n+1} \right)\left(\frac{-2\log(2)+2\tilde{H}_{n}}{2n+1} \right) \\
&= -2\log(2)\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{2n+1}+2G\log(2) + 2\sum_{n=0}^\infty \frac{(-1)^n (\tilde{H}_n)^2}{2n+1} -2\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2} \\
&= G\log(2) - \frac{\pi \log^2(2)}{4} + 2\sum_{n=0}^\infty \frac{(-1)^n (\tilde{H}_n)^2}{2n+1} -2\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2} 
\end{aligned}
\end{equation}
$$

The result of exercise 1 was used in the last step.

Now, integrate the function $f(z) = \pi\csc(\pi z) \frac{\left( \gamma + \psi_0 \left(-z+\frac{3}{2} \right)\right)^2}{-2z+1}$ over the positively oriented square, $C_N$, with vertices $\pm \left(N+\frac{1}{4}\right)\pm i\left(N+\frac{1}{4} \right)$. It takes a bit of effort to see that

$$
\lim_{N\to \infty}\int_{C_N} f(z)\; dz = 0
$$

This implies that the sum of residues of $f(z)$ at it's poles is equal to $0$. We have

$$
\begin{aligned}
\mathop{\text{Res}}\limits_{z=-n} f(z) &= (-1)^n \frac{\left(\gamma +\psi_0\left(n+\frac{3}{2}\right) \right)^2}{2n+1} = (-1)^n \frac{\left(-2\log(2)+2\tilde{H}_n \right)^2}{2n+1}, \quad n\in\{0,1,2,\cdots\} \\
\mathop{\text{Res}}\limits_{z=n} f(z) &= (-1)^{n-1} \frac{\left(\gamma+\psi_0\left(-n+\frac{3}{2} \right) \right)^2}{2n-1} = (-1)^{n-1} \frac{\left(-2\log(2)+2\tilde{H}_{n-1} -\frac{2}{2n-1}\right)^2}{2n-1}, \quad n\in\{1,2,3,\cdots\} \\
\mathop{\text{Res}}\limits_{z=\frac{2n+1}{2}} f(z) &= (-1)^{n-1} \frac{\pi H_n}{n} - (-1)^{n-1} \frac{3\pi}{2n^2}, \quad n\in\{1,2,3,\cdots\}
\end{aligned}
$$

Summing up the residues and performing some algebraic simplifications gives:

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-10}
\begin{aligned}
&\; 8\sum_{n=0}^\infty \frac{(-1)^n (\tilde{H}_n)^2}{2n+1}-8\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2}-16\log(2)\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{2n+1}+ 4\sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^3} \\ &\quad + 8\log(2)\sum_{n=0}^\infty \frac{(-1)^n }{(2n+1)^2} + \pi\sum_{n=1}^\infty \frac{(-1)^{n-1}H_n}{n} - \frac{3\pi}{2}\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n^2} = 0 \\
&\implies 8\left(\sum_{n=0}^\infty \frac{(-1)^n (\tilde{H}_n)^2}{2n+1}-\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2} \right) + \frac{\pi^3}{8} + \pi \left(\frac{\pi^2}{12}-\frac{\log^2(2)}{2}\right)-\frac{3\pi}{2}\left(\frac{\pi^2}{12} \right) = 0 \\
&\implies \sum_{n=0}^\infty \frac{(-1)^n (\tilde{H}_n)^2}{2n+1}-\sum_{n=0}^\infty \frac{(-1)^n \tilde{H}_n}{(2n+1)^2} = -\frac{\pi^3}{96}+\frac{\pi \log^2(2)}{16} 
\end{aligned}
\end{equation}
$$

In the above calculation, we used the result of exercise 1 and that

$$
\sum_{n=1}^\infty \frac{(-1)^{n-1}H_n}{n} = \frac{\pi^2}{12}-\frac{\log^2(2)}{2}
$$

This follows from [(A)]({filename}/posts/an-alternating-euler-sum.md).
Finally, plugging equation $\eqref{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-10}$ into $\eqref{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-9}$, gives

$$
\begin{equation}\label{evaluating-very-nasty-logarithmic-integrals-part-ii-eq-11}
\boxed{I_6 = -\frac{\pi^3}{48}-\frac{\pi}{8}\log^2 (2) +G\log (2)}
\end{equation}
$$
