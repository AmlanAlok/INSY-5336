
def average(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


if __name__ == '__main__':
    x = 2

    if x == 1:
        print(True)
    else:
        None