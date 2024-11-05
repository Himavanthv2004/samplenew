students_grades = {
    '': [85, 92, 88, 91],
    'Bob': [78, 82, 80, 85],
    'Charlie': [95, 98, 100, 97],
    'David': [60, 65, 70, 68]
}


def calculate_average(grades):
    return sum(grades) / len(grades)


with open('p1.txt', 'w') as file:
    
    file.write('Student Name\tAverage Grade\n')
    file.write('-------------------------------\n')

   
    for student, grades in students_grades.items():
        avg_grade = calculate_average(grades)
        file.write(f'{student}\t{avg_grade:.2f}\n')
