#%%
from optim import NewtonsMethod
from utils import *
import numpy as np
import sympy as sp

INIT = np.array([[0], 
                 [-1.5]], dtype=float)

def f(x, y):
    return x**2 + y**2

x = np.linspace(-2,2,20)
y = np.linspace(-2,2,20)
X, Y = np.meshgrid(x, y)
Z = f(X,Y)

x, y = sp.symbols('x y', real=True)
function = x**2 + y**2

optim = NewtonsMethod()

x_k = optim.forward(function, INIT)

function_latex = "$f(\\theta) = x^2 + y^2$"

animate_contour(x_k, X, Y, Z, function_latex, f)

animate_surface(x_k, X, Y, Z, function_latex, f)

# %%
