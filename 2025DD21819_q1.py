n = list(map(int,input().split()))

def merge(left, right):
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp.extend(left[i:])
    temp.extend(right[j:])
    
def merge_sort(lst):

    k = len(lst)
    if (k == 0): 
        return []
    mid = len // 2
    
    A = merge_sort(lst[:mid])
    B = merges_sort(lst[mid:])
    
    return merge(A, B)
    
print(merge_sort(n))
