''' Check whether 5 is in list of first 5 natural numbers or not . Hint : List=>[1 2 3 4 5 ]'''
'''

i = {1,2,3,4,5}
if i in range (1,5):
    print ('five is natural number')
else:
    print('five is not in natural number')









'''8. Given a three-digit number. Find the sum of its digits'''
number = int(input("Enter the three digit number:"))
start = 1
value = 0
while start>0:
    rem = number%10
    number=number//10
    start= 1+ start
    add= rem+value
    value= rem
    if start>3:
        break
print(add, end=" ")

























































