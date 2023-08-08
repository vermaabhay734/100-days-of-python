############DEBUGGING#####################

# # Describe Problem
# def my_function():
# # Range function does not allow 20.
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")

# my_function()

############DEBUGGING#####################

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # Randint include both end of the digits 
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

############DEBUGGING#####################

# # Play Computer
# year = int(input("What's your year of birth?"))
# # 1994 is not included.
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

############DEBUGGING#####################

# # Fix the Errors
# # convert age to int.
# age = input("How old are you?")
# if age > 18:
# # indentation error and add fstring
# print("You can drive at age {age}.")

############DEBUGGING#####################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # double equal too
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

############DEBUGGING#####################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
# # not intended
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])