class Sort:
    @staticmethod
    def bubble_sort(array:list[int | float | str])->list[int | float | str]:
        flag = True
        while flag:
            flag = False
            for i in range(len(array)-1):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    flag = True
        return array
    @staticmethod
    def selection_sort(array:list[int | float | str])->list[int | float | str]:
         for i in range(len(array)-1):
             index = i
             for k in range(i+1,len(array)):
                  if array[index]>array[k]:
                      index = k
             array[index],array[i] = array[i],array[index]
         return array
    @staticmethod
    def insertion_sort(array):
        for i in range(1,len(array)):
            index = i
            while index>1 and array[i]<array[index-1]:
                index-=1
            else:
                array.insert(index,array.pop(i))
        first = array.pop(0)
        for i in range(len(array)):
            if array[i]>first:
                array.insert(i,first)
                break
        return array
    @staticmethod
    def heap_sort(array):
        def helpify(array,n,i):
            largest = i
            left = largest*2+1
            right = largest*2+2
            if left<n and array[left]>array[largest]:
                largest = left
            if right<n and array[right]>array[largest]:
                largest = right
            if largest!= i:
                array[i],array[largest] = array[largest],array[i]
                helpify(array,n,largest)

        for i in range(len(array)-1, -1, -1):
            helpify(array,len(array), i)
        for i in range(len(array)-1,0,-1):
            array[i],array[0] = array[0],array[i]
            helpify(array,i,0)
        return array
    @staticmethod
    def shell_sort(array:list[int | float | str]) -> list[int | float | str]:
        middle = len(array)//2
        while middle:
            for i in range(middle, len(array)):
                index = i
                temp = array[index]
                while index>=middle and array[index-middle]>temp:
                    array[index] = array[index-middle]
                    index = index-middle
                array[index] = temp
            middle=middle//2
        return array
    @staticmethod
    def merge_sort(array:list[int | float | str]) -> list[int | float | str]:
        def merge(arr1:list[int | float | str], arr2:list[int | float | str]) -> list[int | float | str]:
            result = []
            while arr1 and arr2:
                if arr1[0]>arr2[0]:
                    result.append(arr2.pop(0))
                else:
                    result.append(arr1.pop(0))
            return result+arr1+arr2
        def helpify(array):
            if len(array)<=1:
                return array
            return merge(helpify(array[:len(array)//2]),helpify(array[len(array)//2:]))
        return helpify(array)
    @staticmethod
    def quick_sort(array:list[int | float | str]) -> list[int | float | str]:
        def helpify(array):
            if len(array)<=1:
                return array
            elif len(array)==2:
                return [min(array),max(array)]
            seed = array[len(array) // 2]
            low, middle, hight = [], [], []
            for i in array:
                if i > seed:
                    hight.append(i)
                elif i == seed:
                    middle.append(i)
                elif i < seed:
                    low.append(i)
            return helpify(low)+middle+helpify(hight)
        return helpify(array)
