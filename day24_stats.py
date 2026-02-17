import random
import numpy as np
data_to_be='6854567890875678908756789075342456868097954324361254576897053241252456768976745789567890756789087654'
new_data = ['685', '45', '6', '7', '89', '087', '567', '8', '9', '08', '75', '678', '907', '534', '24', '5', '68', '6', '80', '979', '54', '3', '2', '4', '36', '12', '545', '76', '89', '705', '3', '2', '412', '5', '24', '56', '768', '97', '6', '745', '789', '56', '789', '075', '67', '890', '876', '54']
starting_point=0
ending_point = 4
data_list=[]
while ending_point<=len(new_data):
    data_list.append(new_data[starting_point:ending_point])
    starting_point = ending_point
    ending_point+= 4
twodimension = [['685', '45'], ['6', '7'], ['89'], ['087', '567', '8'], ['9', '08'], ['75', '678'], ['907'], ['534', '24', '5'], ['68', '6', '80'], ['979', '54', '3'], ['2'], ['4', '36', '12'], ['545', '76', '89'], ['705', '3', '2'], ['412', '5', '24'], ['56', '768'], ['97'], ['6', '745', '789'], ['56', '789'], ['075'], ['67', '890', '876']]
print('numpy:', np.__version__)
data_np = np.array(new_data, dtype=float)
# print(type(data_np))
# print(data_np)
# print (data_list)

twodimension_np = np.array(data_list)
print(twodimension_np)
print(type(twodimension_np))
print(type(twodimension_np.tolist()))


# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5] :)<

print(twodimension_np.shape)
print(numpy_array_from_tuple.shape[0])
print(twodimension_np.size)
print(numpy_array_from_tuple.size)

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)