# Basic Statistics Calculator
# by itsmekamp
# c.2018
# I actually made this code for my homework
# Because im lazy, i made this code to do my homework

import statistics
import math

itemlist = [] #List of integers
inpl = [] #Input list for splitting input

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

def find_mode(items):
    buffer = 0
    final = []
    items_unique = list(sorted(set(items)))
    for item in items_unique:
        if items_unique.count(item) >= buffer:
            buffer = items_unique.count(item)
            final.append(item)
        else:
            continue
    return final

def findMedianIndex(items):
    final = []
    if len(items) % 2 == 0:
        final.append(items[int(len(items) / 2 - 1)])
        final.append(items[int(len(items) / 2)])
        return final
    else:
        final.append(int(math.ceil(len(items) / 2)-1))
        return final

def quartile1(items):
    oddlist = []
    templist = items
    templist.sort()
    index = findMedianIndex(templist)
    if len(templist) % 2 == 0:
        for item in items:
            if item == index[0]:
                pass
            elif item == index[1]:
                pass
            else:
                oddlist.append(item)
        oddlist.insert(int(len(templist)/2-1), statistics.median(templist))
        q1 = oddlist[int(math.ceil(len(templist)/4)-1)]
    else:
        q1 = templist[int(math.ceil(len(templist) / 4) - 1)]
    return q1
def quartile2(items):
    return statistics.median(items)

def quartile3(items):
    oddlist = []
    templist = items
    templist.sort()
    index = findMedianIndex(templist)
    if len(templist) % 2 == 0:
        for item in items:
            if item == index[0]:
                pass
            elif item == index[1]:
                pass
            else:
                oddlist.append(item)
        oddlist.insert(int(len(templist) / 2 - 1), statistics.median(templist))
        q3 = int(oddlist[int(math.ceil(len(templist) / 4) * 3 - 1)])
    else:
        q3 = int(templist[int(math.ceil(len(templist) / 4) * 3 - 1)])
    return q3
def listrange(items):
    biggest = 0
    smallest = 0
    smallestIs0 = True
    for item in itemlist:
        if smallestIs0:
            if item > smallest:
                smallest = item
                smallestIs0 = False
            elif item >= biggest:
                biggest = item
            else:
                pass
        else:
            if item <= smallest:
                smallest = item
            elif item >= biggest:
                biggest = item
            else:
                pass
    return biggest - smallest

def interquartile_range(items):
    return quartile3(items) - quartile1(items)



while True:
    print("Enter number")
    inp = input("")
    if inp.startswith("get"):
        inpl = inp.split(" ")
        out = inpl[1]
        try:
            testout = int(out)
            print(itemlist.count(testout))
        except ValueError:
            print("ERROR: Input is not an integer")
    elif inp == "sort":
        templist = itemlist
        templist.sort()
        print(templist)
    elif inp == "invsort":
        templist = itemlist
        templist.sort()
        print(templist[::-1])
    elif inp == "show":
        print(*itemlist, sep=", ")
    elif inp == "quartile1":
        print(quartile1(itemlist))
    elif inp == "quartile2":
        print(quartile2(itemlist))
    elif inp == "quartile3":
        print(quartile3(itemlist))
    elif inp == "range":
        biggest = 0
        smallest = 0
        smallestIs0 = True
        for item in itemlist:
            if smallestIs0 == True:
                if item > smallest:
                    smallest = item
                    smallestIs0 = False
                elif item >= biggest:
                    biggest = item
                else:
                    pass
            else:
                if item <= smallest:
                    smallest = item
                elif item >= biggest:
                    biggest = item
                else:
                    pass
        print(str(biggest) + " - " + str(smallest))
        print(listrange(itemlist))
    elif inp == "quartilerange":
        print(str(quartile3(itemlist)) + " - " + str(quartile1(itemlist)))
        print(interquartile_range(itemlist))
    elif inp == "mean":
        print(*itemlist, sep=" + ")
        print(str(sum_list(itemlist)) + " / " + str(len(itemlist)))
        print(statistics.mean(itemlist))
    elif inp == "median":
        templist = itemlist
        templist.sort()
        print(*templist, sep=", ")
        if statistics.median(itemlist) % 2:
            print(str(itemlist[int(len(itemlist)/2)-1]) + " + " + str(itemlist[int(len(itemlist)/2)]) + " / 2")
        print(statistics.median(itemlist))
    elif inp == "mode":
        print(*find_mode(itemlist), sep=", ")
    elif inp == "reset":
        itemlist = []
    elif inp == "x":
        break;
    else:
        try:
            testinp = int(inp)
            itemlist.append(testinp)
        except ValueError:
            print("ERROR: Input is not an integer")