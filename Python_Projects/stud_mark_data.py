import pandas as pd
student_grades = []
total_mark = 0

stud_roll=[]
print("===========================================================")

print("Welcome to the student overall grade calculator")
number_students = int(input('How many students are on the module? '))



for students in range(number_students):
    mark = int(input('Please enter mark> '))
    student_grades.append(mark) 
    total_mark += int(mark)
    stud_roll.append(students)



    

print('=======================================================')
average_mark = int(total_mark) / number_students
print("The average mark is", average_mark)
print("The minimum mark is", min(student_grades))
print("The maximum mark is", max(student_grades))
print("Total mark for students is", total_mark)
print('=======================================================')
result=[]
for i in student_grades:
    if i<40:
        result.append('Fail')
    else:
        result.append('Pass')

data={
    "Student ID":stud_roll,
    "Student Grade":student_grades,
    "Result":result
}

df=pd.DataFrame(data)
print(df.to_string(index=False))
