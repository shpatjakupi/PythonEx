import os

def write_foldercontent_to_file(path, outputfile):
    with open(outputfile, 'w') as file_object:
        for s in os.listdir(path):
            file_object.write(path + s + '\n')

def write_foldercontent_to_file_with_dir(folder, outputfile):
    with open(outputfile, 'w') as file_object:
        for path,dirs,files in os.walk(folder):
            for filename in files:
                file_object.write(os.path.join(path, filename) + '\n')

def print_firstline_of_files(list_of_filenames):
    for filename in list_of_filenames:
        with open(filename, 'r') as file_object:
            print(file_object.readline())

def print_emails_of_files(list_of_filenames):
     for filename in list_of_filenames:
            with open(filename, 'r') as file_object:
                for line in file_object:
                    if '@' in line:
                        print(line)   

def print_header_of_files(list_of_filenames):
     for filename in list_of_filenames:
            with open(filename, 'r') as file_object:
                for line in file_object:
                    if line.startswith('#'):
                        print(line) 