array = [1, 7, 4, 9, 2, 5]

def zigzag(array):
    difference = []
    for i in range(len(array)-1):
        difference.append(array[i+1]-array[i])
    print(difference)
    first  = difference[0]
    counter = 1
    for i in range(1,len(difference[:])):
        print(first)
        if first>0:
            if difference[i]<0:
                counter +=1
                first = difference[i]

        if first<0:
            if difference[i]>0:
                counter +=1
                first = difference[i]
        else:
            pass
    print(counter+1)

zigzag(array)
