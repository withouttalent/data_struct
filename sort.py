def bubble(alist):
    for number in range(len(alist)-1,0,-1):
        for i in range(number):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


l = [42, 1, 32, 64, 13, 74, 42, 45]
bubble(l)
print(l)