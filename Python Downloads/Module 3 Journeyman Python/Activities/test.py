from JourneymanActivities import *


def journeyman2test(final_num):
	# has 2 variations:
	# its either you include 0
	# or you exclude 0
	num1 = 0
	num2 = 0
	num_range = []
	num_sum = []

	while num1 < final_num:
		# this includes 0
		num1 += 1
		num_range.append(num1)
		# this excludes 0
		# num1 += 1

	for i in num_range:
		num2 += i

	num_sum.append(num2)
	print num_sum
	return num_sum[0]

test_var1 = 10
y = range(10)
print y

x = sum(range(test_var1))
print x
if x == journeyman2test(test_var1):
	print "True"
else:
	print "False"

# fout = open('output.txt', 'r+')
# print fout
# line1 = "this is a test"
# fout.write(line1)
# line2 = "this is a test 2"
# fout.write(line2)

# working_list = ['a', 'c', 'd', 'e']
# print working_list

def journeyman1test():
	str_list_list = [
					['a','b','c','d','e'] ,
	                ['this' , 'is' , 'a' , 'chimpanzee' , 'test'] ,
	                ['item1' , 'item2' , 'item3' , 'item4' , 'item5']
	                ]

	integer_list = [1]
	
	journeyman1(str_list_list[0] , integer_list[0])
	test = open(str_list_list[0][integer_list[0]])
	test = test.read()
	print test
	return 

# test2()

str_list = ['a','b','c','d','e']
item = 1

def journeyman1activity(str_list, item):
	filename = str_list[item]
	f = open(filename, "w+")
	for i in str_list:
		if i != str_list[item]:
			f.write(i)
	f.close
	return

# print type(test1(str_list, item))
# test1(str_list, item)

# import sys
# for i in sys.argv:
# 	print i
