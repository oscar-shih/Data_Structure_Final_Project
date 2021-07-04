# Input:    mathematical expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float
import numpy as np
import math
import time
import argparse

class Node1:
    def __init__(self, c):
        self.content = c
        self.parent  = None
        self.r_child = None
        self.l_child = None

class ParseTree1:
    def __init__(self, a):
        #print("self.angle is",a)
        self.angle = a
        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmnopq"
        self.ops = {'(':-1, '+':5, '-':5, '*':4, '/':4, '^':3, 'c':2, 'd':2,\
                    'e': 2, 'f':2, 'g':2, 'h':2, 'i':2, 'j':2, 'k':2, 'l':2,\
                    'm': 2, 'n':2, 'o':2, 'p':2, 'q':2 }
        self.root = Node1(None)
    
    
    def toNum(self, char):
        if(char == 'a'):    # pi
            return float(np.pi)
        if(char == 'b'):    # e
            return float(np.exp(1))


    def rank(self,expr):
        rk = []
        in_par = 0
        new_expr = []
        i = 0

        while i < len(expr):
            char = expr[i]
            if(char == '('):
                in_par += 1               

            elif(char == ')'):
                in_par -= 1
    
            elif(char in self.codes):
                rk.append(-10000000000000)
                new_expr.append(self.toNum(char))
            
            elif(char in self.nums):
                temp = ""
                while(i < len(expr) and expr[i] in self.nums):
                    temp += expr[i]
                    i += 1
                i -= 1
                
                rk.append(-10000000000000)
                new_expr.append(float(temp))
                
            elif(char in self.ops):
                rk.append(-in_par*6 + self.ops.get(char))
                new_expr.append(char)
            i += 1

        return rk, new_expr  

    def split(self, node, expr, rk):

        max = 0
        for i in range(len(expr)):
            if(rk[i] >= rk[max]):
                max = i

        if(rk[max] >= 4):
            max = 0
            for i in range(len(expr)):
                if(rk[i] > rk[max]):
                    max = i
  
        
        node.content = expr[max]
        node.r_child, node.l_child = Node1(None), Node1(None)
        node.r_child.parent, node.l_child.parent = node, node
        
        if(expr[:max]):
            self.split(node.l_child, expr[:max],   rk[:max])
        if(expr[max+1:]):
            self.split(node.r_child, expr[max+1:], rk[max+1:])

    def merge(self, node):
        if(type(node.content) == float):
            return node.content

        elif(str(node.content) in "+-*/^"):

            a = self.merge(node.r_child)
            b = self.merge(node.l_child)
            c = None

            if(node.content == '+'):
                c = a + b

            elif(node.content == '-'):
                c = a - b

            elif(node.content == '*'):
                c = a * b

            elif(node.content == '/'):
                c = a / b

            elif(node.content == '^'):
                c = a ** b
            
            #print(c,"=",a,node.content,b)
            return c
    
        elif(node.content in self.ops):
   
            A = self.merge(node.l_child)
            c = None

            if(node.content == 'c'):    # sin(x)
                if(self.angle):
                    c =  np.sin(A*np.pi/180)
                else:
                    c =  np.sin(A)

            elif(node.content == 'd'):    # cos(x)
                if(self.angle):
                    c =  np.cos(A*np.pi/180)
                else:
                    c =  np.cos(A)

            elif(node.content == 'e'):    # tan(x)
                if(self.angle):
                    c =  np.tan(A*np.pi/180)
                else:
                    c =  np.tan(A)
    
            elif(node.content == 'f'):    # arcsin(x)
                #if(self.angle):
                #    c =  np.arcsin(A)/np.pi*180
                #else:
                #    c =  np.arcsin(A)
                c = np.arcsin(A)

            elif(node.content == 'g'):    # arccos(x)
                #if(self.angle):
                #    c =  np.arccos(A)/np.pi*180
                #else:
                #    c =  np.arccos(A)
                c = np.arccos(A)

            elif(node.content == 'h'):    # arctan(x)
                #if(self.angle):
                #    c =  np.arctan(A)/np.pi*180
                #else:
                #    c =  np.arctan(A)
                c = np.arctan(A)

            elif(node.content == 'i'):    # square(x)
                c =  pow(A,2)

            elif(node.content == 'j'):    # cube(x)
                c =  pow(A,3)

            elif(node.content == 'k'):    # exp(x)
                c =  np.exp(A)

            elif(node.content == 'l'):    # square_root(x)
                c =  pow(A,(1/2))

            elif(node.content == 'm'):    # cubic_root(x)
                c =  pow(A,(1/3))

            elif(node.content == 'n'):    # log(x)
                c =  np.log10(A)

            elif(node.content == 'o'):    # ln(x)
                c =  np.log(A)

            elif(node.content == 'p'):    # abs(x)
                c =  abs(A)

            elif(node.content == 'q'):    # factorial(x)
                c =  math.factorial(int(abs(A)))
            
            #print(c,"=",node.content,"(",A,")")
            return c
    


    def output(self,expr):
        ranking, expr = self.rank(expr)
        self.split(self.root, expr[::-1], ranking[::-1])
        return self.merge(self.root)
        

class Calculator1:
    def __init__(self):
        self.rnd_to = 3
        self.angle = True
    
    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        

    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle

    def calculate(self, expr):
        tree = ParseTree1(self.angle)
        ans  = round(tree.output(expr), self.rnd_to)
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

    #test = Calculator1()
    #expr = "a/o(8*b^b)-e(80)-f(0.8)+f(0.8)+q(5)-i(11)+l(100)"        

    #t1 = time.time()
    #ans = test.calculate(expr)
    #t2 = time.time()
    #print(ans)
    #print("time:",t2-t1)
    #print()

    #test = Calculator1()
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

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default='./correctness/correct_1.txt',help="Input file root")
    parser.add_argument("--output", type=str, default='./ouput_1.txt', help="Output file root")
    args = parser.parse_args()
    Cal = Calculator1()
    Cal.main(args.input, args.output) 

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