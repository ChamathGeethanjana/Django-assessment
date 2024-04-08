import csv
from .models import Student,School,Class,Answer

# CSV file paths
csv_file1 = './ganison_dataset_1.csv'
csv_file2 = './ganison_dataset_2.csv'
csv_file3 = './ganison_dataset_3.csv'
csv_file4 = './ganison_dataset_4.csv'
csv_file5 = './ganison_dataset_5.csv'
csv_file6 = './ganison_dataset_6.csv'

def process_csv_file(csv_file1):
    with open(csv_file1, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract data based on your model fields
            first_name = row['First Name']
            last_name = row['Last Name']
            school_name = row['school_name']
            class_name = row['Class']
            answer = row['Answers']
            
            #enter school datata to school table
            sch_data_object = School(name = school_name)
            sch_data_object.save()
            
            
            #enter student datata to student table
            stu_data_object = Student(full_name = first_name +" " + last_name)
            stu_data_object.save()
            
            #enter class datata to class table
            class_data_object = Class(class_name = class_name)
            class_data_object.save()
            
            #enter answer datata to answer table
            answer_data_object = Answer(answer = answer)
            answer_data_object.save()
            
            
#run function with appropriate csv file name
process_csv_file(csv_file1)