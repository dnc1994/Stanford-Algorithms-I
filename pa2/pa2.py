with open('QuickSort.txt', 'r') as f:
    num = map(lambda x: int(x.strip()), f.readlines())

num1 = num[:]
num2 = num[:]
num3 = num[:]
    
def quicksort(array, left, right, p):
    global cnt
    if left < right:
        cnt += right - left       
        middle = p(array, left, right)
        quicksort(array, left, middle - 1, p)
        quicksort(array, middle + 1, right, p)
    
def partition(array, left, right):
    pivot = array[left]
    
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            
    array[left], array[i - 1] = array[i - 1], array[left]
    
    return i - 1
    
def partition2(array, left, right):
    POS = right

    array[left], array[POS] = array[POS], array[left]
    pivot = array[left]
    
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            
    array[left], array[i - 1] = array[i - 1], array[left]
    
    return i - 1
    
def partition3(array, left, right):
    middle = (left + right) / 2
    if middle == left or middle == right:
        POS = middle
    else:
        vals = [array[left], array[right], array[middle]]
        minval = min(vals)
        maxval = max(vals)
        for x in [left, right, middle]:
            if array[x] != minval and array[x] != maxval:
                POS = x

    array[left], array[POS] = array[POS], array[left]
    pivot = array[left]
    
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            
    array[left], array[i - 1] = array[i - 1], array[left]
    
    return i - 1
    
cnt = 0
quicksort(num1, 0, 9999, p=partition)
print cnt

cnt = 0
quicksort(num2, 0, 9999, p=partition2)
print cnt

cnt = 0
quicksort(num3, 0, 9999, p=partition3)
print cnt