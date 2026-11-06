
def sum(lst):
    if lst == []:
        return 0
    return lst[0] + sum(lst[1:])

def count(lst):
    if lst == []:
        return 0
    return 1 + count(lst[1:])

def max(lst):
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
    sub_max = max(lst[1:])
    if lst[0] > sub_max:
        return lst[0]
    else:
        return sub_max

def quick_sort(lst):
    if len(lst) <2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

data = [int(i) for i in input().split()]
print(sum(data))
print(count(data))
print(max(data))
print(quick_sort(data))
