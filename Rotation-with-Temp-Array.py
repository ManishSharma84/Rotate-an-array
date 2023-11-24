def rotatearray(arr, shift):
    new_list = []
    new_list = arr[shift:]+arr[0:shift]
    return new_list


A = [1, 2, 3, 4, 5, 6]
d = 2

rotated = rotatearray(A, d)
for i in rotated:
    print(i, end=" ")
