class QSort:
    def __init__(self, arr):
        self.low = 0
        self.arr = arr
        self.high = len(self.arr)-1
        self.QSort = self.sort(self.low, self.high, self.arr)#Call
        
    
    def recurve(self, low, high, arr):
        if low < high:
            pi = self.quick(low, high, arr)
            self.sort(low, pi-1, arr)
            self.sort(pi+1, high, arr)
            
            return arr
        
    def quick(self, low, high, arr):
        i = low-1
        for j in range(low, high):
            if arr[j] < arr[high]:
                i = i+1
                arr[i], arr[j] = arr[j],arr[i]       
        
        arr[i+1], arr[high] = arr[high],arr[i+1]
        return i+1


#test    
xyz = [10,30,80,90,40,50,70]
print(QSort(xyz).QSort)
