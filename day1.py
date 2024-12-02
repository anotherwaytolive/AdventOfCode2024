


#Advent of code day 1 2024

import csv
import heapq

def listDistance(list1, list2)-> int:
    sum = 0
    heapq.heapify(list1)
    heapq.heapify(list2)

    while list1 and list2:
        val1, val2 = heapq.heappop(list1), heapq.heappop(list2)
        difference = abs(val1 - val2)
        sum += difference

    return sum


def main():
    # Read the CSV file and extract columns
    with open('day1Input.csv', mode='r') as file:
        reader = csv.DictReader(file)
        columns = list(zip(*reader))

    # Debug: Print columns to inspect raw data
    print("Raw Columns:", columns)

    # Convert columns to lists of integers, handling spaces
    try:
        columns_as_lists = [
            list(map(lambda x: int(x.strip()), column)) for column in columns
        ]
    except ValueError as e:
        print(f"Error converting data to integers: {e}")
        return

    # Ensure there are at least two columns to compare
    if len(columns_as_lists) < 2:
        print("Error: Not enough columns in the CSV file.")
        return

    # Get the first two columns
    list1, list2 = columns_as_lists[0], columns_as_lists[1]

    # Calculate and display the distance
    result = listDistance(list1, list2)
    print(f"The total distance between the lists is: {result}")

if __name__ == "__main__":
    main()


