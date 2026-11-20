
import sys
import matplotlib
#matlpotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
x = ["Apples", "Bananas"]
y = [400,320]

plt.bar(x,y)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()