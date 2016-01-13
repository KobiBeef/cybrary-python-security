from JourneymanActivities import *
import os

def journeymantest1():
    str_list_list = [
                    ['a','b','c','d','e'] ,
                    ['this' , 'is' , 'a' , 'chimpanzee' , 'test'] ,
                    ['item1' , 'item2' , 'item3' , 'item4' , 'item5']
                    ]
    integer_list = [1,3,0]
    for i in range(len(str_list_list)):
        # range(len(str_list_list))
        # x = len(str_list_list)
        # x = 3
        # i = range(x)
        # i = [0, 1, 2]
        # i[0] = ['a','b','c','d','e']
        # i[1] = ['this' , 'is' , 'a' , 'chimpanzee' , 'test']
        # i[2] = ['item1' , 'item2' , 'item3' , 'item4' , 'item5']

        # for i in range(len(str_list_list))
            # i = str_list_list[0, 1, 2]
            # i @ init_iter[0]: i[0] = ['a', 'b', 'c', 'd', 'e']

        working_list = []
        for item in str_list_list[i]:
            # i = init_iter[0]
            # str_list_list[i] = ['a','b','c','d','e']
            # item = init_item['a']++
            
            working_list.append(item)
            # append all items in working_list[]
            # i[0]: working_list = ['a','b','c','d','e']

        journeyman1(str_list_list[i] , integer_list[i])
        # this function creates the files
        # journeyman1(i[0]: init_iter[i] = ['a', 'b', 'c', 'd', 'e'], i[0]:iniger_list[i] = 1)

        f = open(str_list_list[i][integer_list[i]])
        # this opens the file b.file
        # f = open(str_list_list[][])
        # str_list_list = [
        #                 ['a','b','c','d','e'] , -> i[0]
        #                 ['this' , 'is' , 'a' , 'chimpanzee' , 'test'] , -> i[1]
        #                 ['item1' , 'item2' , 'item3' , 'item4' , 'item5'] -> i[2]
        #                 ]
        #               i[0], i[1], i[2]
        # integer_list = [1,    3,    0]
        # f = 'b'
        working_list.remove(working_list[integer_list[i]])
        # working_list = ['a','c','d','e']

        for j in range(4):
            # range(4) = [0, 1, 2, 3]
            line = f.read(len(working_list[j]))
            # reads the 4 items in working_list[j]
            if line != working_list[j]:
                # checks whether each line string is equal with each working_list[j] string
                print "Failed: %s != %s" % (line , working_list[j])
                return -1
            print line
        print "\n"
        f.close()
        os.remove(str_list_list[i][integer_list[i]])
        # this function removes the created file[i]
    print "Test 1: SUCCESS\n"
    return 0

def journeymantest2():
    max_list = [10,4,1000,35]
    for i in max_list:
        if journeyman2(i) != sum(range(i+1)):
            print "Failed: %d != %d" % (journeyman2(i) , sum(range(i+1)))
            return -1
        print "%d\t:\t%d" % (i , journeyman2(i))
    print "Test 2: SUCCESS\n"
    return 0

def journeymantest3():
    message_list = ['alpha' , 'bravo' , 'charlie' , 'delta']
    
    for i in message_list:
        res = journeyman3()
        if res != i:
            print "Failed: %s != %s" % (res , i)
            return -1
        print res
    print "Test 3: SUCCESS\n"

def journeymantest4():
    journeyman4()

def main():
    journeymantest1()
    journeymantest2()
    # journeymantest3()
    journeymantest4()

main()