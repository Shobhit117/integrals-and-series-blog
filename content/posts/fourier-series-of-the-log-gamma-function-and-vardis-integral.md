Title: Fourier Series of the Log-Gamma Function and Vardi's Integral
Date: 2020-06-01 12:11:38 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: fourier-series-of-the-log-gamma-function-and-vardis-integral
Author: Shobhit Bhatnagar
Category: Logarithmic Integrals
Tags: logarithmic-integrals, gamma-function, fourier-series, definite-integrals
Summary: Derive Kummer's Fourier series for the logarithm of the gamma function, then use it to evaluate Vardi's integral.
Status: published
WordPress_ID: 210

Kummer's Fourier series for $\log\Gamma$ provides a useful bridge between special functions and logarithmic integrals. We will derive the series and then evaluate it at a suitable point to obtain Vardi's integral:

$$
\int_0^1 \frac{\log\log \left(\frac{1}{x}\right)}{1+x^2}dx = \frac{\pi}{2}\log\left(\sqrt{2\pi}\frac{\Gamma\left(\frac{3}{4}\right)}{\Gamma\left(\frac{1}{4}\right)} \right)
$$

## Fourier Series of the Log-Gamma Function:

For $s\in (0,1)$, we have

$$
\begin{equation}\label{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-1}
\log \Gamma(s) = \left(\frac{1}{2}-s \right)(\gamma + \log 2)-\frac{1}{2}\log(\sin (\pi s)) + (1-s) \log(\pi) + \frac{1}{\pi}\sum_{n=1}^\infty \frac{\sin(2\pi n s)\log n}{n}
\end{equation}
$$

**Proof:**  It suffices to do the following integrals:

$$
\begin{aligned}
\int_0^1 \log \Gamma (s) \; ds &= \frac{1}{2}\log(2\pi) \\
\int_0^1 \log \Gamma(s) \cos(2\pi n s)\; ds &= \frac{1}{4n} \quad \forall n\in \mathbb{Z}^+ \\
\int_0^1 \log \Gamma(s) \sin(2\pi n s)\; ds &= \frac{\gamma + \log(2n\pi )}{2n\pi}\quad \forall n\in \mathbb{Z}^+
\end{aligned}
$$

The first integral can be evaluated with the help of Euler's reflection formula:

$$
\begin{aligned}
\int_0^1 \log \Gamma(s) \; ds &= \frac{1}{2} \int_0^1 \log \Gamma(s) \; ds + \frac{1}{2}\int_0^1 \log \Gamma(1-s) \; ds \\
&= \frac{1}{2}\int_0^1 \log\left(\frac{\pi}{\sin(\pi s)} \right)\; ds \\
&= \frac{\log (\pi)}{2} - \frac{1}{2}\int_0^1 \log(\sin(\pi s))\; ds \\
&= \frac{\log(2\pi)}{2}
\end{aligned}
$$

The second integral can also be dealt in a similar way. We have:

$$
\begin{aligned}
\int_0^1 \log \Gamma(s) \cos(2\pi n s)\; ds &= \frac{1}{2}\int_0^1 \log \Gamma(s) \cos(2\pi n s)\; ds + \frac{1}{2}\int_0^1 \log \Gamma(1-s) \cos(2\pi n (1-s))\; ds \\
&= \frac{1}{2}\int_0^1 \log\left(\frac{\pi}{\sin(\pi s)} \right)\cos(2\pi n s)\; ds \\
&= -\frac{1}{2}\int_0^1 \log(2\sin(\pi s))\cos(2\pi n s)\; ds \\
&= \frac{1}{2}\int_0^1 \left(\sum_{k=1}^\infty \frac{\cos(2\pi k s)}{k} \right)\cos(2\pi n s)\; ds \\
&= \frac{1}{2}\sum_{k=1}^\infty \frac{1}{k}\int_0^1 \cos(2\pi k s)\cos(2\pi n s)\; ds \\
&= \frac{1}{4n}
\end{aligned}
$$

In the above calculation, we used the well known Fourier series:

$$
\begin{equation}\label{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-2}
\log(2\sin (\pi s)) = -\sum_{k=1}^\infty \frac{\cos(2\pi k s)}{k} \quad \forall s\in (0,1) \quad
\end{equation}
$$

The third integral is the most troublesome of all since the trick involving Euler's reflection formula does not work. We will instead use the following integral representation of the Log-Gamma function:

$$
\log \Gamma(s) = \int_0^\infty \left(\frac{s-1}{t e^t} -\frac{1-e^{t(1-s)}}{t(e^t-1)}\right) dt \quad \forall s>0
$$

One can easily verify the above equation via the differentiation under the integral technique. Therefore, upon changing the order of integration we get:

$$
\begin{aligned}
\int_0^1 \log \Gamma(s) \sin(2\pi n s)\; ds &= \int_0^\infty \left(\frac{1}{t e^t}\int_0^1 s\sin(2\pi ns)\; ds +\frac{1}{t(e^t-1)}\int_0^1e^{t(1-s)}\sin(2\pi n s)\; ds  \right)dt \\
&= \int_0^\infty \left[\frac{1}{t e^t}\left(-\frac{1}{2\pi n}\right) +\frac{1}{t(e^t-1)}\left(\frac{2\pi n (e^t-1)}{t^2 + (2\pi n)^2} \right)  \right]dt \\
&= \int_0^\infty \left(-\frac{1}{2\pi n t e^t} + \frac{2\pi n}{t\left( t^2 + (2\pi n)^2 \right)} \right)dt \\
&= \frac{1}{2\pi n}\int_0^\infty\left(-\frac{1}{te^t} +\frac{1}{t}-\frac{t}{t^2 + (2\pi n)^2} \right) dt \\
&= \frac{1}{2\pi n}\left(\gamma + \left[ \log t - \log (t) e^{-t} - \frac{1}{2}\log\left( t^2 + (2\pi n)^2 \right)\right]_{t=0}^\infty  \right) \\
&= \frac{\gamma + \log(2\pi n)}{2\pi n}
\end{aligned}
$$

To get equation $\eqref{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-1}$, one needs to piece together all these calculations. Equation $\eqref{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-2}$ along with the result:

$$
\pi \left(\frac{1}{2}- s\right) = \sum_{k=1}^\infty \frac{\sin(2\pi k s)}{k} \quad \forall s\in (0,1)
$$

are needed to perform simplifications.

Now, we turn our attention to the Vardi's integral:

$$
\begin{equation}\label{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-3}
\begin{aligned}
I &= \int_0^1 \frac{\log\log \left(\frac{1}{x}\right)}{1+x^2}dx \\ &= \int_0^\infty \frac{\log(t) e^{-t}}{1 + e^{-2t}}dt \\
&= \int_0^\infty \log(t)\sum_{n=0}^\infty (-1)^n e^{-(2n+1)t} \; dt\\
&= \sum_{n=0}^\infty (-1)^n \int_0^\infty \log (t) e^{-(2n+1)t}\; dt \\
&= -\sum_{n=0}^\infty (-1)^n \left(\frac{\log(2n+1)}{2n+1}+\frac{\gamma}{2n+1} \right) \\
&=  -\frac{\gamma \pi}{4}-\sum_{n=1}^\infty \frac{\sin\left(\frac{\pi n}{2}\right)\log n}{n} 
\end{aligned}
\end{equation}
$$

To get the value of the sum, plug $s=\frac{1}{4}$ in equation $\eqref{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-1}$.

$$
\sum_{n=1}^\infty \frac{\sin\left(\frac{\pi n}{2}\right)\log n}{n} = \pi \log \Gamma\left(\frac{1}{4}\right) - \frac{\gamma \pi}{4} - \frac{\pi \log 2}{2}- \frac{3\pi}{4}\log(\pi)
$$

Substituting the above into equation $\eqref{fourier-series-of-the-log-gamma-function-and-vardis-integral-eq-3}$ and performing some simplifications gives the desired result.
