from tkinter import *
from tkinter import ttk
import numpy as np
import time


def show(n: int, data: list, colours: list):
    canvas.delete('all')
    width = 1560/(3*n-1)
    gap = width/2
    for i in range(n):
        canvas.create_rectangle(7+i*width+i*gap, 0, 7 +
                                (i+1)*width+i*gap, data[i],
                                fill=colours[i])
    win.update_idletasks()


def shuffle():
    win.title('Sorting visualizer')
    mainText.config(text='Sorting visualizer')
    np.random.shuffle(arr)
    show(N, arr, color)


def mergesort(arr, left, right):
    if left < right:
        m = (left+right)//2
        mergesort(arr, left, m)
        mergesort(arr, m+1, right)

        j = m+1
        if arr[m] <= arr[m+1]:
            return

        while left <= m and j <= right:
            show(N, arr, ['blue' if x == left or x ==
                          j else 'grey' for x in range(N)])
            time.sleep(1/speed)
            if arr[left] <= arr[j]:
                left += 1
            else:
                show(N, arr, ['red' if x == left or x ==
                              j else 'grey' for x in range(N)])

                time.sleep(1/speed)
                temp = arr[j]

                i = j
                while i != left:
                    arr[i] = arr[i-1]
                    show(N, arr, ['red' if x == i or x ==
                                  j else 'grey' for x in range(N)])
                    time.sleep(1/speed)
                    i -= 1

                arr[left] = temp

                show(N, arr, ['green' if x == left or x ==
                              j else 'grey' for x in range(N)])
                time.sleep(1/speed)
                left += 1
                m += 1
                j += 1


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                show(N, arr, ['blue' if x == j or x ==
                              j+1 else 'grey' for x in range(N)])
                time.sleep(1/speed)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def partition(arr, low, high):

    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            show(N, arr, ['blue' if x == j or x ==
                          i else 'grey' for x in range(N)])
            time.sleep(1/speed)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    show(N, arr, ['blue' if x == i+1 or x ==
                  high else 'grey' for x in range(N)])
    time.sleep(1/speed)
    return (i+1)


def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        show(N, arr, ['blue' if x == i or x ==
                      0 else 'grey' for x in range(N)])
        time.sleep(1/speed)
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        show(N, arr, ['blue' if x == i or x ==
                      largest else 'grey' for x in range(N)])
        time.sleep(1/speed)
        heapify(arr, n, largest)


def startMergeSort():
    shuffle()
    win.title('Complexity: O(nlogn), Best: O(nlogn), Worst: O(nlogn)')
    mainText.config(text='Visualizing Merge Sort')
    mergesort(arr, 0, N-1)
    show(N, arr, ['green' for _ in range(N)])


def startBubbleSort():
    shuffle()
    win.title('Complexity: O(n^2), Best: O(n), Worst: O(n^2)')
    mainText.config(text='Visualizing Bubble Sort')
    bubbleSort(arr)
    show(N, arr, ['green' for _ in range(N)])


def startQuickSort():
    shuffle()
    win.title('Complexity: O(nlogn), Best: O(nlogn), Worst: O(n^2)')
    mainText.config(text='Visualizing Quick Sort')
    quickSort(arr, 0, N-1)
    show(N, arr, ['green' for _ in range(N)])


def startHeapSort():
    shuffle()
    win.title('Complexity: O(nlogn), Best: O(nlogn), Worst: O(nlogn)')
    mainText.config(text='Visualizing Heap Sort')
    heapSort(arr)
    show(N, arr, ['green' for _ in range(N)])


def setSpeed():
    global speed
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


arr = np.linspace(10, 390, N, dtype=np.uint16)

color = ['grey' for _ in range(N)]

win.title('Sorting visualizer')

global mainText
mainText = ttk.Label(win, text='Sorting Visualizer')
mainText.pack(padx=5, pady=5)
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


speedLabel = ttk.Label(win, text='Speed:')
speedLabel.pack(side='left', padx=5, pady=5)

speedVar = StringVar()
speedVar.set('100')
speedMenu = ttk.OptionMenu(win, speedVar, '100', '10', '20', '30', '40',
                           '50', '60', '70', '80', '90', '100', '250', '500', '1000', '10000')

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
