


#Advent of code day 1 2024
#import pandas as pd
import heapq

#df = pd.read_csv('day1Iput.csv')

#list1, list2 = df[0], df[1]

import heapq

def listDistance(list1, list2)-> int:
    sum = 0

    while list1 and list2:
        val1, val2 = heapq.heappop(list1), heapq.heappop(list2)
        difference = abs(val1 - val2)
        sum += difference

    return sum


def main():
    #1, 5, 7, 8, 9
    #1, 2, 5, 6, 7
    #0, 3, 2, 2, 2
    list1 = [9, 8, 5, 7, 1]
    list2 = [5, 6, 1, 2, 7]
    val = listDistance(list1= list1, list2= list2)
    print("Difference vale is: ", val)

if __name__ == "__main__":
    main()


