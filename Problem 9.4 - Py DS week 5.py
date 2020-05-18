# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name:")
address = open(fname)
counts = dict()

for line in address:
    if line.startswith('From '):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

max_addr = None
max_count = None
for k,v in counts.items():
    if max_count is None or v > max_count:
        max_addr = k
        max_count = v

print (max_addr, max_count)