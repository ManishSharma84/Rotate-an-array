# Rotate an Array one by one (left shift)
def rotatearray(arr, length, shift):
    itr = 1
    while itr <= shift:
        # for left shift
        first = arr[0]
        for i in range(length-1):
            arr[i] = arr[i+1]
        arr[length-1] = first
        itr += 1

        # # for Right shift
        # last = arr[length - 1]
        # for i in range(length-1, 0, -1):
        #     arr[i] = arr[i-1]
        # arr[0] = last
        # itr += 1
    return arr


A = [1, 2, 3, 4, 5, 6]
n = len(A)
s = 4

rotated = rotatearray(A, n, s)
print(rotated)
