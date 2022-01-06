class FindPairs:

    def __init__(self, arr, arr_size, suma):
        self.arr = arr
        self.arr_size = arr_size
        self.suma = suma

    #returns a list of the index of the pairs which sum matches
    #if no matches are found it will return an empty list
    # this is an usual two pointers strategie with modifications to find all posible pairs
    def findPairs(self):
        # Create an empty set
        pairs = list()
        #we are goint to use a two pointers strategie left(l) and right(r)
        l = 0
        r = self.arr_size-1
        #we need to guaratie that the array is sorted O(n log n)
        self.arr.sort()
        #temporal to save a pointer when we have pairs that might occur more than once
        temp = 0
        #a flag to identify when we have encounter a pair more than once
        flag = 0
        # traverse the array for the two elements
        while l<r:
            #if the flag is 0 we refresh the temporal pointer
            if flag == 0:
                temp = l
            if ( (self.arr[l] + self.arr[r]) == self.suma):
                pairs.append([l , r])
                # in the case of we find a pair we should mark the flag 
                if flag == 0:
                    flag = 1
                    temp = l
                l += 1
                # in the case we reach the right pointer we need to start moving the right pointer
                # so we have in count those extra pairs that cant be foind moving just the left one 
                if l == r:
                    r -= 1
                    l = temp
                # since we are moving the right pointer we need to find a way to stop the while
                # otherwise we can end up evaluating a value with itself
                # also at this point we finish the program so we can stop the while
                if r == temp:
                    break
            elif ( (self.arr[l] + self.arr[r]) < self.suma):
                l += 1
                #if we dont find a match we need to always mark the flag with  
                if flag == 1:
                    flag = 0
                    l = temp
            else:
                r -= 1
                if flag == 1:
                    flag = 0
                    l = temp
        return pairs