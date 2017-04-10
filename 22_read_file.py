"""
Given (nameslist.txt) has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 

Extra:
* Instead of using the .txt file from above (or instead of, if you want the challenge), take (Training_01.txt), and count how many of each “category” of each image there are. 
This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. 
Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. 
To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.
"""

names = {}
with open("nameslist.txt", 'r') as work_file:
    for line in work_file:
        temp = line.strip()

        if temp not in names:
            names[temp] = 1
        else:
            names[temp] += 1

print(names)

categories = {}
with open("Training_01.txt", 'r') as extra_file:
    for line in extra_file:
        temp = line.split("/")

        if temp[2] not in categories:
            categories[temp[2]] = 1
        else:
            categories[temp[2]] += 1

print(categories)