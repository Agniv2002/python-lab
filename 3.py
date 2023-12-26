def divisible(num):
    ans=[]
    for i in num:
        if i%4==0 and i%5!=0:
            ans.append(i)
    print(f'{ans}')
def sumAndOdd(num):
    odd=0
    even=0
    for i in num:
        if i&1:
            odd+=i
        else:
            even+=i
    print(f'odd:{odd}even:{even}')
def uniqueNums(num):
    ans=list(set(num))
    print(f'{ans}')
num=list(map(int,input("Enter a list of numbers separated by spaces").split()))
sumAndOdd(num)
divisible(num)
uniqueNums(num)
