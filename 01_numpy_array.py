import numpy as np

array = np.array([[1,2,3],
                  [2,3,4]],dtype=np.int) #定義陣列型態dtype=ny.int/float


print(array)
print('number of dim', array.ndim)
print('shape : ',array.shape)
print('size', array.size)
print(array.dtype)


#定義一個都是0的陣列 np.zeros
#全部為1的陣列 np.ones

a = np.zeros((4,5)) 
print(a)

b = np.arange(10,20,3)  #arange  10,13,16,19
print(b)

c= np.arange(12).reshape((3,4))  #arange().reshape(a,b) 自己定義幾行幾列並排序
print(c)


