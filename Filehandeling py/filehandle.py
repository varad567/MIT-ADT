import json
import csv

student_file = open(r"D:\Cohert 2\Polymorphism\student.json", 'r')
student_data = json.load(student_file)
student_file.close()

csv_file = open(r"D:\Cohert 2\Polymorphism\students.csv", 'w', newline='')
header = student_data[0].keys()
csv_writer = csv.DictWriter(csv_file, fieldnames=header) 

csv_writer.writeheader()
csv_writer.writerows(student_data)
csv_file.close()

print("Data has been successfully converted from JSON to CSV.")