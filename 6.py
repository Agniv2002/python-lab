class Car:
    def __init__(self,model_name,color,price,top_speed):
        self.model_name=model_name
        self.color=color
        self.price=price
        self.top_speed=top_speed
      
    def readDetails(self):
        print(f"model_name: {self.model_name} color: {self.color} price: {self.price} top_speed: {self.top_speed}")

car1=Car("toyota","red",1234,400)
car2=Car(None,None,None,None)
car2.model_name="raja"
car2.price=134
car2.top_speed=400
car2.color="yellow"

car1.readDetails()
car2.readDetails()