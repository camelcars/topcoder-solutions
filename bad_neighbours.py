class bad_neighbour:
    '''Read the rules on topcoder, you 'll understand what this does'''
    def __init__(self,array):
        self.array = array
        self.first_array = array[0:len(array)-1]
        self.last_array = array[1:len(array)]
        #The purpose of first_array and last_array is to deal with the circular nature of the question
        self.final_value_1 = self.maximizing(self.first_array,len(self.first_array)-1)
        self.final_value_2 = self.maximizing(self.last_array,len(self.last_array)-1)
        self.final_value = max(self.final_value_1,self.final_value_2)

    def maximizing(self,different_arrays,length):
        if length == 0:
            return different_arrays[0]
        if length == 1:
            return max(different_arrays[0],different_arrays[1])
        if length == 2:
            return max(different_arrays[2] + different_arrays[0], self.maximizing(different_arrays,1))
        bigger = max(different_arrays[length] + self.maximizing(different_arrays,length - 2), self.maximizing(different_arrays,length - 1))
        # print(bigger)
        return bigger

a = bad_neighbour([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(a.final_value)
