import time
import random as rd
import numpy  as np
import shunting_yard as sy


class Generator2:

    def __init__(self, dcml, p_limit, i_limit, prob_op, prob_nm, prob_par, calculator): 
        self.funcs = "cdefghijklmnopqr"
        self.ops   = "+-*/^"
        self.dec   = dcml       # maximal digits behind decimal point
        self.p_lmt = p_limit    # higher and lower bound of values in pool
        self.i_lmt = i_limit    # higher and lower bound of initial nums
        self.p_op  = prob_op    # probability of occurence of operands <=> functions
        self.p_nm  = prob_nm    # probability of occurence of numbers  <=> e, pi
        self.p_pr  = prob_par   # probability of occurence of paranthesis
        self.cal   = calculator
        self.pool  = []


    def randNum(self):          # random number
        string = ""
        chance = rd.random()
        if(chance <= self.p_nm):
            string = str( round( rd.randint(1, 10**self.dec)/(10**self.dec)\
            + rd.randint(0, self.i_lmt-1), self.dec) )

        elif(chance >= self.p_nm + (1-(self.p_nm/2))):
            string = str(round(np.pi, self.dec))

        else:
            string = str(round(np.e, self.dec))

        return string


    def randPar(self, string):  # add paranthesis or not
        chance = rd.random()
        if(chance <= self.p_pr):
            string = "(" + string + ")"
        return string
    

    def randOpFunc(self):       # random operand or function
        string = ""
        chance = rd.random()

        if chance <= self.p_op: 
            string = self.ops[rd.randint(0, 4)]
            
            # for '^': abs(X) ^ log(abs(Y)) to avoid complex numbers and overflowing
            if(string == "^"):              
                string = "p(" + self.pool[rd.randint(0, len(self.pool)-1)] + ")"\
                         + string + "n(p(" + self.pool[rd.randint(0, len(self.pool)-1)] + "))"
            else:
                string = self.pool[rd.randint(0, len(self.pool)-1)] + string \
                         + self.pool[rd.randint(0, len(self.pool)-1)]

        else:                   
            string = self.funcs[rd.randint(0, 15)]
            input = self.pool[rd.randint(0, len(self.pool)-1)]
  
            # positive input for sqrt(), ln(), log()
            if(string in "lmno"):
                string =  string + "(p(" + input + "))"
        
                
            # -1 <= input <= 1 for arcsin(), arccos()
            elif(string in "fg"):
                string = string + "((" + input + ")/" + str(self.p_lmt) + ")"
                            
            else:
                string = string + "(" + input + ")"

        return string


    def genSeed(self):          # generates seeds for pool
        string = self.randNum()
        string = self.randPar(string)
        return string


    def feedPool(self, qty):    # feed pool with entries 
        
        if(not self.pool):      # if pool is empty, generate seeds
            for i in range(qty):
                self.pool.append(self.genSeed())  
            print("SEED INITIALIZED\n")
        
        else:                   # else, generate new entries from old ones
            fed = 0
            for i in range(qty):
                expr = self.randOpFunc()
                ans = self.cal.calculate(expr)

                if(ans != "nan" and -1*self.p_lmt <= float(ans) and self.p_lmt >= float(ans)):
                    fed += 1
                    expr = self.randPar(self.randOpFunc())
                    self.pool.append(expr)

            print("\nACCEPTANCE RATE:", round(fed*100/qty,2), "%")

        return self.pool
                
if __name__ == "__main__":

    shunt_yrd = sy.Calculator3()
    test = Generator2(3, 1000, 10, 0.8, 0.95, 0.2, shunt_yrd)
    # dcml, p_limit, i_limit, prob_op, prob_nm, prob_par, calculator

    it = 5
    qty = 40
    for i in range(it):
        test.feedPool(qty)
    
    print("\n",test.pool)