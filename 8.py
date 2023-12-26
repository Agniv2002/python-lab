def countFileStats(filename):
    with open(filename,'r') as file :
        text=file.read()
        lines=text.count('.') + text.count('?') + text.count('!')
        print(f"the total number of line are {lines}")

        words=text.split()
        print(f"the totlan umber of words are {words}")

        char=len(text)
        print(f"the total number of character are {char}")


def copyToTarget(source):
    with open(source,'r') as source,open("target.txt",'w') as target:
        lines=0
        for line in source:
            target.write(line.lower())
            lines+=1
        print(f"Number of lines copied to target.txt: {lines}")

records=[{'name':'agniv','roll':123,'branch':'ise'},{'name':'raju','roll':423,'branch':'ise'},{'name':'rahul','roll':32,'branch':'ece'}]
filename=input("Enter the file name: ")
countFileStats(filename)
copyToTarget(filename)
branchName=input("Enter the branch")

for record in records:
    if record['branch']==branchName:
        print(f"the details are {record['name']} and {record['roll']}")