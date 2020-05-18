# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name / directory:")
rom  = open(fname)
extr_list = []

for line in rom:
    line.rstrip()
    words = line.split()
    for word in words:
        if word not in extr_list:
            extr_list.append(word)
extr_list.sort()
print(extr_list)