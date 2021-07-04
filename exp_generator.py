import random
import time
import parse_tree2 as ps
import shunting_yard as sy

class Generator:
    def __init__(self):
        self.oprs = "+-*/"
        self.nums = ['a^a', 'a+b', 'b^3', 'c(140.5)', 'd(138)', 'e(237)','f(0.123)', 'g(0-0.4265)','h(72)','i(6.666)', 'j(7.777)', 'k(8)', 'l(878791)', 'm(11174148)', 'n(8*10^9-3.19*10^7)', 'o(8*a+b^b)', 'p(18^2-3^11)', 'q(q(3))']
    def genExp(self, length):
        exp = ""
        for i in range(length//2):
            exp += self.nums[random.randint(0, len(self.nums)-1)]
            exp += self.oprs[random.randint(0, 3)]
        exp += self.nums[random.randint(0, len(self.nums)-1)]
        return exp


if __name__ == '__main__':

    # inputs: m mathematical expressions each with length l
    test = Generator()
    inputs = []
    path = 'correct_5.txt'
    f = open(path, 'w')
    m, l = 15, 19
    for i in range(m):
        print(test.genExp(l), file=f)
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