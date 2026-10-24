Title: Integral representations of the reciprocal beta function
Date: 2023-11-27 18:28:58 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: integral-representations-of-the-reciprocal-beta-function
Author: Shobhit Bhatnagar
Category: Beta and Gamma Functions
Tags: beta-function, gamma-function, contour-integration, logarithmic-integrals
Summary: A contour argument gives integral representations involving the reciprocal beta function and their logarithmic consequences.
Status: published
WordPress_ID: 1028

Integrating a suitable branch of a complex power around a contour gives a useful representation of the reciprocal beta function. We will derive the identity below and then differentiate related formulas to obtain logarithmic integrals:

$$
\int_0^\pi \left(\sin(\theta) \right)^{\alpha-1} e^{i \beta \theta} \; d\theta = \frac{\pi e^{\frac{i \pi}{2} \beta}}{\alpha 2^{\alpha-1} B \left(\frac{\alpha+\beta+1}{2}, \frac{\alpha-\beta+1}{2} \right)}
$$

We will first prove this for real parameters satisfying $\beta + 1>\alpha>0$. An analytic-continuation argument at the end will show that the identity actually holds for every real $\alpha>0$ and every complex $\beta$. Here $B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$ is the [Beta function](https://mathworld.wolfram.com/BetaFunction.html).

The idea is to integrate the principal branch of $f(z) = (1-z^2)^{\alpha-1} (-iz)^{\beta - \alpha}$ around the following contour:

![Upper-half-plane contour for the reciprocal beta integral]({static}/images/contour11.webp)

where

- $C_\epsilon$ is an arc parameterized by $e^{it}$, where $\varphi_\epsilon\leq t \leq \pi - \varphi_\epsilon$ and $\varphi_\epsilon = \text{arctan}\left( \frac{\epsilon \sqrt{4-\epsilon^2}}{2-\epsilon^2}\right)$.
- $I_{1,\epsilon}, \; I_{2,\epsilon}, \; I_{3,\epsilon}$ are circular indents of radius $\epsilon$ around the branch points -1, 1 and 0, respectively.
- $S_{1,\epsilon}$ is a line joining $-1+\epsilon$ and $-\epsilon$.
- $S_{2,\epsilon}$ is a line joining $\epsilon$ and $1-\epsilon$.

The condition $\beta + 1 > \alpha > 0$ ensures that:

$$
\lim_{\epsilon\to 0^+}\int_{I_{1,\epsilon}}f(z)\; dz = \lim_{\epsilon\to 0^+}\int_{I_{2,\epsilon}}f(z)\; dz = \lim_{\epsilon\to 0^+}\int_{I_{3,\epsilon}}f(z)\; dz = 0
$$

We'll only prove that the integral around $I_{3,\epsilon}$ tends to 0 as $\epsilon \to 0^+$. The proof is quite similar for $I_{1,\epsilon}$ and $I_{2,\epsilon}$. We have

$$
\begin{aligned}
\left| \int_{I_{3,\epsilon}} f(z) \; dz\right|
&= \left|-i\epsilon \int_0^\pi e^{it} f(\epsilon e^{it})\; dt\right| \\
&\leq \epsilon\int_0^\pi |f(\epsilon e^{it})| \; dt \\
&\leq \epsilon^{\beta-\alpha+1}
\int_0^\pi |1-\epsilon^2 e^{2it}|^{\alpha-1} \; dt.
\end{aligned}
$$

For $0<\epsilon<1$ we have

$$
1-\epsilon^2\leq |1-\epsilon^2e^{2it}|\leq 1+\epsilon^2,
$$

we must distinguish the sign of the exponent $\alpha-1$. More precisely,

$$
|1-\epsilon^2e^{2it}|^{\alpha-1}
\leq M_\alpha(\epsilon)
:=
\begin{cases}
(1+\epsilon^2)^{\alpha-1}, & \alpha\geq 1,\\
(1-\epsilon^2)^{\alpha-1}, & 0<\alpha<1.
\end{cases}
$$

Therefore,

$$
\left| \int_{I_{3,\epsilon}} f(z) \; dz\right|
\leq \pi\epsilon^{\beta-\alpha+1}M_\alpha(\epsilon).
$$

As $M_\alpha(\epsilon)\to1$, the indentation integral tends to zero whenever $\beta-\alpha+1>0$. Next, by Cauchy's theorem we have:

$$
\begin{aligned}
\int_{-1}^1 f(z) \; dz &= -i\int_0^\pi e^{it}f(e^{it})\; dt
\end{aligned}
$$

The integral on the left hand side is:

$$
\begin{aligned}\int_{-1}^1 f(z) \; dz &= 2\cos\left( (\beta-\alpha)\frac{\pi}{2}\right)\int_0^1 (1-z^2)^{\alpha-1} z^{\beta-\alpha}\; dz \\ &= \cos\left( (\beta-\alpha)\frac{\pi}{2}\right) \int_0^1 (1-w)^{\alpha-1} w^{\frac{\beta-\alpha-1}{2}}\; dw \\ &= \cos\left( (\beta-\alpha)\frac{\pi}{2}\right) B\left(\alpha, \frac{\beta-\alpha+1}{2} \right) \\ &= \cos\left( (\beta-\alpha)\frac{\pi}{2}\right) \frac{\Gamma(\alpha) \Gamma\left(\frac{\beta-\alpha+1}{2} \right)}{\Gamma\left(\frac{\beta+\alpha+1}{2} \right)} \\ &= \frac{\pi \Gamma(\alpha)}{\Gamma\left(\frac{\beta+\alpha+1}{2} \right) \Gamma\left(\frac{-\beta+\alpha+1}{2} \right)} \\
&= \frac{\pi}{\alpha B \left(\frac{\alpha+\beta+1}{2}, \frac{\alpha-\beta+1}{2} \right)}\end{aligned}
$$

The integral on the right hand side is:

$$
\begin{aligned}-i\int_0^\pi e^{it}f(e^{it})\; dt &= \int_0^\pi (1-e^{2it})^{\alpha-1}(-i e^{it})^{\beta-\alpha+1} \; dt \\
&= \int_0^\pi (2\sin(t))^{\alpha-1}e^{i\beta t -\frac{i\pi}{2}\beta}\; dt \\
&= e^{-\frac{i\pi}{2}\beta} 2^{\alpha-1} \int_0^\pi (\sin (t))^{\alpha-1}e^{i\beta t}\; dt
\end{aligned}
$$

Therefore, we have:

$$
\begin{aligned}e^{-\frac{i\pi}{2}\beta} 2^{\alpha-1} \int_0^\pi (\sin (t))^{\alpha-1}e^{i\beta t}\; dt &=  \frac{\pi}{\alpha B \left(\frac{\alpha+\beta+1}{2}, \frac{\alpha-\beta+1}{2} \right)} \\ \implies \int_0^\pi \left(\sin(t) \right)^{\alpha-1} e^{i \beta t} \; dt &= \frac{\pi e^{\frac{i \pi}{2} \beta}}{\alpha 2^{\alpha-1} B \left(\frac{\alpha+\beta+1}{2}, \frac{\alpha-\beta+1}{2} \right)}\end{aligned}
$$

We can use a similar technique to show that:

$$
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left(\cos(t)\right)^{\alpha-1}e^{i\beta t}\; dt = \frac{\pi}{\alpha 2^{\alpha-1} B \left(\frac{\alpha+\beta+1}{2}, \frac{\alpha-\beta+1}{2} \right)}, \quad \beta+1 > \alpha > 0
$$

### Removing the restriction on $\beta$

We now make the analytic-continuation argument precise. Fix a real $\alpha>0$ and define

$$
F_\alpha(\beta)
:=e^{-\frac{i\pi\beta}{2}}
\int_0^\pi (\sin t)^{\alpha-1}e^{i\beta t}\;dt
=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}
(\cos u)^{\alpha-1}e^{i\beta u}\;du.
$$

The function $F_\alpha$ is entire in $\beta$. Indeed, on every compact set of $\beta$-values, the integrand and each of its derivatives with respect to $\beta$ are bounded by a constant times the integrable function $(\cos u)^{\alpha-1}$. Thus differentiation under the integral sign is valid to every order.

On the other hand, put

$$
G_\alpha(\beta)
:=\frac{\pi\Gamma(\alpha)}
{2^{\alpha-1}
\Gamma\left(\frac{\alpha+\beta+1}{2}\right)
\Gamma\left(\frac{\alpha-\beta+1}{2}\right)}.
$$

This is also entire in $\beta$, because [$1/\Gamma(z)$ is an entire function](https://dlmf.nist.gov/5.2). The contour argument above proves $F_\alpha(\beta)=G_\alpha(\beta)$ for every real $\beta>\alpha-1$. This set has accumulation points in the complex plane, so the identity theorem gives

$$
F_\alpha(\beta)=G_\alpha(\beta),\qquad \beta\in\mathbb C.
$$

Multiplying by $e^{i\pi\beta/2}$ proves the original formula without the condition $\beta+1>\alpha$. Notice that the integral on the left still converges for every complex $\beta$ when $\alpha>0$; it is only the auxiliary beta integral along the real diameter that required the original restriction. The apparent poles on the right are harmless: when one of the gamma factors has a pole, its reciprocal is zero.

The same identity is holomorphic in $\alpha$ on the half-plane $\operatorname{Re}(\alpha)>0$. Applying the identity theorem once more, now with $\beta$ fixed and $\alpha$ as the variable, extends the result to every complex $\alpha$ with $\operatorname{Re}(\alpha)>0$.

### A lower-half-plane contour

There is a useful companion proof obtained by closing the contour in the lower half-plane. We cannot use exactly the same powers without crossing their branch cuts, so instead take principal branches in

$$
g(z)=(1-z^2)^{\alpha-1}(iz)^{-\beta-\alpha}.
$$

Use the lower unit semicircle, with the same small indentations at $-1$, $0$, and $1$. For real $\alpha>0$ and $\beta<1-\alpha$, the endpoint indentations are again $O(\left(\epsilon^\alpha\right))$, while the indentation around the origin is

$$
O\left(\epsilon^{1-\alpha-\beta}\right),
$$

and hence all three vanish. On the real diameter,

$$
\begin{aligned}
\int_{-1}^{1}g(x)\;dx
&=2\cos\left(\frac{\pi(\alpha+\beta)}{2}\right)
\int_0^1(1-x^2)^{\alpha-1}x^{-\alpha-\beta}\;dx\\
&=\cos\left(\frac{\pi(\alpha+\beta)}{2}\right)
B\left(\alpha,\frac{1-\alpha-\beta}{2}\right)\\
&=\frac{\pi\Gamma(\alpha)}
{\Gamma\left(\frac{\alpha+\beta+1}{2}\right)
\Gamma\left(\frac{\alpha-\beta+1}{2}\right)}.
\end{aligned}
$$

Take the diameter from $-1$ to $1$ and then traverse the lower arc from $1$ back to $-1$. Parameterizing that arc by $z=e^{-it}$ with $0<t<\pi$ gives

$$
g(z)\,dz
=-2^{\alpha-1}e^{-\frac{i\pi\beta}{2}}
(\sin t)^{\alpha-1}e^{i\beta t}\;dt.
$$

Cauchy's theorem therefore yields the same integral representation as before. This lower contour proves it directly in the second range $\beta<1-\alpha$, whereas the upper contour proves it for $\beta>\alpha-1$. If $0<\alpha<1$, these two ranges together cover the entire real $\beta$-axis. When $\alpha=1$, they cover every real $\beta$ except $\beta=0$, which follows immediately by continuity (or direct evaluation). For $\alpha>1$ there remains a gap $1-\alpha\leq\beta\leq\alpha-1$, so the identity-theorem argument is still the clean way to obtain the unrestricted result.

Many interesting logarithmic integrals can be derived using these identities by differentiating both sides with respect to the parameters $\alpha$ and $\beta$. One such example is:

$$
\int_0^{\frac{\pi}{2}} \theta^2 \log^2\left(\cos \theta\right)d\theta = \frac{11\pi^5}{1440}+\frac{\pi^3}{24}\log^2(2)+\frac{\pi}{2} \log(2)\zeta(3)
$$
