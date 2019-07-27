
"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

l=list(range(20))
print(l)

list=[]
for i in range(1,20):
    list.append(i)
print(list)
"""
Hands On 2
"""
# Make a function to find whether a year is a leap year or no, return True or False 

def findleapyear():
    year=int(input("Enter year"))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    
    else:
        print("{0} is not a leap year".format(year))
                
findleapyear()
"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year
import calendar
def days_in_month(month, year):
    days=calendar.monthrange(year,month)
    print(days)
    
    
days_in_month(2,2019)


"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
a=5 #int(input("Enter no of line"))


for i in range(1,a+1):
    print("* " * i)
for i in range(a-1,0,-1):
    print("* " * i)

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
def fun():
    str=input("Enter space separated value")
    userdata=str.split()
    flag=True
    Pflag=False
    
    for i in userdata:
        if int(i)<0:
            flag=False
                        
    if flag==True:
        for a in userdata:
            if a==a[::-1]:
                Pflag=True
    
    if flag == True and Pflag == True:
        print("True")
    else:
        print("False")
        
fun()
            




"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
def pangram():
    str=input("Enter string ")
    str=str.lower()
    userlist=[]
    for i in str:
        if i ==" ":
            continue
        if i not in userlist:
            userlist.append(i)
    
    if len(userlist) == 26:
        print("PanGrams")
    else:
        print("Not panGram")
        
pangram()
    
    


"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and in membership Operator
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'Clfrn', 'klhm', 'Flrd']
    
"""
def vowels():
    state_name=[ 'Alabama', 'California', 'Oklahoma', 'Florida']
    vowel_list=['a','e','i','o','u']
    result=[]
    for state in state_name:
        str=state.lower()
        for letter in state.lower():
            if letter in vowel_list:
                str=str.replace(letter,'')
        result.append(str)
    print(result)
            
                
"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

def bricks():
    userinput=input("Enter no of small brick, big brick and target").split()
    small=int(userinput[0])
    big=int(userinput[1])
    target=int(userinput[2])
    
    if target % 5 < small:
        temp=big*5+ small
        if temp > target:
            print("True")
        else:
            print("False")
    else:
        print("False")
    
"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
def reverse():
    userinput=input("enter string")
    print(userinput[::-1])


"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""
def translate():
    userinput=input("Enter String")
    vowel=['a','e','i','o','u',' ']
    result=[]
    for word in userinput:
        for letter in word:
            if letter not in vowel:
                result.append(letter+"o"+letter)
            else:
                result.append(letter)
    print(''.join(result))
        

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
def Add(userlist):
    sum=0
    for a in userlist:
        sum+=a
    
    return sum

def multiply(userlist):
    mul=1
    for a in userlist:
        mul*=a
    
    return mul

def largest(userlist):
    return max(userlist)

def Smallest(userlist):
    return min(userlist)
def sort(userlist):
    userlist.sort()
    return userlist

def Remove_duplicate(userlist):
    result=[]
    for x in userlist:
        if x not in result:
            result.append(x)
    
    return result

def Print(userlist):
    print("Addition of list is {}".format(Add(userlist)))
    print("Multipication of list is {}".format(multiply(userlist)))
    print("Largest no in the list is {}".format(largest(userlist)))
    print("Smallest no in the list is {}".format(Smallest(userlist)))
    print("sorted list is {}".format(sort(userlist)))
    print("list of unique element is {}".format(Remove_duplicate(userlist)))
    
    
str=input("Enter element in list")
userdata = str.split()
userdata=[int(x) for x in userdata]
Print(userdata)
    
    


"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""
userdata=[]
while True:
    str=input("Enter name age and score")
    if not str:
        break
    name, age, score=str.split()
    userdata.append((name,int(age),int(score)))
userdata.sort()
print(userdata)
    
    
    
    

"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

str=input("enter values in the array")
userdata =str.split()

userdata=[int(x) for x in userdata]

userdata.sort()

userdata=userdata[1:len(userdata)-1]

avg=sum(userdata)//len(userdata)


"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
 
str=input("Enter list of element ")
userdata=str.split()
userdata=[int(x) for x in userdata]
sum=0
f=False

for x in userdata:
    if f is True:
        f=False
        continue
    if x == 13:
        f=True
        continue
    sum+=x

print(sum)  


# second way
total = 0

for index in range( len( userdata ) ):
    # checks if current number or previous number is 13
    if (userdata[index] == 13 or userdata[index-1] == 13):
        continue
    total += userdata[index]

print (total)      
