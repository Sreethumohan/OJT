#creating vector in numpy
import numpy as np
#creating a 1-D list(Horizontal)
list1=[1,2,3]
#creating a 1-D array(vertical)
list2=[[10],
       [20],
       [30]]
#creating a vector1,vector as row
vector1=np.array(list1)
#creating vector2,vector as column
vector2=np.array(list2)

#showing horizontal vector
print("Horizontal vector")
print(vector1)
print("Vertical Vector")
print(vector2)