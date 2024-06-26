import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3)

def funk(x):
    f = np.sqrt(1+x)*np.exp(x/2)-2*np.sin(2*x)*(x+x**2)
    print("x=", x, "f(x)=", f)
    return f

plt.plot(x, funk(x))
plt.plot(x, np.zeros(len(x)))
plt.show()
