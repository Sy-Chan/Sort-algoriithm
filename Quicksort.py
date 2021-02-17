class QSort:
    def __init__(self, arr):
        self.low = 0
        self.arr = arr
        self.high = len(self.arr)-1
        #call the properties to get the result
        self.sort = self.recurve(self.low, self.high, self.arr)
        
    #recurve to arrnge the list
    def recurve(self, low, high, arr):
        if low < high:
            pi = self.part(low, high, arr)
            self.recurve(low, pi-1, arr)
            self.recurve(pi+1, high, arr)
            
            return arr
   #divide the list into parts by index     
    def part(self, low, high, arr):
        i = low-1
        for j in range(low, high):
            if arr[j] < arr[high]:
                i = i+1
                arr[i], arr[j] = arr[j],arr[i]       
        
        arr[i+1], arr[high] = arr[high],arr[i+1]
        return i+1


    
xyz = [10,30,80,90,40,50,70]
print(QSort(xyz).QSort)
