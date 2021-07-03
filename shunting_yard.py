# Reference: Shunting-yard Algorithm (Wikipedia) 
#            https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# 
# Input:    mathematical expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float
# ToDo:     error checking (complex numbers?)

import numpy as np
import math  
import time
import argparse

class Calculator3:

    def __init__(self):
        self.rnd_to = 3          # decimal points to round to
        self.angle = True      # True for Degrees, False for Radius

        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmnopq"
        self.ops = {'(':-1, '+':2, '-':2, '*':3, '/':3, '^':4, 'c':5, 'd':5,\
                    'e': 5, 'f':5, 'g':5, 'h':5, 'i':5, 'j':5, 'k':5, 'l':5,\
                    'm': 5, 'n':5, 'o':5, 'p':5, 'q':5 }
        # self.ops: operands/functions to corresponding precedence


    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        


    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle   

    
    def toNum(self, char):
        if(char == 'a'):    # pi
            return float(np.pi)
        if(char == 'b'):    # e
            return float(np.exp(1))
    

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
        if(func == 'c'):    # sin(x)
            if(self.angle):
                return np.sin(x*np.pi/180)
            return np.sin(x)

        if(func == 'd'):    # cos(x)
            if(self.angle):
                return np.cos(x*np.pi/180)
            return np.cos(x)

        if(func == 'e'):    # tan(x)
            if(self.angle):
                return np.tan(x*np.pi/180)
            return np.tan(x)

        if(func == 'f'):    # arcsin(x)
            return np.arcsin(x)

        if(func == 'g'):    # arccos(x)
            return np.arccos(x)

        if(func == 'h'):    # arctan(x)
            return np.arctan(x)

        if(func == 'i'):    # square(x)
            return pow(x,2)

        if(func == 'j'):    # cube(x)
            return pow(x,3)

        if(func == 'k'):    # exp(x)
            return np.exp(x)

        if(func == 'l'):    # square_root(x)
            return pow(x,(1/2))

        if(func == 'm'):    # cubic_root(x)
            return pow(x,(1/3))

        if(func == 'n'):    # log(x)
            return np.log10(x)

        if(func == 'o'):    # ln(x)
            return np.log(x)

        if(func == 'p'):    # abs(x)
            return abs(x)

        if(func == 'q'):    # factorial(x)
            return math.factorial(int(abs(x)))
        
        if(func == 'r'):    # deg(x)
            if(self.angle):
                return x/np.pi*180
            return x
    
        if(func == 's'):    # rad(x)
            if(self.angle):
                return x
            return x/180*np.pi

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
            elif(repr(i) >= repr('c') and repr(i) <= repr('q')):
                temp = self.funcOp(numStack[-1], i)
                numStack.pop()
            elif(type(i) == str):
                temp = self.operate(numStack[-2], numStack[-1], i)
                numStack.pop()  
                numStack.pop()
            else:
                print("exception!", i, type(i))
            #print(temp)
            numStack.append(temp)

        return round(numStack[0], self.rnd_to)

    def calculate(self, expr):
        ans = self.findVal(self.genRP(expr))
        # print(ans)
        return str(ans)
    def main(self, input_path, output_path):
        output = open(output_path, 'w')
        with open(input_path, 'r') as file_in:
            f = file_in.read().splitlines()
            t1 = time.time()
            for lines in f:
                ans = self.calculate(lines)
                output.write(ans)
                output.write('\n')
            t2 = time.time()
            print('time:'+str(t2-t1))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default='./input.txt',help="Input file root")
    parser.add_argument("--output", type=str, default='./ouput.txt', help="Output file root")
    args = parser.parse_args()
    Cal = Calculator3()
    Cal.main(args.input, args.output) 
    
    #test = Calculator3()
    #expr = [
    #"i(11)*p(10^2-2^10)+l(100)/a-j(10)-f(0.8)*h(37)*h(37)",
    #"f(0.8)/o(8*b^b)-o(8*b^b)*q(15)/f(0.8)*p(10^2-2^10)/q(15)*m(17)",
    #"i(11)-b-m(17)-h(37)*d(60)/b+l(100)+i(11)",
    #"a-k(2)*g(0.3)*j(10)/k(2)-l(100)/g(0.3)+k(2)",
    #"a/o(8*b^b)-e(80)-f(0.8)+f(0.8)+q(5)-i(11)+l(100)",
    #"m(17)*e(80)+d(60)-q(15)/j(10)*g(0.3)-n(3*10^7)*b",
    #"e(80)-e(80)/g(0.3)*k(2)*f(0.8)-j(10)-o(8*b^b)/g(0.3)",
    #"d(60)+d(60)/b*h(37)+c(30)+b+d(60)/b",
    #"a-o(8*b^b)/f(0.8)/c(30)+g(0.3)-g(0.3)-k(2)*l(100)",
    #"i(11)-h(37)*m(17)/m(17)+j(10)-i(11)-h(37)*i(11)",
    #"q(9)*n(3*10^7)+i(11)-d(60)*o(8*b^b)*d(60)+l(100)*d(60)",
    #"c(30)/p(10^2-2^10)+k(2)/a-f(0.8)*f(0.8)*f(0.8)*a",
    #"j(10)+p(10^2-2^10)+k(2)*c(30)+n(3*10^7)+d(60)*e(80)+m(17)",
    #"f(0.8)+c(30)/f(0.8)/b+l(100)+l(100)/f(0.8)/a",
    #"b/n(3*10^7)+i(11)-m(17)/g(0.3)+d(60)+m(17)/i(11)"
    #]
        
    #for x in expr:
    #    print(test.calculate(x))

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
#   p(): abs()
#   q(): factorial()
#   +:   addition
#   -:   subtraction
#   *:   multiplication
#   /:   division
#   ^:   power
#   .:   decimal point