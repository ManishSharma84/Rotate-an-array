A = [1, 2, 3, 4, 5, 6]
shift = 2

def ArrayRotationbyRight(Arr_num, sift):
    for i in range(0, sift):
        temp = Arr_num[len(Arr_num)-1]
        for j in range(len(Arr_num)-1, 0, -1):
            Arr_num[j] = Arr_num[j-1]
        Arr_num[0] = temp
    return Arr_num

def printArray(Arr):
    for i in range(0, len(Arr)):
        print(Arr[i], end=' ')

print(A)
RotatedArray = ArrayRotationbyRight(A, shift)
printArray(RotatedArray)