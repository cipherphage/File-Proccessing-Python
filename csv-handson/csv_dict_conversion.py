import csv

def csv2dict(filename):
    # open file and create DictReader object
    # use the DictReader to get data and 
    # add data to a variable named data_list
    with open(filename, newline='') as infile:
        reader = csv.DictReader(infile)
        return list(reader)

def dict2csv(filename, fieldnames, data):
    # open file and create DictWriter object
    # use the DictWriter to write csv data 
    # to file
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():

    # test csv to dict conversion
    student_data_file = "student_data.csv"
    data_dict = csv2dict(student_data_file)
    print(data_dict)

    # test result
    expected_dict = [
        {'date': '3/12', 
        'student': 'Cindy Who', 
        'class': 'English1', 
        'teacher': 'Brown', 
        'grade': None}, 
        {'date': '3/12', 
        'student': 'Charlie Brown', 
        'class': 'English1', 
        'teacher': 'Brown', 
        'grade': None}, 
        {'date': '3/12', 
        'student': 'Melvin Arnold', 
        'class': 'English', 
        'teacher': 'Brown', 
        'grade': None}, 
        {'date': '3/12', 
        'student': 'Jennifer Buckle', 
        'class': 'English1', 
        'teacher': 'Brown', 
        'grade': None}, 
        {'date': '3/12', 
        'student': 'Peppermint Patty',
        'class': 'English1', 
        'teacher': 'Brown', 
        'grade': None}
    ]
    assert data_dict == expected_dict, "the returned data does not match the expected dict"

    # test dict to csv conversion
    filename = "student_grades.csv"
    fieldnames = ["date", "student", "class", "teacher", "grade"]

    # add grades to simulate grades added by teacher
    for item in data_dict:
        item["grade"] = "A"

    dict2csv(filename, fieldnames, data_dict)

    # test result
    with open("student_grades.csv", "r") as infile:
        check_data = infile.read()
        print(check_data)
    expected_data = """date,student,class,teacher,grade\n3/12,Cindy Who,English1,Brown,A\n3/12,Charlie Brown,English1,Brown,A\n3/12,Melvin Arnold,English,Brown,A\n3/12,Jennifer Buckle,English1,Brown,A\n3/12,Peppermint Patty,English1,Brown,A\n"""
    assert check_data == expected_data, "the written data does not match the expected data"

if __name__ == "__main__":
    main()