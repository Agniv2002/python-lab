def divisibleByK(tuple,k):
    result=[]
    for tup in tuple:
        divisible=True
        for element in tup:
            if(element%k!=0):
                divisible=False
                break
        if divisible==True:
            result.append(tup)
    print(f'divisible by k is {result}')
def isUpper(tuple):
    result=[]
    for tup in tuple:
        upperCase=True
        for elem in tup:
            if not(elem.isupper()):
                upperCase=False
                break
        if upperCase==True:
            result.append(tup)
    print(f'disupper is {result}')
def countOccurences(tuple_arr,list_arr):
    result={}
    for i in list_arr:
        result[i]=result.get(i,0)+tuple_arr.count(i)
        
    print(f'result : {result}')

test_list = [(6, 24, 12), (60, 12, 6), (12, 18,21)]
divisibleByK(test_list,6)
alphabets=[("GFG","IS","BEST"),("gGF","AVERAGE"),("GFG")]
isUpper(alphabets)
tuple_arr=('a','a','b','b','c','c','c')
list=['a','b']
countOccurences(tuple_arr,list)

