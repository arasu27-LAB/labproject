#Creat a numpy ndarray object
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#Dimensions in array 0-D array
import numpy as np
arr=np.array(42)
print(arr)

#1-D array
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr) 

#2-D Array
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
 
#3-D Array
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr)

#check number of dimensions
import numpy as np
a=np.array(42)
b=np.array([1,2,3,4,5]) 
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#Access Array Elements
import numpy as np
arr=np.array([1,2,3,4]) 
print(arr[0])

#Access Array Elements2
import numpy as np
arr=np.array([1,2,3,4]) 
print(arr[2]+arr[3])

#Slicing array
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])

#Numpy array shape
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

#Reshaping arrays
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)

#Iterating Arrays
import numpy as np
arr=np.array([1,2,3])
for x in arr:
  print(x)
  
#Joining NumPy arrays
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

#Splitting Numpy Arrays
import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)

#searching Arrays
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

#Sorting arrays
import numpy as np
arr=np.array([3,2,0,1])
print(np.sort(arr))



0