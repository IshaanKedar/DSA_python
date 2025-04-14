'''You're working on a new feature on Jovian called "Top Notebooks of
the Week". Write a function to sort a list of notebooks in decreasing order of likes.
Keep in mind that up to millions of notebooks can be created every week, so your
function needs to be as efficient as possible.'''

#wap to sort a list of numbers
def sort(nums):
    pass

test0 = {'input': {'nums':[4,2,6,3,4,6,2,1]},'output':[1,2,2,3,4,4,6,6]}
test1 = {'input': {'nums':[5,2,6,1,23,7,-12,12,-243,0]},'output':[-243,-12,0,1,2,5,6,7,12,23]}
test2 = {'input': {'nums':[1,2,3,4,5,6,7,8]},'output': [1,2,3,4,5,6,7,8]}
test3 = {'input': {'nums':[99,10,9,8,6,5,3]},'output':[3,5,6,8,9,10,99]}
test4 = {'input': {'nums':[5,12,2,6,1,23,7,7,-12,6,6,12,1,-243,1,0]},'output':[-243,-12,0,1,1,1,2,5,6,6,6,7,7,12,12,23]}
test5 = {'input': {'nums': []},'output':[]}
test6 = {'input': {'nums': [3]},'output':[3]}
test5 = {'input': {'nums': [5,5,5,5,5,5]},'output':[5,5,5,5,5,5]}

import random

in_list = list(range(10000))
out_list = list(range(10000))

random.shuffle(in_list)

test7 = {'input': {'nums':in_list},'output':out_list}

tests = [test0,test1,test2,test3,test4,test5,test6,test7]

#bubble sort

def bubble_sort(nums):
    nums = list(nums)

    for j in range(len(nums)-1):
        for i in range(len(nums)-1):
        
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]

    return nums

nums0 ,out0 = test0['input']['nums'], test0['output']

result0 = bubble_sort(nums0)
print('input',nums0)
print('expected output',out0)
print('actual output', result0)
print("match:",result0==out0)

from jovian.pythondsa import evaluate_test_cases

results = evaluate_test_cases(bubble_sort,tests)

#more efficient algorithm 
#insertion sort

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j>=0 and nums[j] > cur:
            j-= 1
        nums.insert(j+1,cur)
    return nums

results2 = evaluate_test_cases(insertion_sort,tests)

#divide and conquer

def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_nums = merge(left_sorted,right_sorted)

    return sorted_nums

def merge(nums1, nums2):
    merged =[]
    i,j = 0,0

    while i<len(nums1) and j< len(nums2):
        if nums1[i]<= nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
        
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    return merged + nums1_tail+nums2_tail

print(merge([1,4,7,9,11],[-1,0,2,3,8,12]))

results3 = evaluate_test_cases(merge_sort,tests)


