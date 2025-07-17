import numpy as np

number_array = np.array([])

for i in range(6):
    for j in range(6):
        number_array = np.append(number_array, [j + i*10])

number_array = number_array.reshape(6, 6)

# slicing blue box
blue_box = number_array[0:, 1]
print("Blue Box:", blue_box)

# slicing pink box
pink_box = number_array[1, 2:4]
print("Pink Box:", pink_box)

# slicing green box
green_box = number_array[2:4, 4:]
print("Green Box:", green_box)