def count(s):
    vowel=0
    consonant=0
    digits=0
    space=0;

    v="aeiou"
    c="bcdfghjklmnpqrstvxyz"
    d='1234567890'

    for char in s:
        if(char in v):
            vowel+=1
        if(char in c):
            consonant+=1
        if(char in d):
            digits+=1
        if char.isspace():
            space+=1
    print(f"vowels:{vowel},consonant:{consonant},digits:{digits},space:{space}")


def isprime(n):
    if(n<=1):return False
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            return False
    return True

def sum(n):
    cnt=0
    for i in range(1,n):
        if isprime(i):
            cnt+=i
    print(f'sum is {cnt}')


sum(2000000)




        
