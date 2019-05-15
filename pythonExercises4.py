#Loop Exercises
#1.) 1-10


# for i in range(1, 11):
#     print(i)

#2.) n to m


# userInput1 = int(input("Choose a starting number between 1 and 10:  "))
# userInput2 = int(input("Choose an ending number: "))
# x = []



#3.) Odd Numbers

# for i in range(1, 11):
#         if i % 2 != 0:
#                 print(i)

#4.) Print a Square

# num = 5

# num = 5
# for i in range(num):
#         print("*" * num)


#5.) Print a Square 2

# num = int(input("Choose a number: "))
# for i in range(num):
#         for i in range(num):
#                 print("*", end = " ")
#         print()




#6.) Print  box


# x = int(input("Enter a number between 1 and 10: "))
# y = int(input("Now enter another: "))
# for i in range(x):
#         for j in range(y):
#                 print("*" if i in [0, y-1] or j in [0, x-1] else " " , end="")
#         print()



#7.) Print a triangle


# nor = 4
# for i in range(0, nor): #<----top of pyramid, input or variable effects row number
#     for j in range(0, nor-i-1):#------this for loop executes 3 times for spaces
#         print(end=" ")#-------------^
#     for j in range(0, 2*i + 1):#--------for printing the stars in the pyramid the variable i will change
#         print("*", end="")#-------^depending on what row and execution the loop is on 
#     print()


#8.)  Print a triangle 2.

# nor = int(input("Choose a number between 1 and 10: "))
# for i in range(0, nor): 
#     for j in range(0, nor-i-1):
#         print(end=" ")
#     for j in range(0, i + 1):
#         print("*", end=" ") 
#     print()


#9.)  Multiplication Table.


# num1 = 1
# num2 = 2
# num3 = 3
# num4 = 4
# num5 = 5
# num6 = 6
# num7 = 7
# num8 = 8
# num9 = 9
# num10 = 10
# for i in range(1, 11):
#     print(num1, 'x', i, '=', num1 * i )
# for i in range(1, 11):
#     print(num2, 'x', i, '=', num2 * i )
# for i in range(1, 11):
#     print(num3, 'x', i, '=', num3 * i )
# for i in range(1, 11):
#     print(num4, 'x', i, '=', num4 * i )
# for i in range(1, 11):
#     print(num5, 'x', i, '=', num5 * i )
# for i in range(1, 11):
#     print(num6, 'x', i, '=', num6 * i )
# for i in range(1, 11):
#     print(num7, 'x', i, '=', num7 * i )
# for i in range(1, 11):
#     print(num8, 'x', i, '=', num8 * i )
# for i in range(1, 11):
#     print(num9, 'x', i, '=', num9 * i )
# for i in range(1, 11):
#     print(num10, 'x', i, '=', num10 * i )