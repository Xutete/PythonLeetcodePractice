import numpy.matlib
import numpy as np

a = np.array([[1,2],[3,4]])

#print(a)
b = np.array([[11,12],[13,14]])
#print(b)



# creating numpy array
arr = np.array([[1, 2, 3, 4, 5],
                [np.nan, 4, np.nan, 2, 1],
                [np.nan, 2, 4, 1, 5],
                [3, 4, 3, 2, 1]])

indexList = np.isnan(arr).any(axis=1)

print(np.isnan(arr))
'''
[[False False False False False]
 [ True False  True False False]
 [ True False False False False]
 [False False False False False]]

'''

#print(indexList)
# -> Outptu: [False, True, True, False]


# remove row with missing value
arr = np.delete(arr, indexList, axis=0)
print(arr)
'''
[[1. 2. 3. 4. 5.]
 [3. 4. 3. 2. 1.]]
'''

# remove column with missing value

# creating numpy array
arr1 = np.array([[1, 2, 3, 4, 5],
                [np.nan, 4, np.nan, 2, 1],
                [np.nan, 2, 4, 1, 5],
                [3, 4, 3, 2, 1]])
# Get an index of columns which has any NaN value
index1 = np.isnan(arr1).any(axis=0)
# Delete columns with any NaN value from 2D NumPy Array
arr1 = np.delete(arr1, index1, axis=1)

print(arr1)


###########################
import pandas as pd
df = pd.DataFrame({'A': [1, np.nan, 2, 6], 'B': [5, np.nan, 8, 2]})
'''
array([[ 1.,  5.],
       [nan, nan],
       [ 2.,  8.],
       [ 6.,  2.]])
'''

m = df.to_numpy()
#print(m)

mean = np.nanmean(m, axis = 0)
idx = np.where(np.isnan(m))
print(idx)
m[idx] = np.take(mean, idx[1])
print(m)

'''
array([[1., 5.],
       [3., 5.],
       [2., 8.],
       [6., 2.]])
'''


def flag(arr, thr):
    solution = np.empty()
    for i in range(0,len(arr)):
        if arr[i]<thr:
            solution[i]=0
        else:
            solution[i]=1
    return solution
test_arr = np.array([[65],[233],[330]])
case = flag(test_arr,300)
print(case)