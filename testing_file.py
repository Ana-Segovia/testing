import numpy as np

def lam(M, pi, alpha):
    ln_richness = pi + (alpha * np.log(M))
    return np.exp(ln_richness)
  

   
