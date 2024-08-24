import pandas as pd
import keyboard
import csv


class Sms:
    def __init__(self):
        self.student = []

    def load(self):
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    print("Interrupted")
                    break
                data_name = input("Name of file: ").strip()
                with open(data_name,'r') as file:
                    csv_reader = csv.DictReader(file)
                    self.student = [row for row in csv_reader]
                    print("Loaded successfully.")
                    break
            except ValueError:
                print("No such file.")

    def read(self):
        print(f"Information: {self.student}")

    def table(self):
        return pd.DataFrame(self.student)
    
    def create(self):
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    print("Intrupted.")
                    break
                int_num = int(input("How many students? "))
                if 0 < int_num < 50:
                    break
            except ValueError:
                    print("Number of input shold be between 0 and 50")
        for _ in range(int_num):
            if keyboard.is_pressed('esc'):
                self.student = []
                break
            while True:
                name = input("Name: ").strip()
                if not name.isalpha():
                    print("Enter name: ")
                    continue
                else:
                    break
            if keyboard.is_pressed('esc'):
                self.student = []
                break
            while True:
                try:
                    studen_id = int(input("Student ID: "))
                    if 0 < studen_id < 100:
                        break
                except ValueError:
                    print("Enter only numbers between 0 and 100")

            if keyboard.is_pressed('esc'):
                self.student = []
                print("Interrupted.")
                break
            while True:
                try:
                    age = int(input("Age: "))
                    if 7 <= age < 18:
                        break
                except ValueError:
                    print("Age must be between 7 and 17.")
            if keyboard.is_pressed('esc'):
                self.student = []
                print("Interrupted")
                break
            while True:
                try:
                    class_num = int(input("Class number: "))
                    if 0 < class_num < 10:
                        break
                except ValueError:
                    print("The number of classes must be between 1 and 9")
            if keyboard.is_pressed('esc'):
                print('Interupted.')
                self.student = []
                break
            while True:
                try:
                    grades_1 = input("Enter the grades by space: ").split()
                    grades = list(map(int, grades_1))
                    average = sum(grades) / len(grades)
                    break
                except ValueError:
                    print("Enter list of numbers.")
                    

            new_list = {
                'name': name,
                'student_id': studen_id,
                'age': age,
                'class_num': class_num,
                'grades': grades,
                'average': average
            }
            self.student.append(new_list)
        print("Student(s) information added.")

    def update(self):
        num_of_update = int(input("How many students to update? "))
        
        for _ in range(num_of_update):
            while True:
                update_name = input("Enter name to update: ").strip()
                if update_name.isalpha():
                    break
                else:
                    print("Enter a valid name: ")

            for name in self.student:
                if name['name'] == update_name:
                    while True:
                        try:
                            student_id = int(input("Student ID: "))
                            if 0 < student_id < 100:
                                break
                        except ValueError:
                            print("Enter only numbers between 0 and 100")

                    while True:
                        try:
                            age = int(input("Age: "))
                            if 7 <= age < 18:
                                break
                        except ValueError:
                            print("Age must be between 7 and 17.")

                    while True:
                        try:
                            class_num = int(input("Class number: "))
                            if 1 <= class_num <= 9:
                                break
                        except ValueError:
                            print("The number of classes must be between 1 and 9")

                    while True:
                        try:
                            grades_1 = input("Enter the grades by space: ").split()
                            grades = list(map(int, grades_1))
                            average = sum(grades) / len(grades)
                            break
                        except ValueError:
                            print("Enter a list of numbers.")

                    name['name'] = update_name
                    name['student_id'] = student_id
                    name['age'] = age
                    name['class_num'] = class_num
                    name['grades'] = grades
                    name['average'] = average

                    if keyboard.is_pressed('esc'):
                        print("Interrupted.")
                        self.student = []
                        return
                    
    def delete(self):
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    print("Interrupted.")
                    break
                name_to_delete = input("Name to delete: ").strip()
                if not name_to_delete.isalpha():
                    print("ENter name")
                    continue
                else:
                    for name in self.student:
                        if name['name'] == name_to_delete:
                            self.student.remove(name)
                    print("Name daleted successfully.")
            except ValueError:
                print("Invalid input.")

    def add_grades(self):
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    print("Interrupted.")
                    break
                name_to_add_grades = input("Enter name to add grades: ").strip()
                if not name_to_add_grades.isalpha():
                    print("Enter name")
                    continue
                for student in self.student:
                    if student['name'] == name_to_add_grades:
                        try:
                            grades_input = input("Add grades separated by space: ").split()
                            grades_to_add = list(map(int, grades_input))
                            student['grades'].extend(grades_to_add)
                            student['average'] = sum(student['grades']) / len(student['grades'])
                            print("New grades added successfully.")
                        except ValueError:
                            print("Invalid input. Please enter integers only.")
                        break
                else:
                    print("Student not found.")
            except ValueError:
                print("Invalid input.")

    def remove(self):
        while True:
            rem = input("Are you sure to remve? Y/N ").strip()
            if not rem.isalpha():
                print("Enter 'Y/N'")
                continue
            else:
                try:
                    if rem == 'Y':
                        self.student = []
                        print("Data removed successfully.")
                        print("There is no data.")
                        break
                    elif rem == 'N':
                        print("Data did not remove.")
                        break
                except ValueError:
                    print("Enter 'Y/N' ")

    def search(self):
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    print("Interrupted.")
                    break
                search_name = input("Enter name to search: ").strip()
                if not search_name.isalpha():
                    print("Enter name: ")
                    continue

                for name in self.student:
                    if name['name'] == search_name:
                        print("Student details: ")
                        print(f"Name: {name['name']}")
                        print(f"Student ID: {name['student_id']}")
                        print(f"Age: {name['age']}")
                        print(f"Class number: {name['class_num']}")
                        print(f"Grades: {name['grades']}")
                        print(f"Average: {name['average']}")
                        return
                print("Not found")
                break
            except ValueError:
                print("Invalid input")

    def save_as_csv(self, filename='savefile.csv'):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name','student_id','age','class_num','grades','average'])
            writer.writeheader()
            for i in self.student:
                writer.writerow(i)
            print("Saved successfully. name='savefile'")

def menu():
    sms =Sms()
    while True:
        print("Welcome to Student Management System: ")
        print("1. Load data in CSV format")
        print("2. Display information")
        print("3. Display as a table.")
        print("4. Add new students.")
        print("5. Update student information")
        print("Delete a student.")
        print("7. Add grades.")
        print("8. Search.")
        print("9. Save as CSV format.")
        print("10. Remove all data.")
        print("11. Exit.")
        choose_numbers = input("Enter your choice: ").strip()
        if choose_numbers == '1':
            sms.load()
        elif choose_numbers == '2':
            sms.read()
        elif choose_numbers == '3':
            print(sms.table())
        elif choose_numbers == '4':
            sms.create()
        elif choose_numbers == '5':
            sms.update()
        elif choose_numbers == '6':
            sms.delete()
        elif choose_numbers == '7':
            sms.add_grades()
        elif choose_numbers == '8':
            sms.search()
        elif choose_numbers == '9':
            sms.save_as_csv()
        elif choose_numbers == '10':
            sms.remove()
        elif choose_numbers == '11':
            print("Exiting...")
            break
        else:
            print("Invalid number. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    menu()