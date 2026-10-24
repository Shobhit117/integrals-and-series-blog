Title: A parametric beta integral with a shifted linear denominator
Date: 2026-10-24 10:01 +0530
Slug: a-parametric-beta-integral-with-a-shifted-linear-denominator
Author: Shobhit Bhatnagar
Category: Beta and Gamma Functions
Tags: beta-function, gamma-function, definite-integrals
Summary: A homographic change of variables reduces a beta-type integral with a shifted linear denominator to Euler's beta function.
Status: published

Recall that Euler's beta function is defined for $\operatorname{Re} x > 0$ and $\operatorname{Re} y > 0$ by

$$
B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}\,dt = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}.
$$

When an extra linear factor $(x+p)^{a+b}$ appears in the denominator with its exponent matching the sum of the two beta parameters, a homographic (Möbius) substitution removes the denominator completely while preserving the unit interval $[0,1]$. We will prove that for $a, b, p > 0$,

$$
\int_0^1 x^{a-1}(1-x)^{b-1} \frac{dx}{(x+p)^{a+b}} = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}\frac{1}{(1+p)^{a} p^b}.
$$

## The homographic substitution

Before changing variables, rewrite the integrand by grouping factors of $x+p$ with $x^{a-1}$, $(1-x)^{b-1}$, and $dx$:

$$
x^{a-1}(1-x)^{b-1}\frac{dx}{(x+p)^{a+b}}
= \left(\frac{x}{x+p}\right)^{a-1}\left(\frac{1-x}{x+p}\right)^{b-1}\frac{dx}{(x+p)^2}.
$$

Now perform the change of variables

$$
\frac{x}{x+p} = \frac{t}{p+1}.
$$

Notice that $x=0$ corresponds to $t=0$, and $x=1$ corresponds to $t=1$, so the limits of integration remain $0$ and $1$. Differentiating both sides with respect to $x$ gives

$$
\begin{aligned}
\frac{p}{(x+p)^2} &= \frac{1}{p+1}\frac{dt}{dx} \\
\implies \frac{dx}{(x+p)^2} &= \frac{dt}{p(p+1)}.
\end{aligned}
$$

To express $\frac{1-x}{x+p}$ in terms of $t$, observe that

$$
\frac{1+p}{x+p} = 1 + \frac{1-x}{x+p}
\quad\text{and}\quad
1 - \frac{x}{x+p} = \frac{p}{x+p} = 1 - \frac{t}{p+1}.
$$

Subtracting $\frac{x}{x+p} = \frac{t}{p+1}$ from $\frac{1+p}{x+p} = \frac{1+p}{p}\left(1 - \frac{t}{p+1}\right) = \frac{p+1-t}{p}$ yields

$$
\frac{1-x}{x+p} = \frac{1-t}{p}.
$$

## Reduction to the standard beta integral

Substituting these three relations into the integral, we obtain

$$
\begin{aligned}
\int_0^1 x^{a-1}(1-x)^{b-1} \frac{dx}{(x+p)^{a+b}}
&= \int_0^1 \left(\frac{t}{p+1}\right)^{a-1}\left(\frac{1-t}{p}\right)^{b-1}\frac{dt}{p(p+1)} \\
&= \frac{1}{p^b(1+p)^a}\int_0^1 t^{a-1}(1-t)^{b-1}\,dt \\
&= \frac{1}{p^b(1+p)^a} B(a,b) \\
&= \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}\frac{1}{(1+p)^a p^b}.
\end{aligned}
$$

By analytic continuation, the same identity remains valid for all complex parameters $\operatorname{Re} a > 0$ and $\operatorname{Re} b > 0$, and for any $p \in \mathbb{C} \setminus [-1,0]$ using the principal branches of the powers. For a concrete application of this formula, see [an algebraic integral with a fifth root]({filename}/posts/an-algebraic-integral-with-a-fifth-root-via-the-beta-function.md).

