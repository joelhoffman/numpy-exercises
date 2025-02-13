# #1
import numpy as np
import subprocess

# #2
# print(np.__version__)
#
# #3
# array = np.zeros(10)
# print(array)
# #4
# print(array.itemsize * array.size)
#
# subprocess.run(["pydoc3","numpy.add"])
#
# array[4]=1
# print(array)
#
# array=np.arange(10,50)
# print(array)
#
# array=array[::-1]
# print(array)
#
# array=np.arange(0,9).reshape(3,3)
# print(array)
#
# array=np.array([1,2,0,0,4,0])
# print([x for x in range(6) if array[x] != 0]);
#
# array=np.zeros(9).reshape(3,3)
# np.fill_diagonal(array, 1)
# print(np.array_equal(array, np.identity(3)))
#
from random import randint;
# array=np.fromfunction(np.vectorize(lambda x,y,z: randint(0,100), otypes=["int"]), (3,3,3), dtype=int)
# print(array)

# #13
# array=np.fromfunction(np.vectorize(lambda x,y: randint(0,100), otypes=["int"]), (10,10), dtype=int)
# print(array)
# min=array.argmin()
# max=array.argmax()
# print(array[np.unravel_index(min,(10,10))], array[np.unravel_index(max,(10,10))])
#

# #14
array=np.fromfunction(np.vectorize(lambda x: randint(0,100)), [30])
print(array)
print(array.mean())
print(np.median(array))

# #15
array=np.ones((10,10))
array[1:9, 1:9] = np.zeros((8,8))
print(array)

# #16
array = np.vstack((np.zeros(10).reshape((1,10)), array, np.zeros(10).reshape((1,10))))
array = np.hstack((np.zeros(12).reshape((12,1)), array, np.zeros(12).reshape((12,1))))
print(array)

# #17
print([0 * np.nan, np.nan == np.nan,np.inf > np.nan, np.nan - np.nan, np.nan in set([np.nan]),0.3 == 3 * 0.1])

# #18
