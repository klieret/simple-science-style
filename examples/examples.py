#!/usr/bin/env python3

"""Plot examples

Identical example to https://github.com/garrettj403/SciencePlots
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("../stylesheets/sss1.mplstyle")


def model(x: np.ndarray, p: float) -> np.ndarray:
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel="Voltage (mV)", ylabel=r"Current ($\mu$A)")

x = np.linspace(0.75, 1.25, 201)

if __name__ == "__main__":
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title="Order")
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig("sss1.jpg")
