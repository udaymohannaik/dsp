import matplotlib.pyplot as plot
import math
import numpy as np
f1=float(input("freqency 1"))
f2=float(input("frequency 2"))
a=float(input("enter amplitude1"))
a1=float(input("enter amplitude 2"))
fr=float(input("enter the fr"))
e=float(input("enter the phase1"))
g=float(input("enter the phase2"))
n=np.linspace(0,10,2000)
x=(np.sin(2*np.pi*(f1/fr)*n)+e)
y=(np.cos(2*np.pi*(f2/fr)*n)+g)
z=x+y
plot.subplot(131)
plot.plot(n,x)
plot.title("sinewave f1")
plot.xlabel("------->time")
plot.ylabel("amplitude")
plot.subplot(132)
plot.plot(n,y)
plot.title("cos wave f2")
plot.xlabel("-------->time")
plot.ylabel("amplitude")
plot.subplot(133)
plot.plot(n,z)
plot.title("mixed wave")
plot.xlabel("-------->time")
plot.ylabel("amplitude")
plot.show()


