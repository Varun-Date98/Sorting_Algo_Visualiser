from bubble_sort import backwardsBubbleSort, bubbleSortForward
from display import MyDisplay

myDisplay = MyDisplay()
array = [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]
bubbleSortForward(array[:], myDisplay)

myDisplay = MyDisplay()
backwardsBubbleSort(array[:], myDisplay)
