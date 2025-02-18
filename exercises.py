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
# 
# # #14
# array=np.fromfunction(np.vectorize(lambda x: randint(0,100)), [30])
# print(array)
# print(array.mean())
# print(np.median(array))
#
# # #15
# array=np.ones((10,10))
# array[1:9, 1:9] = np.zeros((8,8))
# print(array)
#
# # #16
# array = np.vstack((np.zeros(10).reshape((1,10)), array, np.zeros(10).reshape((1,10))))
# array = np.hstack((np.zeros(12).reshape((12,1)), array, np.zeros(12).reshape((12,1))))
# print(array)
#
# # #17
# print([0 * np.nan, np.nan == np.nan,np.inf > np.nan, np.nan - np.nan, np.nan in set([np.nan]),0.3 == 3 * 0.1])
#
# # #18
# array=np.diag([1,2,3,4], k=-1)
# print(array)
#
# # #19
# r1 = np.array([0,1,0,1,0,1,0,1]).reshape((1,8))
# r2 = np.array([1,0,1,0,1,0,1,0]).reshape((1,8))
# array=np.vstack((r1,r2,r1,r2,r1,r2,r1,r2))
# print(array)
#
# # #20
# print(np.unravel_index(100,(6,7,8)))
#
# # #21
# array=np.tile(np.array([0,1,1,0]).reshape(2,2), (4,4))
# print(array)
#
# # #22
# array = np.random.random((5,5)) * 20 + 30
# array = (array - array.mean()) / array.std();
# print(array)
#
# # #23
# color_dtype=np.dtype([('red','u8'),('green','u8'),('blue','u8'),('alpha','u8')])
# print(color_dtype)
#
# # #24
# array1 = np.random.random((5,3))
# array2 = np.random.random((3,2))
# print(array1 @ array2)
#
# # #25
# array = np.random.random((10)) * 5 + 5
# print(array)
# array[(array > 3) & (array < 8)] *= -1
# print(array)

# # #26
#
# print(sum(range(5)))
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))

# # ## 27
#Z = np.arange(10)
# print(Z)
# print(Z**Z)
# print(2 << Z >> 2)
# print(Z <- Z)
# print(1j*Z)
# print(Z/1/1)
# Z = np.arange(3)
# print(Z)
# print((Z<Z)>Z)
# print(Z<(Z>Z))
# print((Z==Z)==Z)

# ## 28
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int))
# print(np.array([np.nan]).astype(int).astype(float))

# # #29
# array = np.random.normal(0, 5, 10)
# print(array)
# pos = array > 0
# array[pos] = np.ceil(array[pos])
# array[~pos] = np.floor(array[~pos])
# print(array)
#
# # # 30
# array1 = np.random.normal(0, 3, 20).astype(int)
# array2 = np.random.normal(0, 3, 20).astype(int)
# print(np.intersect1d(array1,array2))

# # # 31
# with np.errstate(all='ignore'):
#     np.arange(3)/0
#

# # #32
# with np.errstate(all='ignore'):
#     print(np.sqrt(-1))
#     print(np.emath.sqrt(-1))
#     print(np.sqrt(-1) == np.emath.sqrt(-1))

# # #33
# print(np.busday_offset("today", [-1,0,1]))

# # #34
# range = np.arange(np.busday_count("2016-07-01", "2016-08-01", weekmask=[1,1,1,1,1,1,1]));
# print(range)
# print(np.busday_offset("2016-07-01", range, weekmask=[1,1,1,1,1,1,1]))
#
# Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
# print(Z)
#
# # #35
# A=np.random.random(10)
# B=np.random.random(10)
# print((A+B)*(-A/2))
# np.add(A,B, out=B)
# np.divide(B,2, out=B)
# np.multiply(A,-1, out=A)
# np.multiply(A,B, out=A)
# print(A)
#

# # #36
# array=np.random.normal(0,20, 10)
# print(array.astype(int))
# print(np.trunc(array))
# print(np.where(array>0,np.floor(array),np.ceil(array)))
# (fpart, ipart) = np.modf(array)
# print(ipart)
# print(array-fpart)
# # doesn't work for negative:
# print(array // 1)
# print(array - array%1)
