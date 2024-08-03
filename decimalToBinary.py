def f_decToBin(n):
    if(n>=2):
        return str(f_decToBin(n//2)) + str((n %2))
    elif(n==1):
        return 1

def f_decToBin2(n):
    return bin(n)

if __name__ == '__main__':
    num= int(input("enter num"))

    print("the binary num of {} is {}".format(num, f_decToBin(num))) #decimal to binary without the bin() function
    num2= f_decToBin2(num)
    print("the binary num of {} with bin() is {}".format(num, f_decToBin2(num))) #bin() function

    print("the binary num of {} with bin() is {}".format(num, num2[2:])) #for the binary number using bin() function but without having binray format

