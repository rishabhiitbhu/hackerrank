#Using inbuilt heap functions
from heapq import heapify, heappop, heappush
#heapop: pop and return the minimum element
#heappush: push new element in the heap
#heapify: transform a list into heap

class MinHeap(object):

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2 if i!=0 else 0

    def insertKey(self, key):
        heappush(self.heap, key)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while(i!=0 and self.heap[i] < self.heap[self.parent(i)]):
            self.heap[i], self.heap[self.parent(i)] = \
                self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, key):
        i = self.heap.index(key)#O(n); use dictionary to store key to index
        self.decreaseKey(i, float('-inf'))
        self.extractMin()

    def getMin(self):
        return self.heap[0]
