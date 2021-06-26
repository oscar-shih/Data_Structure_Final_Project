# Reference: Shunting-yard Algorithm (Wikipedia) 
#            https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# 
# Input:    expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float
# ToDo:     1. conversion of complex types (any complex results would be displayed as 'nan' for now)
#           2. conversion of degrees and radius
#           3. absolute values
#           4. factorials
#           5. features for complex numbers

import numpy as np

class Calculator:

    def __init__(self):
        self.rnd_to = 10
        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmn"
        self.ops = {'(':-1, '+':2, '-':2, '*':3, '/':3, '^':4, 'c':5, 'd':5,\
                    'e': 5, 'f':5, 'g':5, 'h':5, 'i':5, 'j':5, 'k':5, 'l':5,\
                    'm': 5, 'n':5, 'o':5 }
 
    
    def toNum(self, char):
        if(char == 'a'):
            return np.pi
        if(char == 'b'):
            return np.exp(1)
    

    def genRP(self, expr):  # converts inflix to reverse polish
        rp_stack = []       # stack
        operators = []      # queue 

        i = 0
        while(i < len(expr)):         # shunting yard algorithm

            char = expr[i]
            if(char in self.codes):   
                rp_stack.append(self.toNum(char))
                
            elif(char in self.nums): 
                temp = ""
                while(i < len(expr) and expr[i] in self.nums):
                    temp += str(expr[i])
                    i += 1
                i = i-1
                rp_stack.append(float(temp))

            elif(char == '('):      
                operators.append(char)

            elif(char in self.ops): 
                # '^' is exception for it is evaluated from right to left
                while(operators and self.ops.get(char) <= self.ops.get(operators[-1])\
                and (char != '^' or operators[-1] != '^')): 
                    rp_stack.append(operators[-1])
                    operators.pop()
                operators.append(char)

            elif(char == ')'):   
                while(operators[-1] != '('):
                    rp_stack.append(operators[-1])
                    operators.pop()
                operators.pop()

            i += 1
            #for j in rp_stack+operators[::-1]:
            #    print(j, end = " ")
            #print()

        return rp_stack + operators[::-1]

    
    def funcOp(self, x, func):      # functions
        if(func == 'c'):    # sin()
            return np.sin(x*np.pi/180)
        if(func == 'd'):    # cos()
            return np.cos(x*np.pi/180)
        if(func == 'e'):    # tan()
            return np.tan(x*np.pi/180)
        if(func == 'f'):    # arcsin()
            return np.arcsin(x)/np.pi*180
        if(func == 'g'):    # arccos()
            return np.arccos(x)/np.pi*180
        if(func == 'h'):    # arctan()
            return np.arctan(x)/np.pi*180
        if(func == 'i'):    # square()
            return pow(x,2)
        if(func == 'j'):    # cube()
            return pow(x,3)
        if(func == 'k'):    # exp()
            return np.exp(x)
        if(func == 'l'):    # square_root()
            return pow(x,(1/2))
        if(func == 'm'):    # cubic_root()
            return pow(x,(1/3))
        if(func == 'n'):    # log()
            return np.log10(x)
        if(func == 'o'):    # ln()
            return np.log(x)

    def operate(self, x, y, op):    # operand calculation
        if(op == '+'):
            return x + y
        if(op == '-'):
            return x - y
        if(op == '*'):
            return x * y
        if(op == '/'):
            return x / y
        if(op == '^'):
            return pow(x,y)
    

    def findVal(self, rp): # derive output from rp stack
        numStack = []
        for i in rp:
            temp = None
            if(type(i) == float): 
                temp = i
            elif(ascii(i) >= ascii('c') and ascii(i) <= ascii('o')):
                temp = self.funcOp(numStack[-1], i)
                numStack.pop()
            elif(type(i) == str):
                temp = self.operate(numStack[-2], numStack[-1], i)
                numStack.pop()  
                numStack.pop()
            #print(temp)
            numStack.append(temp)

        return round(numStack[0], self.rnd_to)

    def calculate(self, expr):
        return self.findVal( self.genRP(expr) )
         

if __name__ == "__main__":
    test = Calculator()
    expr = "i(20)+k(i(3))"
    print(expr,'=')
    print(test.calculate(expr))

# function/operator:notation
#   a:   pi
#   b:   e
#   c(): sin()
#   d(): cos()
#   e(): tan()
#   f(): arcsin()
#   g(): arccos()
#   h(): arctan()
#   i(): square()
#   j(): cube()
#   k(): exp()
#   l(): square_root()
#   m(): cubic_root()
#   n(): log()
#   o(): ln()
#   +:   addition
#   -:   subtraction
#   *:   multiplication
#   /:   division
#   ^:   power
#   .:   decimal point