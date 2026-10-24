Title: Introduction to Theta Functions I
Date: 2021-05-12 18:01:49 +0000
Modified: 2026-10-24 00:00:00 +0530
Slug: introduction-to-theta-functions-i
Author: Shobhit Bhatnagar
Category: Elliptic Functions
Tags: elliptic-functions, Elliptic Integrals
Summary: Begin with Jacobi's theta series and derive their periodicity, zeros, and fundamental identities.
Status: published
WordPress_ID: 855

Jacobi's theta functions connect rapidly convergent series with doubly periodic functions. In this first part, we will work from their series definitions to their periodicity, zeros, and fundamental identities.

## The four theta functions

For complex $z$ and a nonzero nome $q$ with $|q|<1$, the four functions are defined by the following series. Fractional powers of $q$ are understood consistently by writing $q=e^{i\pi\tau}$ with $\operatorname{Im}\tau>0$.

$$
\begin{aligned}
\vartheta_1 (z,q) &= -i \sum_{n=-\infty}^{\infty} (-1)^n q^{(n+1/2)^2} e^{i(2n+1)z} \\
\vartheta_2 (z,q) &= \sum_{n=-\infty}^{\infty} q^{(n+1/2)^2} e^{i(2n+1)z} \\
\vartheta_3 (z,q) &= \sum_{n=-\infty}^{\infty} q^{n^2} e^{2inz} \\  
\vartheta_4 (z,q) &= \sum_{n=-\infty}^{\infty} (-1)^n q^{n^2} e^{2inz} \\ 
\end{aligned}
$$

The parameter $q$ is called the nome. Let $\tau$ be a complex number whose imaginary part is positive and write $q=e^{i\pi \tau}$ so that $|q| < 1$. Sometimes, $q$ will not be specified, so that $\vartheta_r (z)$ is written for $\vartheta_r(z,q)$ where $r=1,2,3,4$. It is easy to see that

$$
\begin{aligned}
\vartheta_1(z+\pi) &= -i e^{i \pi}\sum_{n=-\infty}^{\infty}(-1)^n q^{\left(n+\frac{1}{2}\right)^2}e^{i(2n+1)z} = -\vartheta_1(z) \\
\vartheta_1(z+\pi \tau) &= i e^{-i\pi \tau -2iz} \sum_{n=-\infty}^{\infty} (-1)^{n+1} e^{i\pi \tau \left( n+\frac{3}{2}\right)^2 + (2n+3) iz} = - (q e^{2iz})^{-1} \vartheta_1(z)
\end{aligned}
$$

Similarly, the periodicity laws for the other theta functions can be derived as well. The multipliers of the theta functions associated with the periods $\pi$ and $\pi \tau$ are summarized in the following table:

$$
\begin{array}{|c|c|c|c|c|}
\hline
\omega & \vartheta_1(z+\omega) & \vartheta_2(z+\omega) & \vartheta_3(z+\omega) & \vartheta_4(z+\omega) \\ \hline \hline
\pi & -1 & -1 & 1 & 1 \\ \hline
\pi \tau & -\lambda & \lambda & \lambda & -\lambda \\ \hline
\end{array}
$$

where $\lambda = (q e^{2iz})^{-1}$. Furthermore, incrementation of $z$ by the half periods $\frac{\pi}{2}, \frac{\pi \tau}{2}, \frac{\pi +\pi \tau}{2}$ yields the following identities:

$$
\begin{array}{|c|c|c|c|c|}
\hline
\omega & \vartheta_1(z+\omega) & \vartheta_2(z+\omega) & \vartheta_3(z+\omega) & \vartheta_4(z+\omega) \\ \hline \hline
\frac{\pi}{2} & \vartheta_2(z) & -\vartheta_1(z) & \vartheta_4(z) & \vartheta_3(z) \\ \hline
\frac{\pi \tau}{2} & i \mu \vartheta_4(z) & \mu \vartheta_3(z) & \mu \vartheta_2(z) & i\mu \vartheta_1(z) \\ \hline
\frac{\pi + \pi \tau}{2} & \mu \vartheta_3(z) & -i\mu \vartheta_4(z) & i\mu \vartheta_1(z) & \mu \vartheta_2(z) \\ \hline
\end{array}
$$

where $\mu = (q^{\frac{1}{4}}e^{iz})^{-1}$.

## Identities involving products of theta functions

Many theta function identities can be derived by multiplying their series and rearranging the terms. This is ok to do since both the series are absolutely convergent. For e.g., we have

$$
\begin{aligned}
\vartheta_3(x,q)\vartheta_3(y,q) &= \left(\sum_{n=-\infty}^{\infty} q^{n^2} e^{2inx} \right)\left(\sum_{m=-\infty}^{\infty} q^{m^2} e^{2imy} \right) \\
&= \sum_{n=-\infty}^\infty \sum_{m=-\infty}^\infty q^{n^2+m^2}e^{2i(nx+my)}
\end{aligned}
$$

Now, we change the summation indices from $(m,n)$ to $(r,s)$ using the following transformation:

$$
\begin{aligned}
r &= m+n \\
s &= m-n
\end{aligned}
$$

If $(m,n)$ are both even then $(r,s)$ will both be even and if $(m,n)$ have opposite parity then $(r,s)$ will both be odd. Therefore, we can rearrange the series as follows:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-1}
\begin{aligned}
\vartheta_3(x,q)\vartheta_3(y,q) &= \sum_{r=-\infty}^{\infty} \sum_{s=-\infty}^{\infty} q^{2(r^2 +s^2)}e^{2i(r(x+y)+s(x-y))} \\ &\quad + \sum_{r=-\infty}^{\infty} \sum_{s=-\infty}^{\infty}q^{2\left[\left(r+\frac{1}{2} \right)^2 + \left(s+\frac{1}{2} \right)^2\right]} e^{i(2r+1)(x+y) + i(2s+1)(x-y)} \\
&= \vartheta_3(x+y,q^2)\vartheta_3(x-y,q^2) + \vartheta_2(x+y,q^2)\vartheta_2(x-y,q^2) 
\end{aligned}
\end{equation}
$$

Some similar identities that can be derived using this method are:

$$
\begin{align}
\vartheta_1(x,q) \vartheta_1(y,q) &= \vartheta_3(x+y,q^2)\vartheta_2(x-y,q^2) - \vartheta_2(x+y,q^2)\vartheta_3(x-y,q^2) \label{introduction-to-theta-functions-i-eq-2}\\
\vartheta_2(x,q) \vartheta_2(y,q) &= \vartheta_2(x+y,q^2)\vartheta_3(x-y,q^2) + \vartheta_3(x+y,q^2)\vartheta_2(x-y,q^2) \label{introduction-to-theta-functions-i-eq-3}\\
\vartheta_4(x,q) \vartheta_4(y,q) &= \vartheta_3(x+y,q^2)\vartheta_3(x-y,q^2) - \vartheta_2(x+y,q^2)\vartheta_2(x-y,q^2) \label{introduction-to-theta-functions-i-eq-4}\\
\vartheta_1(x,q) \vartheta_2(y,q) &= \vartheta_1(x+y,q^2)\vartheta_4(x-y,q^2) + \vartheta_4(x+y,q^2)\vartheta_1(x-y,q^2) \label{introduction-to-theta-functions-i-eq-5}\\
\vartheta_3(x,q) \vartheta_4(y,q) &= \vartheta_4(x+y,q^2)\vartheta_4(x-y,q^2) - \vartheta_1(x+y,q^2)\vartheta_1(x-y,q^2) \label{introduction-to-theta-functions-i-eq-6}
\end{align}
$$

Squaring and subtracting identities $\eqref{introduction-to-theta-functions-i-eq-4}$ and $\eqref{introduction-to-theta-functions-i-eq-2}$ gives us:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-7}
\begin{aligned}
&\; \vartheta_4^2(x,q) \vartheta_4^2(y,q) - \vartheta_1^2(x,q) \vartheta_1^2(y,q)\\ 
&= \left[\vartheta_3^2(x+y,q^2)-\vartheta_2^2(x+y,q^2) \right]\times \left[\vartheta_3^2(x-y,q^2)-\vartheta_2^2(x-y,q^2) \right] 
\end{aligned}
\end{equation}
$$

Putting $y=0$ in the above equation gives the result:

$$
\vartheta_3^2(x,q^2)-\vartheta_2^2(x,q^2) = \vartheta_4(x,q)\vartheta_4(0,q)
$$

Now, using the above result in equation $\eqref{introduction-to-theta-functions-i-eq-7}$ gives us:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-8}
\vartheta_4(x+y,q)\vartheta_4(x-y,q)\vartheta_4^2(0,q) = \vartheta_4^2(x,q) \vartheta_4^2(y,q) - \vartheta_1^2(x,q) \vartheta_1^2(y,q)
\end{equation}
$$

Note that all theta functions in this equation have the same nome, $q$. More identities of this type can be derived by incrementing $x$ and/or $y$ by the half periods $\frac{\pi}{2},\frac{\pi \tau}{2},\frac{\pi+\pi\tau}{2}$:

$$
\begin{align}
\vartheta_1(x+y)\vartheta_1(x-y)\vartheta_4^2(0) &= \vartheta_3^2(x) \vartheta_2^2(y) - \vartheta_2^2(x) \vartheta_3^2(y) \notag\\ &= \vartheta_1^2(x) \vartheta_4^2(y) - \vartheta_4^2(x) \vartheta_1^2(y)\label{introduction-to-theta-functions-i-eq-9}\\
\vartheta_2(x+y)\vartheta_2(x-y)\vartheta_4^2(0) &= \vartheta_4^2(x) \vartheta_2^2(y) - \vartheta_1^2(x) \vartheta_3^2(y) \notag\\ &= \vartheta_2^2(x) \vartheta_4^2(y) - \vartheta_3^2(x) \vartheta_1^2(y)\label{introduction-to-theta-functions-i-eq-10}\\
\vartheta_3(x+y)\vartheta_3(x-y)\vartheta_4^2(0) &= \vartheta_4^2(x) \vartheta_3^2(y) - \vartheta_1^2(x) \vartheta_2^2(y) \notag\\ &= \vartheta_3^2(x) \vartheta_4^2(y) - \vartheta_2^2(x) \vartheta_1^2(y)\label{introduction-to-theta-functions-i-eq-11}\\
\vartheta_4(x+y)\vartheta_4(x-y)\vartheta_4^2(0) &= \vartheta_3^2(x) \vartheta_3^2(y) - \vartheta_2^2(x) \vartheta_2^2(y) \notag\\ &= \vartheta_4^2(x) \vartheta_4^2(y) - \vartheta_1^2(x) \vartheta_1^2(y)\label{introduction-to-theta-functions-i-eq-12}
\end{align}
$$

One can keep on deriving similar identities by squaring and adding equations $\eqref{introduction-to-theta-functions-i-eq-1}$ and $\eqref{introduction-to-theta-functions-i-eq-2}$ and squaring and subtracting equations $\eqref{introduction-to-theta-functions-i-eq-3}$ and $\eqref{introduction-to-theta-functions-i-eq-2}$. For a complete list of such identities, refer to [1 sec 1.4].

Another way to derive theta function identities is to utilize properties of doubly periodic functions. More details on this method are presented in [2]. Consider the function:

$$
\frac{a \vartheta_1^2(z) + b \vartheta_4^2(z)}{\vartheta_2^2(z)}
$$

This is a doubly periodic function with periods $\pi$ and $\pi \tau$. Furthermore, we can choose the constants $a$ and $b$ such that there are no poles in each cell. By Liouville's Theorem, such a function is a constant. By appropriately scaling the constants $a$ and $b$, we can make the function equal to 1. Therefore, there exists a relationship of the form:

$$
a \vartheta_1^2(z) + b \vartheta_4^2(z) = \vartheta_2^2(z)
$$

To find $a$ and $b$, we can put $z = 0, \frac{\pi\tau}{2}$:

$$
\begin{aligned}
b \vartheta_4^2(0) &= \vartheta_2^2(0) \; \implies b = \frac{\vartheta_2^2(0)}{\vartheta_4^2(0)} \\
a (i \mu\vartheta_4(0))^2 &= (\mu \vartheta_3(0))^2 \; \implies a = -\frac{\vartheta_3^2(0)}{\vartheta_4^2(0)}
\end{aligned}
$$

Thus, we have obtained the identity:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-13}
\vartheta_2^2(0) \vartheta_4^2(z) -\vartheta_3^2(0) \vartheta_1^2(z) = \vartheta_4^2(0) \vartheta_2^2(z)
\end{equation}
$$

A similar technique yields the identity:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-14}
\vartheta_3^2(0) \vartheta_4^2(z) - \vartheta_2^2(0) \vartheta_1^2(z) = \vartheta_4^2(0) \vartheta_3^2(z)
\end{equation}
$$

Incrementing $z$ by $\frac{\pi}{2}$ in $\eqref{introduction-to-theta-functions-i-eq-11}$ and $\eqref{introduction-to-theta-functions-i-eq-12}$ gives two additional identities:

$$
\begin{align}
\vartheta_4^2(0) \vartheta_1^2(z) &= \vartheta_2^2(0) \vartheta_3^2(z) - \vartheta_3^2(0) \vartheta_2^2(z) \label{introduction-to-theta-functions-i-eq-15}\\
\vartheta_4^2(0) \vartheta_4^2(z) &= \vartheta_3^2(0) \vartheta_3^2(z) - \vartheta_2^2(0) \vartheta_2^2(z) \label{introduction-to-theta-functions-i-eq-16}
\end{align}
$$

With these relations one can express any theta function in terms of any other pair of theta functions. Putting $z=0$ in $\eqref{introduction-to-theta-functions-i-eq-16}$ gives the famous identity:

$$
\vartheta_4^4(0)+\vartheta_2^4(0) = \vartheta_3^4(0)
$$

## The identity $\vartheta_1'(0)=\vartheta_2(0)\vartheta_3(0)\vartheta_4(0)$

This particular proof is from [1]. Differentiating equation $\eqref{introduction-to-theta-functions-i-eq-5}$ with respect to $x$ and substituting $x=y=0$, we get:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-17}
\vartheta_1'(0,q) \vartheta_2(0,q) = 2 \vartheta_1'(0,q^2)\vartheta_4(0,q^2)
\end{equation}
$$

Substituting $x=y=0$ in equations $\eqref{introduction-to-theta-functions-i-eq-3}$ and $\eqref{introduction-to-theta-functions-i-eq-6}$ gives:

$$
\begin{align}
\vartheta_2^2(0,q) &= 2\vartheta_2(0,q^2) \vartheta_3(0,q^2) \label{introduction-to-theta-functions-i-eq-18}\\
\vartheta_3(0,q)\vartheta_4(0,q) &= \vartheta_4^2(0,q^2) \label{introduction-to-theta-functions-i-eq-19}
\end{align}
$$

Now, dividing $\eqref{introduction-to-theta-functions-i-eq-17}$ by both $\eqref{introduction-to-theta-functions-i-eq-18}$ and $\eqref{introduction-to-theta-functions-i-eq-19}$ gives

$$
\frac{\vartheta_1'(0,q)}{\vartheta_2(0,q)\vartheta_3(0,q)\vartheta_4(0,q)} = \frac{\vartheta_1'(0,q^2)}{\vartheta_2(0,q^2)\vartheta_3(0,q^2)\vartheta_4(0,q^2)}
$$

The repeated application of this result gives:

$$
\frac{\vartheta_1'(0,q)}{\vartheta_2(0,q)\vartheta_3(0,q)\vartheta_4(0,q)} = \frac{\vartheta_1'(0,q^{2^n})}{\vartheta_2(0,q^{2^n})\vartheta_3(0,q^{2^n})\vartheta_4(0,q^{2^n})}
$$

for all positive integers $n$. Letting $n\to\infty$ in the above equation, we find that:

$$
\begin{equation}\label{introduction-to-theta-functions-i-eq-20}
\frac{\vartheta_1'(0,q)}{\vartheta_2(0,q)\vartheta_3(0,q)\vartheta_4(0,q)} = \lim_{q\to 0}\frac{\vartheta_1'(0,q)}{\vartheta_2(0,q)\vartheta_3(0,q)\vartheta_4(0,q)}
\end{equation}
$$

From the definitions of the theta functions, it is evident that

$$
\begin{aligned}
\vartheta_1'(0,q) &= 2q^{\frac{1}{4}} + \mathcal{O}(q^{\frac{9}{4}}) \\
\vartheta_2(0,q) &= 2q^{\frac{1}{4}} + \mathcal{O}(q^{\frac{9}{4}}) \\
\vartheta_3(0,q) &= 1 + \mathcal{O}(q) \\
\vartheta_4(0,q) &= 1 + \mathcal{O}(q) \\
\end{aligned}
$$

Therefore, the limit in equation $\eqref{introduction-to-theta-functions-i-eq-20}$ equals 1 and

$$
\vartheta_1'(0)=\vartheta_2(0)\vartheta_3(0)\vartheta_4(0)
$$

is established as desired.

## References

1. Derek F. Lawden (1989). *Elliptic Functions and Applications*. Springer-Verlag New York
2. E. T. Whittaker, G. N. Watson (1927). *A Course of Modern Analysis*. Cambridge University Press
