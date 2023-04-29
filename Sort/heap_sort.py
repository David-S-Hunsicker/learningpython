def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

	if l < n and arr[l] > arr[largest]:
		largest = l
	if r < n and arr[r] > arr[largest]:
		largest = r
	if largest != i:
 		(arr[i], arr[largest]) = (arr[largest], arr[i]) # swap
		heapify(arr, n, largest)

def heap_sort(arr):
	n = len(arr)
	last_parent = n//2-1
	for i in range (last_parent, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[i],arr[0] = arr[0],arr[i]
		heapify(arr, i, 0)
	return arr


arr = [5, 8, 3, 9, 4, 1, 7, 33, 45, 18, 111, 38, 94, 29, 0, -2, 563, 24, 265]
heap_sort(arr)
print(heap_sort(arr))

