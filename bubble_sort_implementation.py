#Bubble sort
def bubble_sort(array):
	for i in range(len(array)-1):
		for j in range (len(array)-1-i):
			if array[j] > array[j+1]:
				temp = a[j+1]
				array[j+1] = array[j]
				array[j] = temp
		return array
array = [1,2,4,3,7,6]
array=bubble_sort(array)
print(array)


