#Exercise 3 List Ex. Step 1

# x = 12 + 5 + 8 + 7
# print(x)

#Exer. 3 step 2.

# list = [2, 56, 3, 9, 1, 34, 99]
# print(max(list))

#Exer. 3 step 3.

# list = [2, 56, 3, 9, 1, 34, 99]
# print(min(list))

#Exer. 3 step 4.

# list = list(range(1, 11))
# evenNum = []
# for i in list:
#     if i % 2 == 0:
#         evenNum.append(i)
# print(evenNum)

#Exer. 3 step 5.

# list = [-3, -2, -1, 0, 1, 2, 3, 4]

# for num in list:
#     if num > 0:
#         print(num)


# #Exer. 3 step 6.

# list = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# newList = []
# for num in list:
#     if num >= 0 and num % 2 ==0:
#         print(num)


# #Exer. 3 step 7.

# num = [1, 2, 3, 4, 5]
# value = [i * 5 for i in num]
# print(value)

# #Exer. 3 step 8.

# num = [1, 2, 3, 4]
# num1 = [2, 3, 4, 5]
# num2 = []
# for a,b in zip(num, num1):
#     num2.append(a * b)
# print(num2)

# #Exer. 3 step 9.

# list1 = [[2, 4],
#         [5, 3]]
# list2 = [[1, 5],
#         [2, 3]]
# number = [[0, 0],
#           [0, 0]]        
# for i in range(len(list1)):
#     for j in range(len(list1[0])):
#         number[i][j] = list1[i][j] + list2[i][j]
# print(number)


# #Exer. 3 step 10.



# list1 = [[2, 4, 8, 6, 3],
#         [5, 3, 7, 3, 1]]
# list2 = [[1, 5, 0, 4, 8],
#         [2, 3, 8, 5, 2]]
# number = [[0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0]]        
# for i in range(len(list1)):
#     for j in range(len(list1[0])):
#         number[i][j] = list1[i][j] + list2[i][j]

# print(number[0])
# print(number[1])


# #Exer. 3 step 11.

# list1 = [2, 8, 3, 9, 2, 4, 3, 4, 8, 6, 3]
# list1 = list(dict.fromkeys(list1))
# print(list1)

