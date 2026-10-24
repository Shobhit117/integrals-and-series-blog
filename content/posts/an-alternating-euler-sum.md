Title: An alternating Euler Sum
Date: 2020-07-05 19:55:22 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: an-alternating-euler-sum
Author: Shobhit Bhatnagar
Category: Uncategorized
Tags: euler-sums, polylogarithm
Summary: An alternating Euler sum leads to harmonic-number generating functions, logarithmic integrals, and polylogarithms.
Status: published
WordPress_ID: 349

Our goal is an alternating Euler sum involving harmonic numbers. The route to its evaluation passes through a generating function, logarithmic integrals, and polylogarithmic identities:

$$
\sum_{n=1}^\infty (-1)^{n+1}\frac{H_n}{n^3}
$$

where $H_n = \sum_{k=1}^n \frac{1}{k}=\int_0^1 \frac{1-t^n}{1-t}dt$ is the $n$-th harmonic number. This series resists contour integration techniques which makes its computation quite challenging. We will start with the following well known generating function identity:

$$
\sum_{n=1}^\infty H_n t^n = -\frac{\log(1-t)}{1-t} ,\quad -1 \leq t < 1
$$

Dividing the above equation by $t$ and integrating both sides, gives us:

$$
\begin{aligned}
\sum_{n=1}^\infty H_n \frac{x^n}{n} &= -\int_0^x\frac{\log(1-t)}{t(1-t)}dt \\
&= -\int_0^x \left(\frac{1}{t} + \frac{1}{1-t} \right)\log(1-t) \; dt \\
&= \text{Li}_2(x) + \frac{1}{2}\log^2(1-x) 
\end{aligned}
$$

where $-1\leq x < 1$.

## 1. Computation of $\sum_{n=1}^\infty \frac{H_n}{n^2}x^n$

Now, we will use the same process to evaluate $\sum_{n=1}^\infty \frac{H_n}{n^2}x^n$ but we'll have to divide the evaluation into two parts.

**(I)** First consider the case when $0 \leq x < 1$. We don't need this for evaluating the original series but I'll do it anyway for completeness. We have:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-1}
\begin{aligned}
\sum_{n=1}^\infty \frac{H_n}{n^2} x^n &= \int_0^x\left(\frac{\text{Li}_2(t)}{t} + \frac{1}{2}\frac{\log^2(1-t)}{t}\right)dt \\
&= \text{Li}_3(x) + \frac{1}{2}\int_0^x \frac{\log^2(1-t)}{t} dt \\
&= \text{Li}_3(x) + \frac{1}{2}\int_{\log(1-x)}^0 \frac{t^2 e^t}{1-e^t}dt \quad (t\mapsto 1-e^t) \\
&= \text{Li}_3(x) + \frac{1}{2}\sum_{n=1}^\infty \int_{\log(1-x)}^0 t^2 e^{nt} \; dt \\
&= \text{Li}_3(x) + \frac{1}{2}\sum_{n=1}^\infty \left(\frac{2}{n^3} -\frac{\log^2(1-x)}{n}(1-x)^n+\frac{2\log(1-x)}{n^2}(1-x)^n-2\frac{(1-x)^n}{n^3}\right) \\
&= \text{Li}_3(x) + \frac{\log^2(1-x)\log(x)}{2} + \log(1-x)\text{Li}_2(1-x) - \text{Li}_3(1-x) + \zeta(3) 
\end{aligned}
\end{equation}
$$

**(II)** Similarly, for the case $-1\leq x < 0$, we obtain:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-2}
\begin{aligned}
\sum_{n=1}^\infty \frac{H_n}{n^2}x^n &= \text{Li}_3(x) -\frac{1}{2}\int_x^0 \frac{\log^2(1-t)}{t}dt \\
&= \text{Li}_3(x) +\frac{1}{2}\int_{0}^{-x} \frac{\log^2(1+t)}{t}dt \quad (t\mapsto -t) \\
&= \text{Li}_3(x) +\frac{1}{2}\int_{0}^{\log(1-x)} \frac{t^2 e^t}{e^t-1}dt \quad (t\mapsto e^t-1) \\
&= \text{Li}_3(x) +\frac{1}{2} \sum_{n=0}^\infty \int_0^{\log(1-x)} t^2 e^{-nt} dt \\
&= \text{Li}_3(x) +\frac{\log^3(1-x)}{6} + \frac{1}{2}\sum_{n=1}^\infty \int_0^{\log(1-x)} t^2 e^{-nt} dt \\
&= \text{Li}_3(x) +\frac{\log^3(1-x)}{6} + \frac{1}{2}\sum_{n=1}^\infty \left(\frac{2}{n^3} -\log^2(1-x)\frac{(1-x)^{-n}}{n}-2\log(1-x)\frac{(1-x)^{-n}}{n^2}-2\frac{(1-x)^{-n}}{n^3}\right) \\
&= \text{Li}_3(x) -\frac{\log^3(1-x)}{3} +\frac{\log^2(1-x)\log(-x)}{2} -\log(1-x)\text{Li}_2\left( \frac{1}{1-x}\right)-\text{Li}_3\left(\frac{1}{1-x}\right)+\zeta(3) \end{aligned}
\end{equation}
$$

## 2. Evaluation of $\sum_{n=1}^\infty \frac{H_n}{n^3}x^n$

This is the hardest step in the evaluation. Once again, we will divide the evaluation into two parts.

**(I)** Similar to section 1, we'll first consider the case when $0\leq x < 1$.

Using integration by parts, we obtain:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-3}
\begin{aligned}
\int_0^x \frac{\zeta(3)-\text{Li}_3(1-t)}{t}dt &= \log(t)\left(\zeta(3)-\text{Li}_3(1-t) \right) \Big|_{0}^x - \int_0^x \frac{\log(t)\text{Li}_2(1-t)}{1-t}dt \\
&= \log(x)\left(\zeta(3)-\text{Li}_3(1-x) \right) - \frac{1}{2}\text{Li}_2^2 (1-x) + \frac{\zeta^2 (2)}{2} 
\end{aligned}
\end{equation}
$$

$$
\begin{equation}\label{an-alternating-euler-sum-eq-4}
\begin{aligned}
\int_0^x \frac{\log(1-t)\text{Li}_2(1-t)}{t}dt &= \log(t)\log(1-t)\text{Li}_2(1-t) \Big|_0^x - \int_0^x \log(t) \left(\frac{-\text{Li}_2(1-t)}{1-t} + \frac{\log(1-t)\log(t)}{1-t}\right)dt \\
&= \log(x)\log(1-x)\text{Li}_2(1-x) + \frac{1}{2}\text{Li}_2^2(1-x)-\frac{\zeta^2(2)}{2} - \int_0^x \frac{\log^2(t) \log(1-t)}{1-t}dt \end{aligned}
\end{equation}
$$

$$
\begin{equation}\label{an-alternating-euler-sum-eq-5}
\begin{aligned}
\int_0^x \frac{\log(t)\log^2(1-t)}{2t}dt &= \frac{1}{4}\log^2(t)\log^2(1-t)\Big|_0^x +\frac{1}{2}\int_0^x \frac{\log^2(t)\log(1-t)}{1-t}dt \\
&= \frac{1}{4}\log^2(x)\log^2(1-x) +\frac{1}{2}\int_0^x \frac{\log^2(t)\log(1-t)}{1-t}dt 
\end{aligned}
\end{equation}
$$

Putting together the results of equations $\eqref{an-alternating-euler-sum-eq-3}$, $\eqref{an-alternating-euler-sum-eq-4}$ and $\eqref{an-alternating-euler-sum-eq-5}$ gives us:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-6}
\begin{aligned}
\sum_{n=1}^\infty \frac{H_n}{n^3}x^n &= \text{Li}_4(x) +\frac{1}{4}\log^2(x)\log^2(1-x) + \log(x)\log(1-x)\text{Li}_2(1-x)\\ &\quad + \log(x)\left(\zeta(3)-\text{Li}_3(1-x) \right) -\frac{1}{2}\int_0^x \frac{\log^2(t)\log(1-t)}{1-t}dt 
\end{aligned}
\end{equation}
$$

**(II)** Now, let $-1\leq x < 0$. We have:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-7}
\begin{aligned}
-\int_x^0 \frac{\zeta(3)-\text{Li}_3\left(\frac{1}{1-t}\right)}{t}dt &= \int_0^{\frac{-x}{1-x}}\frac{\zeta(3)-\text{Li}_3(1-t)}{t(1-t)}dt \quad \left(t\mapsto\frac{-t}{1-t} \right)\\
&= \int_0^{\frac{-x}{1-x}}\frac{\zeta(3)-\text{Li}_3(1-t)}{t}dt + \int_0^{\frac{-x}{1-x}}\frac{\zeta(3)-\text{Li}_3(1-t)}{1-t}dt \\
&= \log\left(\frac{-x}{1-x}\right)\left(\zeta(3) - \text{Li}_3\left(\frac{1}{1-x}\right) \right) - \frac{1}{2}\text{Li}_2^2\left(\frac{1}{1-x}\right) + \frac{\zeta^2(2)}{2} \\
&\quad + \zeta(3)\log(1-x) + \text{Li}_4\left(\frac{1}{1-x} \right) - \zeta(4) 
\end{aligned}
\end{equation}
$$

Here, we used equation $\eqref{an-alternating-euler-sum-eq-3}$ to simplify the integral after the transformation. Similarly, we obtain:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-8}
\begin{aligned}
\int_x^0 \frac{\log(1-t)\text{Li}_2\left(\frac{1}{1-t}\right)}{t}dt &= \int_0^{\frac{-x}{1-x}}\frac{\log(1-t)\text{Li}_2(1-t)}{t(1-t)}dt \\
&= \int_0^{\frac{-x}{1-x}}\frac{\log(1-t)\text{Li}_2(1-t)}{t}dt + \int_0^{\frac{-x}{1-x}}\frac{\log(1-t)\text{Li}_2(1-t)}{1-t}dt \\
&= -\log\left(\frac{-x}{1-x} \right)\log(1-x)\text{Li}_2\left(\frac{1}{1-x}\right)+\frac{1}{2}\text{Li}_2^2\left(\frac{1}{1-x}\right)-\frac{\zeta^2(2)}{2} \\
&\quad +\text{Li}_4\left(\frac{1}{1-x}\right)+\log(1-x)\text{Li}_3\left(\frac{1}{1-x}\right) -\zeta(4) \\
&\quad -\int_0^{\frac{-x}{1-x}}\frac{\log^2(t)\log(1-t)}{1-t}dt
\end{aligned}
\end{equation}
$$

$$
\begin{equation}\label{an-alternating-euler-sum-eq-9}
\begin{aligned}
\int_x^0 \left( \frac{\log^3(1-t)}{3t} - \frac{\log^2(1-t)\log(-t)}{2t}\right) dt &= \frac{1}{6}\log^3(1-x)\log\left(\frac{-x}{1-x}\right) + \frac{1}{24}\log^4(1-x) \\
&\quad +\frac{1}{4}\log^2\left(\frac{-x}{1-x}\right)\log^2(1-x) + \frac{1}{2}\int_0^{\frac{-x}{1-x}}\frac{\log^2(t)\log(1-t)}{1-t}dt \end{aligned}
\end{equation}
$$

Finally, putting these results together gives:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-10}
\begin{aligned}
\sum_{n=1}^\infty \frac{H_n}{n^3}x^n &= \text{Li}_4(x) + 2\text{Li}_4\left( \frac{1}{1-x}\right) + \log\left(\frac{-x}{1-x} \right)\left(-\text{Li}_3\left(\frac{1}{1-x}\right) +\frac{\log^3(1-x)}{6}-\log(1-x)\text{Li}_2\left(\frac{1}{1-x} \right)\right) \\
&\quad + \log(1-x)\text{Li}_3\left(\frac{1}{1-x}\right) + \frac{\log^4(1-x)}{24} +\frac{1}{4}\log^2 \left(\frac{-x}{1-x}\right)\log^2(1-x) +\zeta(3) \log(-x)- 2\zeta(4) \\
&\quad -\frac{1}{2}\int_0^{\frac{-x}{1-x}}\frac{\log^2(t)\log(1-t)}{1-t}dt 
\end{aligned}
\end{equation}
$$

The integral $\int \frac{\log^2(t)\log(1-t)}{1-t}dt$ can be evaluated in terms of Polylogarithms (refer to section 7.6 of "Polylogarithms and Associated Functions" by Leonard Lewin). Luckily for us, there is a much simpler was to evaluate this integral between the limits $0$ and $\frac{1}{2}$.

## 3. Evaluation of $\int_0^{\frac{1}{2}}\frac{\log^2(t)\log(1-t)}{1-t}dt$

Let $I=\int_0^{1}\frac{\log^2(t)\log(1-t)}{1-t}dt$ and $J=\int_0^{\frac{1}{2}}\frac{\log^2(t)\log(1-t)}{1-t}dt$. The integral, $I$, can be evaluated by the differentiation under the integral technique.

$$
\begin{aligned}
I &= \lim_{y\to 0^+}\lim_{x\to 1}\frac{\partial^2 }{\partial x^2} \frac{\partial }{\partial y} \int_0^1 t^{x-1} (1-t)^{y-1} dt \\
&= \lim_{y\to 0^+}\lim_{x\to 1}\frac{\partial^2 }{\partial x^2} \frac{\partial }{\partial y} \left\{\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)} \right\}
\end{aligned}
$$

It takes a bit of effort to compute the derivatives in terms of Polygamma functions so I won't write the details here. One can easily verify that the end result is:

$$
I = -\frac{\pi^4}{180}
$$

Next, apply integration by parts to the integral $J$:

$$
\begin{aligned}
J &= \int_0^{\frac{1}{2}}\frac{\log^2(t)\log(1-t)}{1-t}dt \\
&= -\frac{\log^2(t)\log^2(1-t)}{2}\Big|_0^{\frac{1}{2}} + \int_0^{\frac{1}{2}} \frac{\log(t)\log^2(1-t)}{t}dt \\
&= -\frac{\log^4(2)}{2} + \int_{\frac{1}{2}}^1 \frac{\log^2(t)\log(1-t)}{1-t}dt \quad (t\mapsto 1-t)\\
&= -\frac{\log^4(4)}{2} + I-J
\end{aligned}
$$

Now, one can solve the above equation for $J$ to get:

$$
\begin{aligned}
J &= -\frac{\log^4(2)}{4}+\frac{I}{2} \\
&= -\frac{\log^4(2)}{4}-\frac{\pi^4}{360}
\end{aligned}
$$

Finally, we have everything needed to evaluate the original series. Plugging in $x=-1$ in equation $\eqref{an-alternating-euler-sum-eq-10}$ and performing some simplifications gives us the beautiful result:

$$
\boxed{\sum_{n=1}^\infty \frac{H_n}{n^3}(-1)^{n+1} = \frac{11\pi^4}{360}+\frac{\pi^2}{12}\log^2(2)-\frac{\log^4(2)}{12}-\frac{7}{4}\log(2)\zeta(3) -2\text{Li}_4\left(\frac{1}{2}\right)}
$$

A similar result is obtained by plugging $x=\frac{1}{2}$ into equation $\eqref{an-alternating-euler-sum-eq-6}$:

$$
\boxed{\sum_{n=1}^\infty \frac{H_n}{n^3 2^n}= \frac{\pi^4}{720}+\frac{\log^4(2)}{24}-\frac{1}{8}\log(2)\zeta(3) +\text{Li}_4\left(\frac{1}{2}\right)}
$$

## 4. Further Results

Let $H_n^{(2)} = \zeta(2) - \psi_1(n+1) = \sum_{k=1}^n \frac{1}{k^2}$. Then, it is easy to verify that:

$$
\sum_{n=1}^\infty t^n H_n^{(2)} = \frac{\text{Li}_2(t)}{1-t}, \quad -1\leq t < 1
$$

Now, dividing the above equation by $t$ and integrating both sides, gives us:

$$
\begin{aligned}
\sum_{n=1}^\infty \frac{H_n^{(2)}}{n}x^n &= \int_0^x \text{Li}_2(t)\left( \frac{1}{t}+\frac{1}{1-t}\right) \\
&= \text{Li}_3(x) + \int_0^x \frac{\text{Li}_2(t)}{1-t} dt \\
&= \text{Li}_3(x) -\log(1-x)\text{Li}_2(x) - \int_0^x \frac{\log^2(1-t)}{t}dt \end{aligned}
$$

From our previous calculation, we know that

$$
\int_0^x \frac{\log^2(1-t)}{t}dt = 2\sum_{n=1}^\infty \frac{H_n}{n^2}x^n -2\text{Li}_3(x)
$$

Hence, we obtain the following relation:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-11}
\sum_{n=1}^\infty \frac{H_n^{(2)}}{n}x^n =3\text{Li}_3(x)-\log(1-x)\text{Li}_2(x) - 2\sum_{n=1}^\infty \frac{H_n}{n^2}x^n
\end{equation}
$$

Once again, divide the above equation by $x$ and integrate both sides to get:

$$
\begin{equation}\label{an-alternating-euler-sum-eq-12}
\sum_{n=1}^\infty \frac{H_n^{(2)}}{n^2}x^n = 3\text{Li}_4(x) + \frac{1}{2}\text{Li}_2^2(x) - 2\sum_{n=1}^\infty \frac{H_n}{n^3}x^n
\end{equation}
$$

Equations $\eqref{an-alternating-euler-sum-eq-11}$ and $\eqref{an-alternating-euler-sum-eq-12}$ are valid for $-1\leq x < 1$. Plugging in $x=\frac{1}{2}$ in equation $\eqref{an-alternating-euler-sum-eq-12}$ and using the known closed form for $\sum_{n=1}^\infty \frac{H_n}{n^3 2^n}$ gives us:

$$
\boxed{ \sum_{n=1}^\infty \frac{H_n^{(2)}}{n^2 2^n} = \frac{\pi^4}{1440}-\frac{\pi^2}{24}\log^2(2) + \frac{\log^4(2)}{24}+ \frac{1}{4}\log(2)\zeta(3) + \text{Li}_4\left(\frac{1}{2}\right) }
$$
