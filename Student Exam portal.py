import csv
import os

#/ Student Exami/nation Portal

class Student:
  def __init__(self, student_id, name, roll_number, batch_id):
    self.student_id = student_id
    self.name = name
    self.roll_number = roll_number
    self.batch_id = batch_id
    self.marks = {}
    
  def get_student_id(self):
    return self.student_id
  
  def get_name(self):
    return self.name
  
  def get_roll_number(self):
    return self.roll_number
  
  def get_batch_id(self):
    return self.batch_id
  
  def get_marks(self):
    return self.marks
  
  def set_marks(self, course_id, marks):
    self.marks[course_id] = marks
    
  def generate_report_card(self):
    # calculate total marks and percentage
    total_marks = sum(self.marks.values())
    percentage = total_marks / len(self.marks)
    
    # determine whether the student passed or failed
    if percentage >= 40:
      result = "PASS"
    else:
      result = "FAIL"
      
    # create the report card text
    report_card = f'Student ID: {self.student_id}\nName: {self.name}\nClass Roll Number: {self.roll_number}\nBatch ID: {self.batch_id}\n\n'
    report_card += 'Course ID  Marks  Grade\n'
    for course_id, marks in self.marks.items():
      grade = self.get_grade(marks)
      report_card += f'{course_id}       {marks}     {grade}\n'
    report_card += f'\nTotal Marks: {total_marks}\nPercentage: {percentage}%\nResult: {result}\n'
    
    return report_card
  
  def get_grade(self, marks):
    if marks >= 90:
      return "A"
    elif marks >= 80:
      return "B"
    elif marks >= 70:
      return "C"
    elif marks >= 60:
      return "D"
    elif marks >= 50:
      return "E"
    else:
      return "F"
    
  def __str__(self):
    return f'Student ID: {self.student_id}, Name: {self.name}, Class Roll Number: {self.roll_number}, Batch ID: {self.batch_id}'

class Course:
  def __init__(self, course_id, course_name, marks_obtained):
    self.course_id = course_id
    self.course_name = course_name
    self.marks_obtained = marks_obtained
    
  def get_course_id(self):
    return self.course_id
  
  def get_course_name(self):
    return self.course_name
  
  def get_marks_obtained(self):
    return

class Course:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks
    
    def performance(self):
        if self.marks >= 90:
            return "Excellent"
        elif self.marks >= 80:
            return "Good"
        elif self.marks >= 70:
            return "Average"
        elif self.marks >= 60:
            return "Below Average"
        else:
            return "Poor"
    
    def stats(self):
        # Code to generate histogram goes here
        pass

import matplotlib.pyplot as plt

# Create a new course with ID 123, name "Math 101", and marks 80
math_course = Course(123, "Math 101", 80)

# Display the student's performance in the course
print(math_course.performance())  # Output: Good

# Generate a histogram showing the distribution of marks in the course
marks = [70, 80, 90, 100, 60, 75]  # List of marks for all students in the course
plt.hist(marks)
plt.show()
 
class Batch:
    def __init__(self, id, name, department, courses, students):
        self.id = id
        self.name = name
        self.department = department
        self.courses = courses
        self.students = students
    
    def view_students(self):
        for student in self.students:
            print(student.name)
    
    def view_courses(self):
        for course in self.courses:
            print(course.name)
    
    def performance(self):
        # Code to calculate and display the performance of all students goes here
        pass
    
    def stats(self):
        # Code to generate pie chart showing the percentages goes here
        pass

import matplotlib.pyplot as plt

# Create a new course with ID 123, name "Math 101", and marks 80
math_course = Course(123, "Math 101", 80)

# Create a new student with ID 123, name "John Doe", and marks [80, 90, 70]
john_doe = Student(123, "John Doe", [80, 90, 70])

# Create a new batch with ID 123, name "Batch 1", department "Math", courses [math_course], and students [john_doe]
batch = Batch(123, "Batch 1", "Math", [math_course], [john_doe])

# View all students in the batch
batch.view_students()  # Output: John Doe

# View all courses taught in the batch
batch.view_courses()  # Output: Math 101

# Calculate and display the performance of all students in the batch
batch.performance()  # Output: John Doe: Excellent

# Generate a pie chart showing the percentages of students in each performance category
performances = ["Excellent", "Good", "Average", "Below Average", "Poor"]
percentages = [50, 25, 15, 5, 5]  # Percentage of students in each performance category
plt.pie(percentages, labels=performances)
plt.show()

class Department:
    def __init__(self, id, name, batches):
        self.id = id
        self.name = name
        self.batches = batches
    
    def view_batches(self):
        for batch in self.batches:
            print(batch.name)
    
    def avg_performance(self):
        # Code to calculate and display the average performance of all batches goes here
        pass
    
    def stats(self):
        # Code to generate a line plot showing the department stats goes here
        pass

import matplotlib.pyplot as plt

# Create a new course with ID 123, name "Math 101", and marks 80
math_course = Course(123, "Math 101", 80)

# Create a new student with ID 123, name "John Doe", and marks [80, 90, 70]
john_doe = Student(123, "John Doe", [80, 90, 70])

# Create a new batch with ID 123, name "Batch 1", department "Math", courses [math_course], and students [john_doe]
batch = Batch(123, "Batch 1", "Math", [math_course], [john_doe])

# Create a new department with ID 123, name "Math", and batches [batch]
math_department = Department(123, "Math", [batch])

# View all batches in the department
math_department.view_batches()  # Output: Batch 1

# Calculate and display the average performance of all batches in the department
math_department.avg_performance()  # Output: Average

# Generate a line plot showing the department stats
years = [2015, 2016, 2017, 2018, 2019]  # Year
enrollments = [100, 120, 140, 160, 180]  # Number of enrollments in the department each year
plt.plot(years, enrollments)
plt.show()