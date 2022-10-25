# a = open('new.txt', 'r')
# Python code to illustrate with() alongwith write()
# with open("new.txt", "w") as f:
# 	f.write("Hello World!!!")

# Python code to illustrate split() function
with open("new.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)
