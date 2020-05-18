fname = input("Enter file name: ")
chuck = open(fname)

for line in chuck:
    line = line.rstrip()
    line = line.upper()
    print(line)