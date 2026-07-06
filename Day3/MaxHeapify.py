def MaxHeapify(A, n, i):
    largest = i 
    
    left = 2*i + 1
    right = 2*i + 2
    
    if left<n and A[left] > A[largest]:
        largest = left
    if right<n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, n,largest)



arr = [int(x) for x in input('Enter array to sort: ').split()]

print(f"array befor sort: {arr}")
MaxHeapify(arr, len(arr), 0)
print(f"arr after sort: {arr}")