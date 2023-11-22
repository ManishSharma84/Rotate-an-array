A = [1, 2, 3, 4, 5, 6]
shift = 2
def rotationByLeft(Arr_num, sift):
    for i in range(0, sift):
        first= Arr_num[0]
        for i in range(0, len(Arr_num)-1):
            Arr_num[i] = Arr_num[i+1]
        Arr_num[len(Arr_num)-1]= first
    return Arr_num
def rotationByRight(Arr_num, sift):
    for i in range(0, sift):
        last = Arr_num[len(Arr_num)-1]
        for j in range(len(Arr_num)-1, 0, -1):
            Arr_num[j] = Arr_num[j-1]
        Arr_num[0] = last
    return Arr_num

def printArray(Arr):
    for i in range(0, len(Arr)):
        print(Arr[i], end=' ')

print("\nArray Rotation by Right")
print("Array", A)
print("Rotated")
RotatedArrayByRight = rotationByRight(A, shift)
printArray(RotatedArrayByRight)

print("\n\nArray Rotation by Left")
print("Array", A)
print("Rotated")
RotatedArrayByLeft = rotationByLeft(A, shift)
printArray(RotatedArrayByLeft)
