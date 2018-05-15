#CTI-110
#Jared Tennant
#Test Average and Grades
#4/22/18

def main():
     grade1 = int(input('Enter the first grade: '))
     grade2 = int(input('Enter the second grade: '))
     grade3 = int(input('Enter the third grade: '))
     grade4 = int(input('Enter the fourth grade: '))
     grade5 = int(input('Enter the fifth grade: '))
     calc_average(grade1, grade2, grade3, grade4, grade5)
     determine_grade()
     
def calc_average(grade1, grade2, grade3, grade4, grade5):
     num_of_grades = 5
     result = (grade1 + grade2 + grade3 + grade4 + grade5) / num_of_grades
     print('This is the average of the grades', result)

def determine_grade():
     grade = int(input('Enter a numerical grade here to see its letter grade: '))
     if grade >= 90:
          print('Your grade is an A')
     elif grade >= 80 and grade <= 89:
          print('Your grade is a B')
     elif grade >= 70 and grade <= 79:
          print('Your grade is a C')
     elif grade >=60 and grade <= 69:
          print('Your grade is a D')
     else:
          print('Your grade is an F')

main()
     
