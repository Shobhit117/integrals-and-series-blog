Title: Introduction to Theta Functions II
Date: 2021-05-27 18:36:01 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: introduction-to-theta-functions-ii
Author: Shobhit Bhatnagar
Category: Elliptic Functions and Integrals
Tags: elliptic-functions, elliptic-integrals, infinite-series
Summary: Continue the study of theta functions with infinite products and connections to elliptic integrals.
Status: published
WordPress_ID: 961

In [part 1]({filename}/posts/introduction-to-theta-functions-i.md), we developed the basic identities for Jacobi's theta functions. We now derive their infinite product representations and use them to connect theta functions with elliptic integrals. We retain the convention $q=e^{i\pi\tau}$, with $\operatorname{Im}\tau>0$.

## Infinite product representations of theta functions

Let $f(z) = \prod_{n=1}^{\infty} (1-q^{2n-1}e^{2iz})(1-q^{2n-1}e^{-2iz})$. Each of these two products converges absolutely and uniformly in any bounded domain of values of $z$. Hence $f(z)$ is analytic throughout the finite part of the $z$ plane. The zeros of $f(z)$ are simple zeros at the points $z=\frac{2n+1}{2}\pi\tau+m\pi$ where $m,n\in \mathbb{Z}$. So, the zeros of $f(z)$ coincide with the zeros of $\vartheta_4(z)$. Therefore, the function $\frac{\vartheta_4(z)}{f(z)}$ has no poles or zeros in the finite part of the plane. Also, it is easy to see that $f(z+\pi) = f(z)$ and

$$
\begin{aligned}
f(z+\pi \tau) &= \prod_{n=1}^\infty (1-q^{2n+1}e^{2iz})(1-q^{2n-3}e^{-2iz}) \\
&= f(z) \frac{1-q^{-1}e^{-2iz}}{1-qe^{2iz}} \\
&= -q^{-1}e^{-2iz} f(z)
\end{aligned}
$$

That is, $\frac{\vartheta_4(z)}{f(z)}$ is a doubly periodic function with periods $\pi,\pi\tau$ and has no poles and zeros. By section 20.12 of [2], it is simply a constant, say $G$. We have

$$
\begin{equation}\label{introduction-to-theta-functions-ii-eq-1}
\vartheta_4(z) = G \prod_{n=1}^{\infty} (1-q^{2n-1}e^{2iz})(1-q^{2n-1}e^{-2iz})
\end{equation}
$$

Incrementing $z$ by the half periods $\frac{\pi}{2}, \frac{\pi \tau}{2}$ and $\frac{\pi +\pi\tau}{2}$, we get the product representations for the other theta functions:

$$
\begin{align}
\vartheta_3(z) &= G \prod_{n=1}^{\infty} (1+q^{2n-1}e^{2iz})(1+q^{2n-1}e^{-2iz})\label{introduction-to-theta-functions-ii-eq-2}\\
\vartheta_1(z) &= 2G q^{\frac{1}{4}}\sin(z) \prod_{n=1}^{\infty} (1-q^{2n}e^{2iz})(1-q^{2n}e^{-2iz}) \label{introduction-to-theta-functions-ii-eq-3}\\
\vartheta_2(z) &= 2G q^{\frac{1}{4}}\cos(z) \prod_{n=1}^{\infty} (1+q^{2n}e^{2iz})(1+q^{2n}e^{-2iz}) \label{introduction-to-theta-functions-ii-eq-4}
\end{align}
$$

Now, all that is left is to find the constant $G$. From identity $\eqref{introduction-to-theta-functions-ii-eq-3}$, it is easy to see that

$$
\vartheta_1'(0) = 2G q^{\frac{1}{4}}\prod_{n=1}^{\infty} (1-q^{2n})^2
$$

Now, using the identity $\vartheta_1'(0)=\vartheta_2(0)\vartheta_3(0)\vartheta_4(0)$, we get:

$$
\begin{aligned}
2G q^{\frac{1}{4}}\prod_{n=1}^{\infty} (1-q^{2n})^2 &= \left\{2G q^{\frac{1}{4}}\prod_{n=1}^{\infty}(1+q^{2n})^2 \right\} \times \left\{G\prod_{n=1}^{\infty}(1+q^{2n-1})^2 \right\} \\ &\quad \times \left\{G \prod_{n=1}^{\infty}(1-q^{2n-1})^2 \right\} \\
\implies G &= \prod_{n=1}^\infty (1-q^{2n})
\end{aligned}
$$

Note that the rearrangements are justified since all products converge absolutely. Finally, we have

$$
\begin{align}
\vartheta_1(z) &= 2 q^{\frac{1}{4}}\sin(z) \prod_{n=1}^{\infty} (1-q^{2n})(1-2q^{2n} \cos(2z)+ q^{4n}) \label{introduction-to-theta-functions-ii-eq-5}\\
\vartheta_2(z) &= 2 q^{\frac{1}{4}}\cos(z) \prod_{n=1}^{\infty} (1-q^{2n})(1+2q^{2n} \cos(2z) + q^{4n}) \label{introduction-to-theta-functions-ii-eq-6}\\
\vartheta_3(z) &= \prod_{n=1}^{\infty} (1-q^{2n})(1+2q^{2n-1} \cos(2z) + q^{4n-2}) \label{introduction-to-theta-functions-ii-eq-7}\\
\vartheta_4(z) &= \prod_{n=1}^{\infty} (1-q^{2n})(1-2q^{2n-1} \cos(2z) + q^{4n-2}) \label{introduction-to-theta-functions-ii-eq-8}
\end{align}
$$

## Derivatives of Ratios of Theta Functions

Consider the function $\phi(z) = \frac{\vartheta_1'(z)\vartheta_4(z) - \vartheta_1(z)\vartheta_4'(z)}{\vartheta_2(z)\vartheta_3(z)}$. Now, $\phi(z)$ is doubly periodic with periods $\pi$ and $\frac{\pi\tau}{2}$. Relative to these periods, the only possible poles of $\phi(z)$ are at points congruent to $\pi\over 2$. It is easy to verify that $\frac{\pi}{2}$ is a removable singularity. This means that $\phi(z)$ is a constant. Letting $z\to 0$, we see that $\phi(z)=\vartheta_4^2(0)$. It is therefore established that

$$
\begin{equation}\label{introduction-to-theta-functions-ii-eq-9}
\frac{d}{dz}\left(\frac{\vartheta_1(z)}{\vartheta_4(z)} \right)=\vartheta_4^2(0) \frac{\vartheta_2(z)\vartheta_3(z)}{\vartheta_4^2(z)}
\end{equation}
$$

Two other identities of this kind can be derived using the same technique:

$$
\begin{align}
\frac{d}{dz}\left(\frac{\vartheta_2(z)}{\vartheta_4(z)} \right) &=-\vartheta_3^2(0) \frac{\vartheta_1(z)\vartheta_3(z)}{\vartheta_4^2(z)} \label{introduction-to-theta-functions-ii-eq-10}\\
\frac{d}{dz}\left(\frac{\vartheta_3(z)}{\vartheta_4(z)} \right) &=-\vartheta_2^2(0) \frac{\vartheta_1(z)\vartheta_2(z)}{\vartheta_4^2(z)} \label{introduction-to-theta-functions-ii-eq-11}
\end{align}
$$

By writing $\xi = \frac{\vartheta_1(z)}{\vartheta_4(z)}$ and using identities (13) and (14) from [part 1]({filename}/posts/introduction-to-theta-functions-i.md), we obtain:

$$
\left(\frac{d\xi}{dz}\right)^2 = (\vartheta_2^2(0) - \xi^2 \vartheta_3^2(0))(\vartheta_3^2(0)-\xi^2 \vartheta_2^2(0))
$$

Using the change of variables $y = \frac{\vartheta_3(0)}{\vartheta_2(0)}\xi$ and $u = \vartheta_3^2(0) z$, the above differential equation can be written as:

$$
\left(\frac{dy}{du}\right)^2 = (1-y^2)(1-k^2 y^2)
$$

where $k = \frac{\vartheta_2^2(0)}{\vartheta_3^2(0)}$. This differential equation has the particular solution:

$$
y = \frac{\vartheta_3(0)}{\vartheta_2(0)} \frac{\vartheta_1(u \vartheta_3^{-2}(0))}{\vartheta_4(u \vartheta_3^{-2}(0))}
$$

We can write $y$ as a function of $u$ and $k$ as $y = \text{sn}(u,k)$ or simply $\text{sn}(u)$. Clearly, $\text{sn}(u,k)$ has periods $2\pi \vartheta^2_3(0)$ and $\pi \tau \vartheta_3^2(0)$. It has two simple poles congruent to $\frac{1}{2}\pi\tau \vartheta_3^2(0)$ and $\pi \vartheta_3^2(0) + \frac{1}{2}\pi\tau \vartheta_3^2(0)$. Also, it is easy to see that

$$
\int_0^1 \frac{dy}{\sqrt{(1-y^2)(1-k^2 y^2)}} = \text{sn}^{-1}(1) = \frac{\pi}{2}\vartheta_3^2(0)
$$

The integral on the left is denoted by complete elliptic integral of the first kind and is denoted by $K(k)$.

## References

1. Derek F. Lawden (1989). *Elliptic Functions and Applications*. Springer-Verlag New York
2. E. T. Whittaker, G. N. Watson (1927). *A Course of Modern Analysis*. Cambridge University Press
