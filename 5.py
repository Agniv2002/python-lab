def first():
    my_dict=dict()
    my_dict['k1']=2
    my_dict['k2']=2
    my_dict['k3']=2
    my_dict['k4']=2

    print(f'my_dict {my_dict}')

    my_dict['k2']=3

    print(f"{my_dict['k3']}")
    print(f"{my_dict.get('k3')}")
    del my_dict['k3']
    print(f'my_dict {my_dict}')
def second():
    my_dict=dict()
    my_dict['k1']=2
    my_dict['k2']=2
    my_dict['k3']=2
    my_dict['k4']=2
    my_dict.pop('k3')
    print(f"{my_dict}")
    my_dict.popitem()
    print(f"{my_dict}")
    my_dict.clear()
    print(f"{my_dict}")
def third():
    my_dict=dict()
    my_dict['k1']=2
    my_dict['k2']=2
    my_dict['k3']=2
    my_dict['k4']=2
    cnt=0
    cnt=sum(my_dict.values())
    print(f"{cnt}")
def fourth():
    my_dict1={'a':2,'b':4,'c':6}
    my_dict2={'a':3,'d':5,'f':8}
    my_dict1.update(my_dict2)
    print(f"{my_dict1}")


first()
second()
third()
fourth()




