"""배열"""
arr = [1,2,3,4,5,6]
print(arr[4])
print(arr[1:4])
print(arr[-1])
arr2 = [1,2,3,[4,5]]
print(arr2[3])
print(arr2[3][0])
arr2.insert(4, [6,7])
print(arr2)
print("arr의 길이 : %d" % len(arr))
print("arr2의 길이 : %d" % len(arr2))