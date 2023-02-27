from tkinter import *
from tkinter import ttk
import numpy as np
import time

global comparisons
comparisons = 0
global arrayAccesses
arrayAccesses = 0

def show(n: int, data: list, colours: list):
    canvas.delete('all')
    comparisonsVar.set("Comparisons: "+str(comparisons))
    arrayAccessesVar.set("Array accesses: "+str(arrayAccesses))
    width = 1560/(3*n-1)
    gap = width/2
    for i in range(n):
        canvas.create_rectangle(7+i*width+i*gap, 0, 7 +
                                (i+1)*width+i*gap, data[i],
                                fill=colours[i])
        
    win.update_idletasks()


def shuffle():
    global isSorted
    global comparisons
    global arrayAccesses
    comparisons = 0
    arrayAccesses = 0
    win.title('Sorting visualizer')
    mainText.config(text='Sorting visualizer')
    np.random.shuffle(arr)
    show(N, arr, color)
    isSorted = False


def mergesort(arr, left, right):
    global comparisons
    global arrayAccesses

    if left < right:
        comparisons += 1
        m = (left+right)//2
        mergesort(arr, left, m)
        mergesort(arr, m+1, right)

        j = m+1
        if arr[m] <= arr[m+1]:
            comparisons += 1
            arrayAccesses += 1
            return

        while left <= m and j <= right:
            comparisons += 1
            show(N, arr, ['blue' if x == left or x ==
                          j else 'grey' for x in range(N)])
            if speed != "No wait":
                time.sleep(1/speed)
            if arr[left] <= arr[j]:
                comparisons += 1
                arrayAccesses += 1
                left += 1
            else:
                show(N, arr, ['red' if x == left or x ==
                              j else 'grey' for x in range(N)])

                if speed != "No wait":
                    time.sleep(1/speed)
                temp = arr[j]
                arrayAccesses += 1

                i = j
                while i != left:
                    comparisons += 1
                    arr[i] = arr[i-1]
                    arrayAccesses += 1
                    show(N, arr, ['red' if x == i or x ==
                                  j else 'grey' for x in range(N)])
                    if speed != "No wait":
                        time.sleep(1/speed)
                    i -= 1

                arr[left] = temp
                arrayAccesses += 1
                show(N, arr, ['green' if x == left or x ==
                              j else 'grey' for x in range(N)])
                if speed != "No wait":
                    time.sleep(1/speed)
                left += 1
                m += 1
                j += 1


def bubbleSort(arr):
    global comparisons
    global arrayAccesses

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                comparisons += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arrayAccesses += 2
                show(N, arr, ['blue' if x == j or x ==
                              j+1 else 'grey' for x in range(N)])
                if speed != "No wait":
                    time.sleep(1/speed)


def quickSort(arr, low, high):
    global comparisons
    global arrayAccesses

    if low < high:
        comparisons += 1
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def partition(arr, low, high):
    global comparisons
    global arrayAccesses

    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            comparisons += 1
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            arrayAccesses += 2
            show(N, arr, ['blue' if x == j or x ==
                          i else 'grey' for x in range(N)])
            if speed != "No wait":
                time.sleep(1/speed)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    arrayAccesses += 2
    show(N, arr, ['blue' if x == i+1 or x ==
                  high else 'grey' for x in range(N)])
    if speed != "No wait":
        time.sleep(1/speed)
    return (i+1)


def heapSort(arr):
    global comparisons
    global arrayAccesses

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arrayAccesses += 2
        show(N, arr, ['blue' if x == i or x ==
                      0 else 'grey' for x in range(N)])
        if speed != "No wait":
            time.sleep(1/speed)
        heapify(arr, i, 0)


def heapify(arr, n, i):
    global comparisons
    global arrayAccesses

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        comparisons += 1
        arrayAccesses += 1
        largest = l
    if r < n and arr[largest] < arr[r]:
        comparisons += 1
        arrayAccesses += 1
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        arrayAccesses += 2
        show(N, arr, ['blue' if x == i or x ==
                      largest else 'grey' for x in range(N)])
        if speed != "No wait":
            time.sleep(1/speed)
        heapify(arr, n, largest)

def radixSort(arr):
    global comparisons
    global arrayAccesses

    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countSort(arr, exp)
        exp *= 10

        sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                break
        if sorted:
            break


def countSort(arr, exp1):
    global comparisons
    global arrayAccesses

    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        arrayAccesses += 1
        show(N, arr, ['blue' if x == i else 'grey' for x in range(N)])
        if speed != "No wait":
            time.sleep(1/speed)
            

def finalArrayRun():
    global isSorted
    global comparisons
    global arrayAccesses

    for i in range(0, N):
        color = ['green' if x == i or x < i else 'grey' for x in range(N)]
        show(N, arr, color)
        if speed != "No wait":
            time.sleep(1/speed)

    isSorted = True

def startMergeSort():
    global isSorted

    if isSorted:
        return
    
    global comparisons
    global arrayAccesses
    comparisons = 0
    arrayAccesses = 0
    win.title('Complexity: O(nlogn), Best: O(nlogn), Worst: O(nlogn)')
    mainText.config(text='Visualizing Merge Sort')
    mergesort(arr, 0, N-1)

    finalArrayRun()



def startBubbleSort():
    global isSorted

    if isSorted:
        return
    global comparisons
    global arrayAccesses
    comparisons = 0
    arrayAccesses = 0
    win.title('Complexity: O(n^2), Best: O(n), Worst: O(n^2)')
    mainText.config(text='Visualizing Bubble Sort')
    bubbleSort(arr)

    finalArrayRun()


def startQuickSort():
    global isSorted

    if isSorted:
        return
    
    global comparisons
    global arrayAccesses
    comparisons = 0
    arrayAccesses = 0
    win.title('Complexity: O(nlogn), Best: O(nlogn), Worst: O(n^2)')
    mainText.config(text='Visualizing Quick Sort')
    quickSort(arr, 0, N-1)

    finalArrayRun()


def startHeapSort():
    global isSorted

    if isSorted:
        return
    
    global comparisons
    global arrayAccesses
    comparisons = 0
    arrayAccesses = 0
    win.title('Complexity: O(nlogn), Best: O(nlogn), Worst: O(nlogn)')
    mainText.config(text='Visualizing Heap Sort')
    heapSort(arr)

    finalArrayRun()

def startRadixSort():
    global isSorted

    if isSorted:
        return
    
    global comparisons
    global arrayAccesses
    comparisons = 0
    arrayAccesses = 0
    win.title('Complexity: O(nk), Best: O(nk), Worst: O(nk)')
    mainText.config(text='Visualizing Radix Sort')
    radixSort(arr)

    finalArrayRun()

def setSpeed():
    global speed
    if speedVar.get() == 'No wait':
        speed = "No wait"
    else:
        speed = int(speedVar.get())

    speedLabel.config(text='Speed:')


def setN():
    global N
    N = int(nVar.get())
    global arr
    arr = np.linspace(10, 390, N, dtype=np.uint16)
    global color
    color = ['grey' for _ in range(N)]
    show(N, arr, color)
    nLabel.config(text='Items:')
    shuffle()


global win
win = Tk()

N = 50
speed = 100
increment = 10
global accesses
accesses = 0
global isSorted
isSorted = False


arr = np.linspace(10, 390, N, dtype=np.uint16)

color = ['grey' for _ in range(N)]

win.title('Sorting visualizer')

global comparisonsVar
comparisonsVar = StringVar()
comparisonsVar.set('Comparisons: 0')
comparisonsLabel = ttk.Label(win, textvariable=comparisonsVar)
comparisonsLabel.pack()

global mainText
mainText = ttk.Label(win, text='Sorting Visualizer')
mainText.pack()

global arrayAccessesVar
arrayAccessesVar = StringVar()
arrayAccessesVar.set('Array accesses: 0')
arrayAccessesLabel = ttk.Label(win, textvariable=arrayAccessesVar)
arrayAccessesLabel.pack()


canvas = Canvas(win, width=800, height=400, bg='white')
canvas.pack()

ttk.Button(win, text='Merge Sort', command=startMergeSort).pack(
    side='right', padx=5, pady=5)

ttk.Button(win, text='Bubble Sort', command=startBubbleSort).pack(
    side='right', padx=5, pady=5)

ttk.Button(win, text='Quick Sort', command=startQuickSort).pack(
    side='right', padx=5, pady=5)

ttk.Button(win, text='Heap Sort', command=startHeapSort).pack(
    side='right', padx=5, pady=5)

ttk.Button(win, text='Radix Sort', command=startRadixSort).pack(
    side='right', padx=5, pady=5)



speedLabel = ttk.Label(win, text='Speed:')
speedLabel.pack(side='left', padx=5, pady=5)

speedVar = StringVar()
speedVar.set('100')
speedMenu = ttk.OptionMenu(win, speedVar, '100', '1', '10', '20', '30', '40',
                           '50', '60', '70', '80', '90', '100', '250', '500', '1000', "No wait")


speedVar.trace('w', lambda *args: setSpeed())
speedMenu.pack(side='left', padx=5, pady=5)

nLabel = ttk.Label(win, text='Items:')
nLabel.pack(side='left', padx=5, pady=5)

nVar = StringVar()
nVar.set('50')
nMenu = ttk.OptionMenu(win, nVar, '50', '10', '20', '30',
                       '40', '50', '60', '70', '80', '90', '100', '250')

nVar.trace('w', lambda *args: setN())
nMenu.pack(side='left', padx=5, pady=5)


ttk.Button(win, text='Shuffle array', command=shuffle).pack(side='right')
shuffle()
show(N, arr, color)

win.mainloop()
