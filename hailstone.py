def hailstone(num):
    print(num, end = " ")
    while num > 1:
        if num%2==0:
            num=int(num/2)
            print(num, end=" ")
        else:
            num=num*3+1
            print(num, end= " ")
num=int(input("Enter a number: "))
hailstone(num)