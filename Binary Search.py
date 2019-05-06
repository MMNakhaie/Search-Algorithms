# This Program Creat by M.M.N

def Binary_Search(LST, item):
    First = 0
    Last = len(LST)-1
    mid = 0
    while First <= Last :
        mid = int((First + Last) / 2)
        if  item < LST[mid] :
            Last = mid - 1
        elif  item > LST[mid] :
            First = mid + 1
        else:
            return mid
    return -1

def main():
    print("\n Binary Search : For Sort List !")
    print("\n List is : [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]")
   
    Numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    Item = int(input("\n Enter Item For Search : "))

    if  Binary_Search(Numbers, Item) == -1 :
        print(" Item Not Exist in Array ! ")
    else:
        print(" Item Exist in Array ! ")

    input()

main()
