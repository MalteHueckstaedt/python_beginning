#import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
#erleichtert die Darstellung von matplotlib:
#In the IPython shell, running %matplotlib sets up the
#integration so you can create multiple plot windows without
#interfering with the console session:
#%matplotlib
# für Jupyter-Notebook wäre es dieser Befehl: ""%matplotlib inline"

#Ploting and saving plots in python
plt.plot(np.random.randn(50).cumsum(), 'k--')
plt.title("Solution-1")
plt.savefig("myfigure2.png", dpi=300)
plt.show()
