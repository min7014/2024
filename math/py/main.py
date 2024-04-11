<py-script>
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,4)
y = np.array([5,8,9])

fig, ax = plt.subplots()
ax.plot(x, y)
print(2)
display(fig, target="mpl")
</py-script>