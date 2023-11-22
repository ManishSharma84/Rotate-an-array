def rotateArr(Arr, lenth, sift):
    iteration=1
    while iteration <= sift:
        Last = Arr[0]
        for i in range(n - 1):
            Arr[i] = Arr[i+1]
        Arr[n-1] = Last
        iteration +=1
Arr = [1, 2, 3, 4, 5, 6]
n =len(Arr)
s =2

rotateArr(Arr, n, s)
print(Arr)
