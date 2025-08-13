# num = -10
# if num > 5:
#     print("Number is greater than 5")
# elif num == 5:
#     print("Number is equal to 5")
# else:
#     print("Number is less than 5")
# print("End of conditional checks")

# # contoh 2: nested conditional statements
# age = 18
# if age >= 18:
#     if age <= 30:
#         print("Young Adult")
# else:
#     print("Adult")
    
# # syntax for for loop 
# # for item in sequence:
#     #code block

# # loop through a list 
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# #loop with range 
# for i in range(5): #index akan memulai dari 0 hingga 4
#     print(i)
    
#     print("loop with range ended")
#while loop
# while True:
    #code block
    
    # contoh
# count = 3
# while count > 0:
#     print(count)
#     count -= 1
# print("While loop ended")

# #break
# for i in range(10):
#     if i == 9:
#         break  # exit the loop when i is 5
#     print(i)
# print("Break Loop ended")

# #continue
# for i in range(10):
#     if i == 5:
#         continue  # kalau i adalah 5, lewati iterasi ini
#     print(i)
# print("continue Loop ended")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)