file = 'python_text.txt'

# reading a file by adding it to an empty list line by line (can be printed without list too)
lines = []
with open(file) as opened_file:
	for line in opened_file:
		lines.append(line.strip())
for line in lines:
	print(line)

# reading a file by reading it as a whole
with open(file) as open_file2:
	print(open_file2.read())

# reading a file by looping over the lines
with open(file) as open_file3:
	list_of_lines = open_file3.readlines()
	for line in list_of_lines:
		print(line.strip())

# replacing a word in the original file
with open(file) as open_file4:
	lines2 = open_file4.readlines()

for line in lines2:
	line = line.strip()
	line = line.replace('Python', 'PHP')
	print(line)

# writing text and numbers to a new file
new_file = 'text_file_creation.txt'
text_to_add = "Hello there!\nWelcome to the new file.\nYour code is: "
numbers_to_add = 9876543210
numbers_string = str(numbers_to_add)
text_to_add += numbers_string

with open(new_file, 'w') as file_object:
	file_object.write(text_to_add)

# adding (appending) a line to the new file without overwriting the whole file
extra_line = "\nDon't forget to keep your code safe."
with open(new_file, 'a') as file_object:
	file_object.write(extra_line)