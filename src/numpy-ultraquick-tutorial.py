import numpy as np


one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print('one_dimensional_array\n', one_dimensional_array)

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print('two_dimensional_array\n', two_dimensional_array)

sequence_of_integers = np.arange(5, 12)
print('sequence_of_integers\n', sequence_of_integers)

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print('random_integers_between_50_and_100\n', random_integers_between_50_and_100)

random_floats_between_0_and_1 = np.random.random([6])
print('random_floats_between_0_and_1\n', random_floats_between_0_and_1)

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print('random_floats_between_2_and_3\n', random_floats_between_2_and_3)
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print('random_integers_between_150_and_300\n', random_integers_between_150_and_300)

feature = np.arange(6, 21)
print('feature\n', feature)
label = (3 * feature) + 4
print('label\n', label)
noise = (np.random.random([len(feature)]) * 4) - 2
print('noise\n', noise)
label = label + noise
print('label\n', label)

