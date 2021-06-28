import random
import time
import parse_tree2 as ps
import shunting_yard as sy

class Generator:
    def __init__(self):
        self.oprs = "+-*/"
        self.nums = "123456789"   

    def genExp(self,length):
        exp = ""
        for i in range(length//2):
            exp += self.nums[random.randint(0,8)]
            exp += self.oprs[random.randint(0,3)]
        exp += self.nums[random.randint(0,8)]
        return exp


if __name__ == '__main__':

    # inputs: m mathematical expressions each with length l
    test = Generator()
    inputs = []
    m,l = 100,100
    for i in range(m):
        inputs.append(test.genExp(l))
    
    # time comparison
    t1 = time.time()
    ps_tree = ps.Calculator2()
    for exp in inputs:
        ps_tree.calculate(exp)
    t2 = time.time()
    print("Parse Tree: \t",t2-t1)

    t3 = time.time()
    shunt_yrd = sy.Calculator3()
    for exp in inputs:
        shunt_yrd.calculate(exp)
    t4 = time.time()
    print("Shunting Yard: \t",t4-t3)