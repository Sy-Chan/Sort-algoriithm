def selection(arr):
    n = len(arr)
    for i in range(n):
        ind0 = i
        
        for j in range(i+1,n):     
            if arr[ind0] > arr[j]:
                ind0 = j
        arr[i], arr[ind0] = arr[ind0],arr[i]
    return arr


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1,n):     
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]
    return arr

    

def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        a = arr[i]
        print("arr",i,"=",a)
        j = i-1
        while j>= 0 and a < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        print("insert before/stay:",arr[j+1])
        arr[j+1] = a
        
        print(arr)
    return arr


class QSort:
    def __init__(self, arr):
        self.low = 0
        self.arr = arr
        self.high = len(self.arr)-1
        self.sort = self.recurve(self.low, self.high, self.arr)#Call
        
    def recurve(self, low, high, arr):
        if low < high:
            pi = self.quick(low, high, arr)
            self.recurve(low, pi-1, arr)
            self.recurve(pi+1, high, arr)
            return arr
        
    def quick(self, low, high, arr):
        i = low-1
        for j in range(low, high):
            if arr[j] < arr[high]:
                i = i+1
                arr[i], arr[j] = arr[j],arr[i]       
        arr[i+1], arr[high] = arr[high],arr[i+1]
        return i+1



##from time import time as t
import numpy.random as np
abc = np.randint(0,100,10)
print(abc)
print('\n',"sorted:",insertion(abc))


##def record(a):
##    from time import time as t
##    start = t()
##    for i in range(10):
##        import numpy.random as np
##        abc = np.randint(0,1000,200)
##        a(abc)
##        i+=1
##        
##    return (t()-start)/i        
##
##print("Bubble",record(bubble),'\n', "Insertion",record(insertion), '\n',"Selection",record(selection))
##
##from time import time as t
##start = t()
##for i in range(10):
##    import numpy.random as np
##    abc = np.randint(0,1000,200)
##    QSort(abc).sort
##    i+=1
##print('',"Qsort",(t()-start)/i)





