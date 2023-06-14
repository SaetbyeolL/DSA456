
# Searching & Sorting

# Merge Sort: O(n)

def merge_sort(arr):
	if len(arr) > 1:
		left_arr = arr[:len(arr)//2]
		right_arr= arr[len(arr)//2:]

		#recursion
		merge_sort(left_arr)
		merge_sort(right_arr)

		#merge
		i = 0 
		j = 0
		k = 0 #merged array index
		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1

		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1

arr_test = [2,3,5,1,7,4,4,4,2,6,0]
merge_sort(arr_test)
print(arr_test)



# Quick Sort: O(N logN) or O(n^2)

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
	if start >= end: # if element is one, end
		return
	pivot = start #pivot is first element
	left = start + 1 #leftmost element excluding pivot
	right = end
	while(left <= right):
		#loop until we find bigger data than pivot
		while(left <= end and array[left] <= array[pivot]):
			left += 1
		#loop until we find smaller data than pivot
		while(right > start and array[right] >= array[pivot]):
			right -= 1
		#if it twist line, change smaller data with pivot
		if(left > right):
			array[right], array[pivot] = array[pivot], array[right]
		#if not, change smaller data with bigger data
		else:
			array[left], array[right] =  array[right], array[left]
		
	#Once split, Sort on left part and right part respectively
	quick_sort(array, start, right-1)
	quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

