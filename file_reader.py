file_name = 'text_example.txt'
file_path = 'C:\\Users\\Casper\\Documents\\python_work\\text_files_example' # this is the path used when specified method is used
non_existing_file = 'non_existing_file.txt'

# opening and reading a text file in the same directory
with open(file_name) as text_file1:
    text_in_file = text_file1.read()
print(text_in_file.rstrip())

# opening and reading a text file in a subfoler in the same directory
with open(f'text_files_example/{file_name}') as text_file2:
    text_in_file = text_file2.read()
print(text_in_file.rstrip())

# opening and reading a text file in a specified directory
with open(f'{file_path}\\{file_name}') as text_file3:
    text_in_file = text_file3.read()
print(text_in_file.rstrip())

# printing each line separately, with hyphen for clarity
with open(file_name) as text_file1:
    for line in text_file1:
        print(f' - {line.rstrip()}')

# making list of lines
lines = []
with open(file_name) as text_file1:
    for line in text_file1:
        lines.append(line.rstrip())
print(lines)
print(lines[0]) # to print a specific line

# making list of lines using .readlines() command
with open(file_name) as text_file2:
    lines2 = text_file2.readlines()
print(lines2)
for line in lines2:
    print(line.rstrip())

# reconstructing the file line by line
with open(file_name) as text_file2:
    lines2 = text_file2.readlines()
full_text = ''
for line in lines2:
    full_text += line                   # as the original
for line in lines2:
    full_text += line.rstrip() + ' '    # without line breaks
print(full_text)
print(len(full_text))

# inbouwen dat een bestand niet wordt gevonden
try:
    with open(non_existing_file) as f:
        text_in_file = f.read()
except:
    print("File not found!")
else:
    print(text_in_file)