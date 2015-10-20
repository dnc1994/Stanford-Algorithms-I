with open('IntegerArray.txt') as f:
    seq = map(int, [line.strip() for line in f.readlines()])
 
count = 0
 
print len(seq) 
 
def merge(left, right):
    global count
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i
    result += left[i:] + right[j:]
    return result
    
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)
    
sorted_seq = merge_sort(seq)
print count