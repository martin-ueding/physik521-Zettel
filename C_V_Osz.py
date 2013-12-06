#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as pl

def main():
    x_gg = np.linspace(1e-2, 1e2, 1e3)
    y_gg = 1/(2*x_gg*np.sinh(1/(2*x_gg)))**2

    pl.plot(x_gg,y_gg)
    pl.xlabel(r'$\frac{k_{\mathrm{B}}T}{\hbar\omega}$')
    pl.ylabel(r'$\frac{C_V^\mathrm{Osz}}{Nk_\mathrm{B}}$')
    pl.grid(True)
    pl.savefig('C_V_Osz_gg.pdf')
    pl.clf()

    x_ll = np.linspace(1e-2, 1, 1e3)
    y_ll = 1/(2*x_ll*np.sinh(1/(2*x_ll)))**2

    pl.plot(x_ll,y_ll)
    pl.xlabel(r'$\frac{k_{\mathrm{B}}T}{\hbar\omega}$')
    pl.ylabel(r'$\frac{C_V^\mathrm{Osz}}{Nk_\mathrm{B}}$')
    pl.grid(True)
    pl.savefig('C_V_Osz_ll.pdf')
    pl.clf()
main()
