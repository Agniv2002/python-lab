def isSymmetrical(s):
    isSym=s[:len(s)//2]==s[len(s)//2:]
    print(f"{isSym}")
    isPal=s[::]==s[::-1]
    print(f"{isPal}")

def vowel(s):
    cnt=0
    ans=""
    vowels="aeiouAEIOU"
    for i in s:
        if(i!='e' and i!='s'):
            ans+=i
        if i in vowels:
            cnt+=1
    print(f"vowel are {cnt}")
    print(f"string is {ans}")
def remove(s):
    r=s.split()
    ans=''.join(r[1::])
    print(f"the string is {ans}")

def count(s):
    ans={}
    for char in s:
        ans[char]=ans.get(char,0)+1
    print(f"count is {ans}")

s1="abcabc"
s2="aeiou"
s3="My name is Agniv"
s4="my name is agniv"
isSymmetrical(s1)
vowel(s2)
remove(s3)
count(s4)

    
