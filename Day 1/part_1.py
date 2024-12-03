import numpy as np

l, r = np.loadtxt("input.txt").T
print(int(np.abs(np.sort(r) - np.sort(l)).sum()))
