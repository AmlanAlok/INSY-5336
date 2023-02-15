
def average(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


if __name__ == '__main__':
    # arbitrary arguments
    # result = average(1, 2, 3, 4, 5)
    # print("The average is:", result)

    dict1 = {1: 'A', 2: 'B', 3: 'C'}

    # List of the keys
    keysList = list(dict1.keys())
    print(keysList)