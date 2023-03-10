import numpy as np
import pandas as pd

#  compute function to calculate the row-wise standard deviation of matrix rounded tp 2 decimal places
def calculate_standard_deviation(mtrx):

    # np.var(mtrx, axis = 0) 方差
    solution = np.std(mtrx, axis = 1).round(2)    # 标准差
    return solution



text_matrix = np.array([[86, 79, 81, 85],
                       [92, 85, 87, 87],
                       [73, 77, 94, 83]])

test_case = calculate_standard_deviation(text_matrix)
print(test_case)


# compute the function to append a binary flag column is_outlier, to a dataframe to flag value above 30 in a specified column,
# return a copy of the flagged dataframe

def flag_over_30(df, column):

    #
    solution = None
    return solution

#
#text_case = flag_over_30(web_metrics, 'time_on_site')



####
# calculate classification accuracy between predicted and actual value

from sklearn.metrics import precision_score, accuracy_score
def classifier_accuracy(predicted, actual):

    solution = accuracy_score(accuracy_score, predicted)
    return solution



###
# complete the function to remove punctuation from text

import string
import re

def exclude_punctuation(text):


    
    solution =  re.sub(r'[^\w\s]', '', text)
    return solution


text_case_string = exclude_punctuation("I propose to consider the question, can machine think?")
print(text_case_string)


####
#complete the function to convert a pandas dataframe, setting the column names the dictionary keys

def dic_to_dataframe(dct):

    df = pd.DataFrame.from_dict(dct)
    # DataFrame.to_dict() 就是转化成 dct 

    solution = df
    return solution

text_dict = {'applicant_id': [12, 133, 1],
             'income': [10, 92, 53],
             'default':[1, 0, 1]}

text_case_dict = dic_to_dataframe(text_dict)
print(text_case_dict)



####
# calculate F1 score, rounded 2 decimal places, using predicted and actual values from a binary classifier


# from sklearn.metrics import precision_score, accuracy_score
from sklearn.metrics import f1_score, precision_score, recall_score
def calculate_f1_score (predicted, actual):

    # solution:
    solution = f1_score(actual, predicted).round(2)

    return solution



# calculate numpy variance

def row_variance(mtrx):

    solution = np.var(mtrx, axis = 1).round(1)

    return solution

text_matrix2 = np.array([[86, 79, 81, 5],
                         [92, 85, 87, 87],
                         [73, 77, 94, 83]])



def foo(*args):
    print('foo(', *args, ')')

    def inside_foo(x):
        print('inside_foo')

        def inside_inside_foo(*args):
            print('inside_inside_foo(', *args, ')')
            return x(*args)


        return inside_inside_foo
    return inside_foo

@foo(1,2,3)

def bar(*args):
    return sum(args)

print('outside')
print(bar(4, 5, 6))


'''
foo( 1 2 3 )
inside_foo
outside
inside_inside_foo( 4 5 6 )
15'''

#####
# complete the function to append a binary flag column, is_outlier,
# a dataframe to flage values above 30 in a specified column, returning
# a copy of the flagged dataframe


data = {'Group':['A', 'A', 'A', 'B', 'B', 'B'], 'Age':[20, 21, 19, 18, 2, 17]}
df = pd.DataFrame(data)

'''
def flag_outlier(x):
    print ("x:" + str(x))
    lower_limit = 0
    upper_limit = 30
    for i in x:
        if i >  lower_limit and i < upper_limit:
            return 1
        else:
            return 0

df['Flag'] = df.groupby('Group')['Age'].apply(flag_outlier)

print(df)


def flag_over_30_1(df, column):

    # write your solution
    df["out_lier"] = df.apply(lambda x: x.column if  x.age > 30 else 1, axis = 1)

    solution = df
    return solution


'''

def  flag_over_30_2(df, column: str):

    # np.where(condition, value if condition is true, value if condition is false)

    df['out_lier'] = np.where(df[column] > 20, 1, 0)

    # Xianyu 学长
    #df["is_outlier"] = df[column] > 20



    solution = df
    return solution 

print(df)
test_case_30_outlier = flag_over_30_2(df, 'Age')

print(test_case_30_outlier )


##### replace case insenstivity substring in string
import re
text = "PHP Exercise"
print("Original Text:", text)
redata = re.compile(re.escape('php'), re.IGNORECASE)
new_text = redata.sub('php', 'PHP Excerises')
print("New Text:", new_text)




#### StandardScalar
from sklearn.preprocessing import StandardScaler
'''

>>> from sklearn import preprocessing
>>> import numpy as np
>>> X_train = np.array([[ 1., -1.,  2.],
...                     [ 2.,  0.,  0.],
...                     [ 0.,  1., -1.]])
>>> scaler = preprocessing.StandardScaler().fit(X_train)
>>> scaler
StandardScaler()

>>> scaler.mean_
array([1. ..., 0. ..., 0.33...])

>>> scaler.scale_
array([0.81..., 0.81..., 1.24...])

>>> X_scaled = scaler.transform(X_train)
>>> X_scaled
array([[ 0.  ..., -1.22...,  1.33...],
       [ 1.22...,  0.  ..., -0.26...],
       [-1.22...,  1.22..., -1.06...]])




'''



























