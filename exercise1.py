##### q1 -- reverse string, print last character
str = 'Hello Python!'
print(str[::-1])
print(str[-1])


##### q2 -- get 'frain' from 'information'
str = 'information'
print(str[2::2])

##### q3 -- explain str.format and f-string
# f-string provides convienent way to interpolate strings with python expressions
put_in_string = 'Hello'
print(f'{put_in_string} world.')
# str.format provides same function as f-string only with different syntax
to_format1 = 'Hello'
to_format2 = '.'
print('{} world {}'.format(to_format1, to_format2))
# both f-string and str.format() mediate conversions for int/float types
num1 = 23
num2 = 32
print(f'my age is {num1}')
print('my age is {}'.format(num2))

##### q4 -- can we sort a dictionary?
# Ans: we can't sort the dictionary itself as it is not indexed so there is 
###### no concept of order whereby sorting can work. However, either the 
###### keys or values themselves can be sorted by retrieving them in a list
###### with, respectively, dict.keys() and dict.values().

##### q5 -- grab 'hello' from following dict assignments
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])


##### q6 -- reassign 'hello' to 'goodbye' in the following nested list
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)


###### q7 -- create a set from the following list
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set5 = set(list5)
print(set5)


###### q8 -- count number of 'i' instances in 'information'
to_count = 'information'
print(to_count.count('i'))


##### in class exercise
total_sales = 0
with open('sales.txt', mode='r') as file:
    products = eval(file.read())
    total_sales = sum([product['price'] for product in products])    
print(total_sales)




