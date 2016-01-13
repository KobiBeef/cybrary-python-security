import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
    # print "remove_letter"
    base_string = str(raw_input("enter string:> "))
    letter_remove = str(raw_input("enter letter to remove:> "))
    letter_remove = letter_remove[0]
    location = 0

    # reference pointer style
    if letter_remove in base_string:
        string_length = len(base_string)
        while location < string_length:
            if base_string[location] == letter_remove:
                base_string = base_string[:location] + base_string[location+1::]
                string_length -= 1
            location += 1

        print base_string

    # for letter in list_base_string:
    #     if letter == letter_remove:
    #         list_base_string.pop(letter_remove)
    #         print list_base_string
    
    return

def num_compare(): #Compare 2 numbers to determine the larger
    # print "num_compare"
    num_1 = int(raw_input("input first number:> "))
    num_2 = int(raw_input("input second number:> "))
    if num_1 > num_2:
        print "%d is greater than %d" % (num_1, num_2)
    elif num_2 > num_1 :
        print "%d is greater than %d" % (num_2, num_1)
    else:
        print "both numbers are equal"
    return

def print_string(): #Print the previously stored string
    # print "print_string"
    print saved_string
    return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
    # print "calculator"
    sign_dict = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}

    num_1 = int(raw_input("input first number:> "))
    operation = str(raw_input("input operator:> "))
    num_2 = int(raw_input("input second number:> "))

    # same magic as the "opt_list[opt_choice]()"
    print sign_dict[operation](num_1, num_2)

    # operation = sign_dict[operation]
    # result = operation(num_1, num_2)
    # print result
    
    # num_1 sign_dict[operator] num_2
    # if operator == "+":
    # 	print num1 + num_2
    # elif operator == "-":
    # 	print num1 - num_2
    # elif operator == "*":
    # 	print num_1 * num_2
    # elif operator == "/":
    # 	print num_1 / num_2

    return

def accept_and_store(): #Accept and store a string
    # print "accept_and_store"
    global saved_string
    saved_string = str(raw_input("input a string:> "))
    return

def main(): #menu goes here
    opt_list = [
    	accept_and_store, 
    	calculator, 
    	print_string, 
    	num_compare, 
    	remove_letter
    	]
    
    while True:
	    print "Select option"
	    print "1\taccept_and_store"
	    print "2\tcalculator"
	    print "3\tprint_string"
	    print "4\tnum_compare"
	    print "5\tremove_letter"
	    
	    opt_choice = int(raw_input("select an option:> "))
	    opt_choice -= 1
	    # this is new: dont know what's it called
	    # what i think it do is it concatenates or attaches the parentheses to the opt_list
	    opt_list[opt_choice]()
	    # test = opt_list[opt_choice]()
	    # test1 = opt_list[opt_choice]

	    # print test, type(test)
	    # print test1, type(test1)

    
    return 

main()
