##### q1 -- print numbers from 0 to 6 excluding 3 & 6 (using continue)
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num)


##### q2 -- user inputs two numbers (n,m) then create nxm 2d array with  
# value i*j in position (i,j) where i=0,1,...,n-1 & j=0,1,...,m-1
def getInputForMatrix():
    n = input('Enter number of rows: ')
    m = input('Enter number of columns: ')
    if not(n.isdigit() and m.isdigit()):
        print('Please enter only integer values!')
        return getInputForMatrix()
    else:
        NxM = [[i*j for j in range(int(m))] for i in range(int(n))]
        return(NxM)
print(getInputForMatrix())

##### q3 -- write program to filter out even nums from a list (use filter+lambda)
nums = [1,2,3,4,5,6,7,8,9,10]
def getEvens(numsToFilter): 
    return list(filter(lambda num: (num%2)-1, numsToFilter))
print(getEvens(nums))

##### q4 -- write program to return list of squares taken from list of nums
nums = [1,2,3,4,5,6,7,8,9,10]
def getSquares(numsToSquare):
    return list(map(lambda num: num**2, numsToSquare))
print(getSquares(nums))

##### q5 -- use *argv to print name/age from object parameters passed into function
def showStudent(*argv):
    for student in argv:
        name = student['name']
        age = student['age']
        print(f'name {name}\nage {age}')

showStudent({'name': 'abhi', 'age': 22}, {'name': 'vikas', 'age': 21})

