"""CS 108 Lab 10

This driver uses the Employee class to compute and save corporate statistics.

@author: Palmer Ford (pjf5)
@date: fall, 2021
"""

from employee import Employee

employees = []

# Construct an employee object for each employee specified in 'employees.txt'
# and add it to the employees list.
employeesfile = open("employees.txt")
lines = employeesfile.readlines()
employeesfile.close()

count = 0
for i in lines:
    count += 1
    values = i.split(',')
    employees.append(Employee(values[0], values[1], values[2], int(values[3].strip())))

# Write the total number of employees into the 'employee-count.txt' file.
countfile = open('employee-count.txt', 'w') 
countfile.write(str(count))
countfile.close()

# Compute statistics for employees
if len(employees) == 0:
    print('There are no employees for there to be statistics of')
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for employee in employees:
        if employee.rank in totals:
            totals[employee.rank] += employee.salary
            counts[employee.rank] += 1
        else:
            totals[employee.rank] = employee.salary
            counts[employee.rank] = 1
        if employee.salary > max_employee.salary:
            max_employee = employee
        elif employee.salary < min_employee.salary:
            min_employee = employee

# Writes the statistics for employees onto a .txt file
statsfile = open('employee-stats.txt', 'w')
statsfile.write("Maximum and Minimum Salaries\n")
statsfile.write(str(max_employee) + '\n')
statsfile.write(str(min_employee) + '\n')
statsfile.write("Rank and Average Salaries\n")
for rank in totals:
    statsfile.write(rank + ': {:.2f}'.format(totals[rank] / counts[rank]) + '\n')
statsfile.close()