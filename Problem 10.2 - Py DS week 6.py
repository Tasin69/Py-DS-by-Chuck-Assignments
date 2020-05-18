# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name:")
data = open(fname)
hour_dict = dict()

for line in data:
    if line.endswith('2008\n'):
        temp_list = line.split()
        time = temp_list[-2].split(':')
        hour_dict[time[0]] = hour_dict.get(time[0], 0) + 1

sorted_hour = sorted(hour_dict.items())
for k,v in sorted_hour:
    print(k, int(v/2))