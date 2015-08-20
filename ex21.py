from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file) 

#######NOTES##############
#each time 'print_a_line' is run you are paa=ssing a variable 'current_line' 
# the "f" in the print_all is a file
#each time you do f.seek(0) you are moving to the start of the file.
#each time you do f.readline() you are reading a line form the file and moving the read head to right after the '\n' that ends that file.
  
#************REVISIT*******************
