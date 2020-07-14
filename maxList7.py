def linearSearch8(arr , x):
  for i in range(len(arr)):
  	if arr[i]==x:
  		return i
  return -1	

arr  = []
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
	ele = int(input("Enter elements: "))
	arr.append(ele)
x = int(input("Enter element to search in list: "))
print("element found at index "+str(linearSearch8(arr,x))) 