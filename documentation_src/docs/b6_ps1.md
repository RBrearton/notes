## Q1: Einstein solid

We're asked to consider a single simple harmonic oscillator, given by $H = \frac{p^2}{2m} + \frac{1}{2}kx^2$

### Classical partition function

We're asked to calculate the classical partition function $Z=\int \frac{d^3p}{(2\pi\hbar)^3} \int d^3x e^{-\beta H(\vec{p}, \vec{x})}$

??? abstract "Show working"

    It's easy however you tackle it, but I decided to solve the 1D partition function, then cube it.
    It's instructive to note that, since we're just looking at heat capacities, we can ignore the prefactor of $\frac{1}{2\pi\hbar}$ in the momentum integral.
    We have:
    $$
    Z_\mathrm{1D} = \iint  e^{-\beta \left(\frac{p^2}{2m} + \frac{1}{2}kx^2\right)} dx dp
    $$

    We can then use the standard Gaussian integral:
    $$
    \int e^{-ax^2} dx = \sqrt{\frac{\pi}{a}}
    $$

    to get:

    $$
    Z_\mathrm{1D} = \sqrt{\frac{\pi}{\beta/2m}} \sqrt{\frac{\pi}{k\beta/2}}
    $$

    Now writing this in terms of $\omega = \sqrt{k/m}$, we get:

    $$
    Z_\mathrm{1D} = \frac{2\pi}{\beta\omega}
    $$

    We can then cube this to get the 3D partition function.

???+ success "Answer"

    $Z_\mathrm{3D} = \left(\frac{2\pi}{\beta\omega}\right)^3$

### Heat capacity from the classical partition function

Now we're asked to calculate the heat capacity from the classical partition function that we just calculated.

??? abstract "Show working"

    Another easy calculation. Start by calculating the internal energy $U$:

    $$
    U = -\frac{\partial}{\partial \beta} \ln Z = -\frac{\partial}{\partial \beta} \ln \left(\frac{2\pi}{\beta\omega}\right)^3 = 3k_BT
    $$

    Then the heat capacity is:

    $$
    C = \frac{\partial U}{\partial T} = 3k_B
    $$

???+ success "Answer"

    $C = 3k_B$

!!! note "Note"

    This means that, for a 3D system containing N oscillators, we have $C = 3R$, which is the Dulong-Petit law.

### Quantum partition function

We're asked to now calculate the quantum partition function $Z = \sum_n e^{-\beta E_n}$

??? abstract "Show working"

    We can use the fact that the energy levels are $E_n = \hbar \omega (n + 1/2)$, so we have:

    $$
    Z = \sum_n e^{-\beta \hbar \omega (n + 1/2)} = e^{-\beta \hbar \omega / 2} \sum_n e^{-\beta \hbar \omega n}
    $$

    The sum is a geometric series, so we can write it as:

    $$
    Z = e^{-\beta \hbar \omega / 2} \frac{1}{1 - e^{-\beta \hbar \omega}}
    $$

    We can then simplify this to:

    $$
    Z = \frac{e^{-\beta \hbar \omega / 2}}{1 - e^{-\beta \hbar \omega}} = \left(2\sinh(\beta \hbar \omega / 2)\right)^{-1}
    $$

???+ success "Answer"

    $Z = \left(2\sinh(\beta \hbar \omega / 2)\right)^{-1}$

!!! note "Note"

    The internal energy, once we calculate it, looks reminiscent of Bose-Einstein statistics.

    $$
    U = -\frac{\partial}{\partial \beta} \ln Z = \frac{\hbar \omega}{2} + \frac{\hbar \omega}{e^{\beta \hbar \omega} - 1}
    $$

    Where the Bose occupation number is $n_B = \frac{1}{e^{\beta \hbar \omega} - 1}$.
    The physical interpretation of this is that a quantum harmonic oscillator is, on average, excited up to the energy level equal to the Bose occupation number.
    I don't believe that there's a deeper physical meaning to this, but it's interesting to note.(1)
    { .annotate }

    1. If there's a deeper physical connection, please let me know!

Next we're asked to find an expression for the heat capacity of the quantum harmonic oscillator.

??? abstract "Show working"

    We can start by calculating the internal energy, as we did above:

    $$
    U = \frac{\hbar \omega}{2} + \frac{\hbar \omega}{e^{\beta \hbar \omega} - 1}
    $$

    Then the heat capacity is:

    $$
    C = \frac{\partial U}{\partial T} = \frac{\hbar \omega}{k_B} \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2}
    $$

    We can then simplify this to:

    $$
    C = k_B \left(\frac{\beta \hbar \omega}{2}\right)^2 \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2}
    $$

    Note that this is the 1D case.
    To get the 3D case, we would need to cube the partition function, which would give us an extra factor of 3 in the heat capacity.
    Similarly, to generalize for $N$ oscillators, we'd end up raising the partition function to the power of $N$, which would give us an extra factor of $N$ in the heat capacity.

???+ success "Answer"

    $$
    C = 3 N k_B (\beta \hbar \omega)^2 \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2}
    $$

## Q2: Debye model

We're asked to state the assumptions of the Debye model.

??? abstract "Answer"

    1. Linear dispersion relation: $\omega = v_s k$
    2. The speed of sound is the same in all directions (isotropy)
    3. There's a maximum frequency, the Debye frequency $\omega_D$, which is the highest frequency that can be supported by the lattice, such that $N_\mathrm{modes} = 3N_\mathrm{atoms}$
