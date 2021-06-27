import random
import time
import parse_tree as ps
import shunting_yard as sy

class Generator:
    def __init__(self):
        self.oprs = "+-*/"
        self.nums = "123456789"   

    def genExp(self,length):
        exp = ""
        for i in range(length//2):
            exp += self.nums[random.randint(0,1000)%9]
            exp += self.oprs[random.randint(0,1000)%4]
        exp += self.nums[random.randint(0,1000)%9]
        return exp


if __name__ == '__main__':

    test = Generator()
    inputs = []
    for i in range(100):
        inputs.append(test.genExp(100))
    
    t1 = time.time()
    ps_tree = ps.Calculator1()
    for exp in inputs:
        ps_tree.calculate(exp)
    t2 = time.time()
    print("Parse Tree: \t",t2-t1)

    t3 = time.time()
    shunt_yrd = sy.Calculator2()
    for exp in inputs:
        shunt_yrd.calculate(exp)
    t4 = time.time()
    print("Shunting Yard: \t",t4-t3)