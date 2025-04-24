import numpy as np
import matplotlib.pyplot as plt

## Task1
def force(x, k=2):
    return -k*x

def energy(x, k=2):
    return 0.5*k*(x**2)

x = np.linspace(-10,10,100)

f = force(x)
u = energy(x)


plt.plot(x,f)
plt.title("Force by distance")
plt.show()

plt.plot(x,u)
plt.title("Potential Energy by Distance")
plt.show()

## Task2
#time steps
t = np.linspace(0,10,11)

def velo(vt, F, m, dt=1):
    return vt + (F/m)*dt

def pos(xt,vt, dt=1):
    return xt + vt*dt