#!/usr/bin/env python
# coding: utf-8

# # Assignment: 
# 
# Using a text editor, write a program that calculates the salary for the week of the employees listed below. If an employee worked more than 40 hours that week, then calculate the remaining hours as time and a half (1.5x the normal rate).The program should print their name and salary earned. Upload your finished script to Github and use its URL for your assignment submission.

# In[10]:


employee_data = [['ID_Number', 'Name', 'Pay_Rate', 'Hours_Worked'],[1, 'Mary', 15.00, 40], [2, 'John', 22.00, 25], 
       [3, 'Bob', 35.00, 4], [4, 'Mel', 43.00, 62],
       [5, 'Jen', 17.00, 33],[6, 'Sue', 29.00, 45],
       [7, 'Ken', 40.00, 36],[8, 'Dave', 20.00, 17],
       [9, 'Beth', 37.00, 37],[10, 'Ray', 16.50, 80]] 
#Let me retrive important datas for calculating the pay and this are Name, Hours, and Rate
Employee_Name = []
for employee in employee_data[1:]: # loops through the big list employee_data
    Employee_Name.append(employee[1] ) # adds it to Employee_Name list
    
Hours_Worked = []

for employee in employee_data[1:]: # loops through the big list employee_data
    Hours_Worked.append(employee[3] ) # adds it to Hours_Worked list
    
    
Pay_Rate = []
for employee in employee_data[1:]: # loops through the big list employee_data
    Pay_Rate.append(employee[2] )# adds it to Pay_Rate list
    
    
# Define a function that calculates the salary 
def payroll(Hours_Worked, Pay_Rate):
    if Hours_Worked <= 40:
        Salary = (Pay_Rate * 40) 
    else:
        Salary = (Pay_Rate * 40) + (Hours_Worked - 40)*Pay_Rate*1.5
    return Salary

# Make a dictionary with Hours_Worked and Pay_Rate list    
Salary_dict = dict(zip(Hours_Worked, Pay_Rate)) 

# Calculate the salary using payroll function and put it as list
Salary_cal = []
for key, value in Salary_dict.items(): # loops through the big list (wines)
    Salary_cal.append(payroll(key , value ) )
    #return Salary_cal

    
# Make a dictionary with Employee's name as key and its salary as value   
Salary_Employee = dict(zip(Employee_Name, Salary_cal)) 

# Print the salary of each employee along thierr names
for key, value in Salary_Employee.items():
    print(f"Salary earned by {key} is ${value} ")


# In[ ]:




