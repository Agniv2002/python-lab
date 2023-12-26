class TIME:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __add__(self,other):
        totalSeconds=self.hour*3600 + self.minute*60 + self.second
        totalSeconds+=other.hour*3600 + other.minute*60 + other.second

        new_hour,rem=divmod(totalSeconds,3600)
        new_minute,new_second=divmod(rem,60)
        return TIME(new_hour,new_minute,new_second)

    def __sub__(self,other):
        totalSeconds=self.hour*3600 - self.minute*60 + self.second
        totalSeconds-=other.hour*3600 - other.minute*60 + other.second
        new_hour,rem=divmod(abs(totalSeconds),3600)
        new_minute,new_second=divmod(rem,60)
        return TIME(new_hour,new_minute,new_second)
    
    def display(self):
        print(f"hours:{self.hour},minutes:{self.minute},seconds:{self.second}")
    

t1=TIME(12,34,56)
t2=TIME(14,45,67)
result_addition=t1+t2
result_addition.display()
# print(f"{result_addition}")

result_subtraction=t1-t2
result_subtraction.display()
# print(f"{result_subtraction}")