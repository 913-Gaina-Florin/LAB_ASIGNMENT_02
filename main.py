from random import randint


def stooge_sort(arr, left, right, cnt, step):
    if left >= right:
        return

    if cnt % step == 0:
        print(arr)

    if arr[left] > arr[right]:
        aux = arr[left]
        arr[left] = arr[right]
        arr[right] = aux

    n = int(right - left + 1)
    dif = n // 3
    if n > 2:
        stooge_sort(arr, left, right - dif, cnt + 1, step)
        stooge_sort(arr, left + dif, right, cnt + 1, step)
        stooge_sort(arr, left, right - dif, cnt + 1, step)


def selection_sort(arr, left, right, step):
    for index in range(left, right):
        min_val = arr[index]
        min_index = index
        for i in range(index, right + 1):
            if arr[i] < min_val:
                min_val = arr[i]
                min_index = i
        arr[index], arr[min_index] = arr[min_index], arr[index]
        if index % step == 0:
            print(arr)


def generate(arr):
    for i in range(100):
        arr.append(randint(0, 100))


def options():
    print("1 - Generate a random sequence of numbers. ")
    print("2 - Sort the sequence using stooge sort. ")
    print("3 - Sort the sequence using selection sort. ")
    print("0 - Exit the program. ")


def options2():
    print("2 - Sort the sequence using stooge sort. ")
    print("3 - Sort the sequence using selection sort. ")
    print("0 - Exit the program. ")


def read():
    n = input("Enter your option: ")
    return n


def main_function():
    options()
    n = read()

    if n == "0":
        return
    elif n == "1":
        arr = []
        generate(arr)
        print("Your sequence has been successfully generated. ")
        options2()
        n = read()
        if n == "0":
            return
        elif n == "2":
            step = int(input("Enter your step: "))
            stooge_sort(arr, 0, len(arr) - 1, 0, step)
        elif n == "3":
            step = int(input("Enter your step: "))
            selection_sort(arr, 0, len(arr) - 1, step)
        elif n == "0":
            return
    elif n == "2" or n == "3":
        arr = []
        print(arr)
        return
    else:
        print("This option does not exist. ")
        return

    print(arr)


main_function()
