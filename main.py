import functions as func
import write_in_tt as tt
import numpy as np

def main():
    r, V, R, t_max, tau = func.NU()

    for i in np.arange(1, int(t_max/tau)):
        r, V = func.integrate(r, V, R, i, tau)

    tt.writting(V,  r,  tau, t_max)
main()