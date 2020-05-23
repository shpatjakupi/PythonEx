#Create a python file with 3 functions:
#def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    with open(file) as file_object:
        print(file_object.read())

#def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file

def write_list_to_file(output_file, *lst):
    with open(output_file, 'w') as file_object:
        for s in lst:
            file_object.write(s + '\n')
#rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list2_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for s in lst:
            file_object.write(s + '\n'
#def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    l = []
    with open(input_file) as file_object:
        reader = csv.reader(file_object)
        for row in list(reader):
            l.append(row[0])
    return l
