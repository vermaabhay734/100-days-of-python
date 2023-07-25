student_height = input("Enter the list of student height: ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

# without len and sum function
lenght = 0
for i in student_height:
    lenght += i
# print(lenght)

sum = 0
for i in student_height:
    sum += 1
# print(sum)
print(f"Average height in a class is : {round(sum/lenght)}")


# with len and sum function
# print(round(sum(student_height)/len(student_height)))
# print(min(student_height))
# print(max(student_height))


# Largest height 
largest = 0
for i in student_height:
    if i > largest:
        largest = i
    
print(f"Largest height is: {largest}")