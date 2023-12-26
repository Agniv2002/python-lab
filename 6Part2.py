class Bank:
    def __init__(self,bankName,numCust):
        self.bankName = bankName
        self.numCust = numCust
    def details(self):
        print(f"bankName: {self.bankName}, numCust: {self.numCust}")

class GovtBank(Bank):
    def __init__(self,bankName,numCust,branchName,IFSCcode):
        super().__init__(bankName,numCust)
        self.branchName=branchName
        self.IFSCcode=IFSCcode
    def details(self):
        super().details()
        print(f"branchName: {self.branchName}, IFSC:{self.IFSCcode}")

class PrivateBank(Bank):
    def __init__(self,bankName,numCust,branchName,IFSCcode):
        super().__init__(bankName,numCust)
        self.branchName=branchName
        self.IFSCcode=IFSCcode
    def details(self):
        super().details()
        print(f"branchName: {self.branchName}, IFSC:{self.IFSCcode}")

GBank=GovtBank("sbi",34234,"hakimpara",1232)
PBank=PrivateBank("hdfc",42342,"raju",4242)
GBank.details()
PBank.details()