import matplotlib.pyplot as plt
import numpy as np

number_of_points = 10000

# create and initialize x and y vectors
sx = np.zeros(number_of_points)
sy = np.zeros(number_of_points)

for index in range(1, number_of_points):
    # generate a random number between 1 and 3
    k = np.random.randint(1, 4)

    # update the x and y points
    sx[index] = sx[index - 1] / 2 + k - 1
    sy[index] = sy[index - 1] / 2
    if k == 2:
        sy[index] += 2

plt.plot(sx, sy, 'k.', markersize=1)
plt.title('Sierpinski Triangle')
plt.axis('off')
plt.show()
