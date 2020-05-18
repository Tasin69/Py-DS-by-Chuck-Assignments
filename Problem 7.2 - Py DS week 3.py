# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")              #Accesing the file and storing the file handle in data
data = open(fname)
count = 0
x = 0

for line in data:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):   #Searching our desired value (which is currently a string) and converting it to our
        x += float(line[-6:])                    #                                                   desired data type (here, float)
        count += 1                               #Performing our calculation to find out the mean
avg = x / count
print(avg)