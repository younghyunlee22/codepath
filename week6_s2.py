def find_max(lst, x):
    pntr1 = 0
    pntr2 = x

    while pntr2 <= len(lst):
        print(max(lst[pntr1:pntr2]))
        pntr1 += 1
        pntr2 += 1


find_max([1, 2, 3, 1, 4, 5], 3)
