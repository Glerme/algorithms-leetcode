def bubble(arr):
  size = len(arr)
  
  for _ in arr:
    is_sorted = True
    print(arr)
    for i in range(size - 1):
      if arr[i] > arr[i+1]:
          is_sorted = False
          arr[i+1], arr[i] = arr[i], arr[i+1]

      if is_sorted: return


bubble([5,4,3,2,1])
bubble([1,2,3,4,5])