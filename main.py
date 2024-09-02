# print(5+6,"test",sep="" ,end=" ")
# coments
# print("print \" 2")
# print (5// 3)
# print (5**2)
# print (max(2,4,0,-25))
# print (abs(-6))
# print(pow(5,3)) #bardzracnuma 5i xoranard
# print (round(5.4)) #kloracnuma motikin
from readline import insert_text

# print( 'barlus' ,input('vedite imya'))
# numb = 5
# st = "525"
# print(st)
# print(st + str(numb))
# print(False)


# a = int(input('greq a tiv@ - '))
# b = int(input('greq b tiv@ - '))
# print (a, ' + ', b, ' = ',a+b)
# print (a, ' - ', b, ' = ',a-b)
# print (a, ' * ', b, ' = ',a*b)
# print (a, ' : ', b, ' = ',a*b)
# print ('a - b = ',a-b)
# print ('a * b = ',a*b)
# print ('a : b = ',a/b)

# num = int(input('vedite chislo'))
#
# if num > 5:
#     print('tiv@ mec e 5-ic')
# print('test')

# isNum = True
#
# if  isNum or num != 5:
#     print(True)
# elif not isNum:
#     print('test')
# else:
#     print(False)


# data = input()
#
# number = 5 if data == 'five'or data == 'fore' else 0
#
# print(number)

# word = 'Hello World'
# count = 0
# for i in word:
#     if i == "w":
#         count +=1
#
# print(count)

# for i in range(1,6,2):
#     print(i)
# status = False

# while status:
#    if input() == 'stop':
#        status = False
#
# for i in range (1,11):
#     if i % 2 == 0:
#         continue
#     if i == 6:
#         break
#     print(i)

# simvol = input('vedite bukvu: ')
# status = None
# for i in "hello":
#     if i == simvol:
#         status = True
#         break
#     else:
#         status = False
# print(status)
#
# nums = [76,2,3,4,5,6,7,8,9]
# # add last element
# nums.append(True)
#
# # add element on n index
# nums.insert(1,25)
#
# # add elements in end array
# nums.extend([23,34,56,76])
# # nums.sort()
# print(nums)
# # nums.reverse()
#
# # Delete last element
# nums.pop()
#
# # delete element on index
# nums.pop(5)
#
# # delete element on value
# nums.remove(6)
# print(nums)
#
# # count element on arr
# arr = [1,2,3,4,5,6,7,8,8,8,8,8,8]
# print(arr.count(8)) # -> 6
#
# # length array
# print(len(arr)) #-> 13

# ----------------------------------------------------
# nums = [1,3,'5',5,7,False,True]
#
# # for i in range(0 , len(nums)):
# #     print(nums[i])
#
# for el in nums:
#     el *=2
#     print(el)

n = int(input('length array: '))
nums = []

for i in range(0,n):
    string = 'add element '+str(i+1) +' : '
    nums.append(input(string))
print(nums)





