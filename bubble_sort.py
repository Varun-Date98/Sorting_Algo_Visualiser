from typing import List


def bubbleSortForward(array, display):
    display.setCaption("Forwards Bubble Sort")

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]

            display.show(array)

    display.exit()


def backwardsBubbleSort(array, display):
    display.setCaption("Backwards Bubble Sort")

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            display.show(array)

    display.exit()
