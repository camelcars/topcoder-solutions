# There are certain things in here that I define as stacks. No doubt I am using the term wrongly as stacks mean something else. Howevver, this was the most appropriate name I could think of at the time
import copy


class autogame:
    def __init__(self,og,iterations):
        self.og = og
        self.repeats = iterations
        self.master_array = [[0 for i in range(len(self.og))] for i in range(len(self.og))]
        for i in range(len(self.og)):
            self.master_array[i][i] = "t"
        self.master_array = self.positions(self.master_array, self.og)
        self.copy_of_master_array = copy.deepcopy(self.master_array)

    def positions(self,master_array,og):    #This function identifies all the ways to arrange 't'. It also replaces the 't' with '1'
        for array in self.master_array:  # In tis loop, I am iterating over an array that is being extended. Technically you shouldn't do this, but it works, so whatever
            for i in range(len(array)):
                tempo = array[:]
                tempo[i] = "t"
                if tempo not in self.master_array:
                    self.master_array.append(tempo)

        for array in self.master_array:
            for t in range(len(array)):
                if array[t] == "t":
                    array[t] = 1
        return self.master_array


    #This function is used in main_possible
    def custom_add(self,array):  # This adds the stacks in the array together. Basically [1,1,0,0]+[1,0,1,0] = [2,1,1,0]
        stack = []
        for i in range(len(array[0])):
            stack.append(array[0][i] + array[1][i])
        return [stack]


    #This function is used in main_possible
    def repositioning_2(self,og,array,t):  # This function repositions the tokens. This is in accordance with the rules of the game
        tempo = og[t] - 1
        a_stack = [0 for i in range(len(og))]
        a_stack[tempo] = 1
        return a_stack



    def main_possible(self):
        for i in range(self.repeats):
            for array in range(len(self.copy_of_master_array)):
                stack = []

                for t in range(len(self.copy_of_master_array[array])):

                    if self.copy_of_master_array[array][t] != 0:            # array is [1,0,0,0]
                        stack.append(self.repositioning_2(self.og, self.copy_of_master_array[array], t))

                        if len(stack) == 2:                 # This makes sure that stack is always a single array
                            stack = self.custom_add(stack)
                print(self.copy_of_master_array[array])
                print(stack)
                reduced_stack = list(filter(lambda x: x < 2, stack[0]))
                if len(reduced_stack) != len(self.copy_of_master_array[array]):
                    self.master_array.remove(self.copy_of_master_array[array])
                else:
                    print(True)
                    self.master_array.insert(0, stack[0])
                    self.master_array.remove(self.copy_of_master_array[array])
            self.copy_of_master_array = copy.deepcopy(self.master_array)

        self.master_array.append([0, 0, 0, 0])

        return len(self.master_array)


a = autogame([4,4,3,2,1],3)
print(a.main_possible())
