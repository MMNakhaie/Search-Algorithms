# This Program Creat by M.M.N

def Linear_Search(LST, item):
    found = 0
    for i in range(0, len(LST), 1):
        if  LST[i] == item :
            found = 1
            break
        else:
            found = 0
            
    if found==1 :
        print(" Item Exist in Array ! ")
    else:
        print(" Item Not Exist in Array ! ")

def main():
    print("\n Linear Search : For Not Sort List !")
    print("\n List is : [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]")

    Numbers = [ 9, 2, 1, 5, 3, 7, 10, 8, 4, 6 ]
    Item = int(input("\n Enter Item For Search : "))
    Linear_Search(Numbers, Item)

    input()

main()
