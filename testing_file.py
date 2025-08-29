import numpy as np
import matplotllib.pyplot as plt

#richness-mass relation
def lam(M, pi, alpha):
    ln_richness = pi + (alpha * np.log(M))
    return np.exp(ln_richness)
  

   
