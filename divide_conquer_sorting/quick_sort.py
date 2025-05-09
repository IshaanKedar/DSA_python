def quicksort(nums, start=0, end = None):
    if end is None:
        nums = list(nums)
        end = len(nums)-1

    if start<end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot -1)
        quicksort(nums, pivot+1, end)
    
    return nums

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    pivot = nums[end]
    i = start - 1

    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1  # Pivot index


ll = [1,5,6,2,0,11,3]
print(ll)
pivot = partition(ll)
print(ll, pivot)

