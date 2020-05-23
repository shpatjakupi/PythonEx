import csv

def print_file_content(file):
    with open(file) as file_object:
        print(file_object.read())

def write_list_to_file(output_file, *lst):
    with open(output_file, 'w') as file_object:
        for s in lst:
            file_object.write(s + '\n')

def write_list2_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for s in lst:
            file_object.write(s + '\n')

def read_csv(input_file):
    l = []
    with open(input_file) as file_object:
        reader = csv.reader(file_object)
        for row in list(reader):
            l.append(row[0])
    return l