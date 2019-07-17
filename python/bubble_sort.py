
def bubble_sort(nlist):

    for passnum in range(len(nlist)-1, 0, -1):
        for i in range (passnum):
            if nlist[i] > nlist[i+1]:
                # Swap values
                nlist[i+1], nlist[i] = nlist[i], nlist[i+1]


test_list = [8, 3, 7, 9, 4, 2]
bubble_sort(test_list)

print(test_list)
