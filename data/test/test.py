import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(0,10,1000)
y=np.sin(x)+1
z=np.cos(x)+1

# plt.figure(figsize=(8,4))
# plt.plot(x,y,'b--',label='$\sinx+1$',color='red',linewidth=2)
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.ylim(0,2.5)
# plt.title("example")
# plt.legend()
# plt.show()

s=pd.Series([1,2,3],index=['a','b','c'])
d2=pd.DataFrame(s)
print d2
d=pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
print d.add(9)











