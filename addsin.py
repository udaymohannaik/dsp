import matplotlib.pyplot as plot
import math
import numpy as np
f1=float(input("freqency 1"))
f2=float(input("frequency 2"))
if (f2>f1):
	fr=2*f2
else:
	fr=2*f1
a=float(input("enter amplitude1"))
a1=float(input("enter amplitude 2"))
t=np.arange(0,0.1,0.0001)
x=a*(np.sin((2*(math.pi)*f1*t)))
y=a1*(np.cos((2*(math.pi)*f2*t)))
z=x+y
plot.subplot(311)
plot.plot(t,x)
plot.subplot(312)
plot.plot(t,y)
plot.subplot(313)
plot.plot(t,z)
plot.show()
