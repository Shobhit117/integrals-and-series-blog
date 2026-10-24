Title: A proof of GR 3.255
Date: 2025-11-16 12:04:08 +0000
Modified: 2025-12-13 05:56:20 +0000
Slug: a-proof-of-gr-3-255
Author: Shobhit Bhatnagar
Category: Beta and Gamma Functions
Tags: beta-function, gamma-function, definite-integrals
Summary: A change of variables and an inversion symmetry reduce integral 3.255 from Gradshteyn and Ryzhik to a beta integral.
Status: published
WordPress_ID: 1189

A quadratic denominator can make a beta-type integral look forbidding. For entry 3.255 in Gradshteyn and Ryzhik, a change of variables exposes an inversion symmetry and reduces the calculation to a standard beta integral. We will prove

$$
\int _0^1 \frac{x^{\mu+\frac{1}{2}} (1-x)^{\mu-\frac{1}{2}}}{(c+2bx-ax^2)^{\mu+1}}dx = \frac{\sqrt{\pi}}{\left\{a + \left(\sqrt{c+2b-a} + \sqrt{c}\right)^2\right\}^{\mu+\frac{1}{2}}\sqrt{c+2b-a}} \frac{\Gamma \left(\mu + \frac{1}{2}\right)}{\Gamma\left(\mu+1\right)}
$$

Assume that $a,b,c$ are real and

$$
c>0,\qquad d:=c+2b-a>0,\qquad D:=a+(\sqrt d+\sqrt c)^2>0,
\qquad \operatorname{Re}\mu>-\frac12.
$$

All powers of positive real numbers use the real logarithm. These hypotheses ensure that the denominator stays positive on $[0,1]$ and that the endpoint singularities are integrable.

## Move the endpoints to zero and infinity

Write the integral as $I$ and set $t=(1-x)/x$, so that $x=1/(1+t)$. The powers of $1+t$ cancel, leaving

$$
I=\int_0^\infty\frac{t^{\mu-\frac12}}{\bigl(ct^2+2(c+b)t+d\bigr)^{\mu+1}}\,dt.
$$

Now put $r=\sqrt{d/c}$, $t=rs$, and $h=(c+b)/\sqrt{cd}$. Then

$$
I=\frac{r^{\mu+\frac12}}{d^{\mu+1}}J,
\qquad
J=\int_0^\infty\frac{s^{\mu-\frac12}}{(s^2+2hs+1)^{\mu+1}}\,ds.
$$

Notice that $D=2(c+b+\sqrt{cd})$, so $D>0$ is equivalent to $h>-1$. Consequently $s^2+2hs+1=(s-1)^2+2(h+1)s>0$ for $s>0$.

## Use the inversion symmetry

Replacing $s$ by $1/s$ in $J$ gives a second representation:

$$
J=\int_0^\infty\frac{s^{\mu+\frac12}}{(s^2+2hs+1)^{\mu+1}}\,ds.
$$

Average the two representations and factor a power of $s$ out of the denominator:

$$
J=\int_0^\infty
\frac{s+1}{2s^{3/2}}\bigl(s+s^{-1}+2h\bigr)^{-\mu-1}\,ds.
$$

The factor in front is exactly the derivative of $u=\sqrt s-1/\sqrt s$. This substitution maps $(0,\infty)$ onto the real line and satisfies $s+s^{-1}=u^2+2$. Hence

$$
J=\int_{-\infty}^{\infty}(u^2+2+2h)^{-\mu-1}\,du.
$$

## Finish with the beta integral

For $A>0$ and $\operatorname{Re}\mu>-1/2$, substituting $u=\sqrt A\,v$ and then using $v^2$ as a variable gives

$$
\int_{-\infty}^{\infty}(u^2+A)^{-\mu-1}\,du
=A^{-\mu-\frac12}B\left(\frac12,\mu+\frac12\right)
=\frac{\sqrt\pi\,\Gamma(\mu+\frac12)}{\Gamma(\mu+1)}A^{-\mu-\frac12}.
$$

Take $A=2+2h=D/\sqrt{cd}$ and restore the prefactor. The constants simplify as

$$
\frac{r^{\mu+\frac12}}{d^{\mu+1}}
\left(\frac{D}{\sqrt{cd}}\right)^{-\mu-\frac12}
=\frac{1}{\sqrt d\,D^{\mu+\frac12}},
$$

which is the claimed evaluation. The symmetry step is the key: averaging before substituting produces the exact differential needed for a single beta integral.
