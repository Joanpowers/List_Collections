
#modify 80 into 89
#add a new value called 55
#find the size of the list having apended item 55
#write a python program to sum allitems in the list.
#write a python function that takes two lists and returns true if they have one common member

#modify 80 to 89
student_marks = [60,70,80]
student_marks [2] ="89"
print(student_marks)

#add a new value 55(append the new list)
new_student_marks = [60,70,89]
new_student_marks.append (55)
print(new_student_marks)

#find the size of the list having 55
print(len(new_student_marks))

#a program to sum all the items in the list
new_student_marks = [60,70,89,55]
total_marks = sum(new_student_marks)
print(total_marks)


#write a python program that takes two lists and return true if they have a common number
comon_numbers = (60,70)
list1 = (input("student_marks:"))
list2 = (input("new_student_mark:"))
if 60 and 70 in student_marks :
    print("True ,there is a common number in list1 and list2")
else:
  print("False,there is no common number in list1 and list2")

  

