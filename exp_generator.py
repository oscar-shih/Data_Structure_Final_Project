import random
import time
import parse_tree2 as ps
import shunting_yard as sy

class Generator:
    def __init__(self):
        self.oprs = "+-*/"
        self.nums = ['1.419','3.348','7.52','51','12','0.318','0.2234','a','b','1.34','0.37'\
                    ,'b^2','i(12)','h(11.4)','o(b^2)','c(45)','d(30)','e(14)']   

    def genExp(self,length):
        exp = ""
        for i in range(length//2):
            exp += self.nums[random.randint(0,len(self.nums)-1)]
            exp += self.oprs[random.randint(0,3)]
        exp += self.nums[random.randint(0,len(self.nums)-1)]
        print(exp)
        return exp


if __name__ == '__main__':

    # inputs: m mathematical expressions each with length l
    test = Generator()
    inputs = []
    m, l = 20, 10
    for i in range(m):
        inputs.append(test.genExp(l))
    
    # time comparison
    # t1 = time.time()
    # ps_tree = ps.Calculator2()
    # for exp in inputs:
    #     ps_tree.calculate(exp) 
    # t2 = time.time()
    # print("Parse Tree:"+str(t2-t1))

    t3 = time.time()
    shunt_yrd = sy.Calculator3()
    for exp in inputs:
        shunt_yrd.calculate(exp)
    t4 = time.time()
    print("Shunting Yard:"+str(t4-t3))