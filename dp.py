# Input:    mathematical expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float
import numpy as np
import argparse
import math
import time

class Node4:
    def __init__(self, c):
        self.content = c
        self.parent  = None
        self.r_child = None
        self.l_child = None

class ParseTree4:
    def __init__(self, a):
        self.angle = a
        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmnopqr"
        self.ops = {'(':-1, '+':5, '-':5, '*':4, '/':4, '^':3, 'c':2, 'd':2,\
                    'e': 2, 'f':2, 'g':2, 'h':2, 'i':2, 'j':2, 'k':2, 'l':2,\
                    'm': 2, 'n':2, 'o':2, 'p':2, 'q':2, 'r':2 }
        self.root = Node4(None)
    
    
    def toNum(self, char):
        if(char == 'a'):    # pi
            return float(np.pi)
        if(char == 'b'):    # e
            return float(np.exp(1))

    def buildTree(self, expr):
        
        self.root.l_child = Node4(None)   # start from left child of root
        self.root.l_child.parent = self.root
        current = self.root.l_child

        if(expr[0] == '-'):
            expr = "0" + expr

        i = 0
        while i < len(expr):
            char = expr[i]  
            #print("CHAR",char)
            if(char in self.nums):
                temp = ""
                while(i < len(expr) and expr[i] in self.nums):
                    temp += str(expr[i])
                    i += 1
                i = i-1
                current.content = float(temp)
                current = current.parent
        
            elif(char == '['):
                temp = ""
                neg = False

                i += 1                
                if(expr[i] == '-'):
                    neg = True
                    i += 1

                while(i < len(expr) and expr[i] in self.nums):
                    temp += str(expr[i])
                    i += 1
                i = i-1
                current.content = float(temp)
                if(neg):
                    current.content *= -1
                current = current.parent

            elif(char in self.codes):
                current.content = self.toNum(char)
                current = current.parent

            elif(char in self.funcs):
                current.content = char
                current.l_child = Node4(None)
                current.l_child.parent = current
                current = current.l_child

            elif(char in self.ops):
                if(not current.content):
                    current.content = char
                    new_node = current
                   
                elif(self.ops.get(char) < self.ops.get(current.content) or (char == "^" and current.content not in self.funcs)):
                    new_node = Node4(char)
                    if(current.r_child):    
                        #print(char,current.content,"goes BOTTOM RIGHT")
                        new_node.l_child, new_node.l_child.parent = current.r_child, new_node
                        current.r_child, new_node.parent = new_node, current
  
                    else:
                        #print(char,"goes BOTTOM LEFT")
                        new_node.l_child, new_node.l_child.parent =  current.l_child, new_node
                        current.l_child, new_node.parent = new_node, current
      
                else:
                    #print(char,"goes UP")
                    new_node = Node4(char)
                    while(current.parent and current.parent.content and\
                    self.ops.get(char) >= self.ops.get(current.parent.content)):
                        current = current.parent
                    if(current.parent):
                        new_node.parent = current.parent
                        if(current.parent.l_child == current):
                            current.parent.l_child = new_node
                        elif(current.parent.r_child == current):
                            current. parent.r_child  = new_node

                    new_node.l_child = current
                    current.parent = new_node

                new_node.r_child = Node4(None)
                new_node.r_child.parent = new_node
                current = new_node.r_child
            i += 1

        while(self.root.parent):
            self.root = self.root.parent
        if(self.root.content == None):
            self.root.content = 'r'

    def eval(self, node):
        cmd = node.content
        #print(cmd)
        if(type(cmd) == float):
            return cmd
        
        if(cmd in "+-*/^"):
            a = self.eval(node.l_child)
            b = self.eval(node.r_child)
            c = None
            
            if(cmd == '+'):
                c = a + b
            elif(cmd == '-'):
                c = a - b
            elif(cmd == '*'):
                c = a * b
            elif(cmd == '/'):
                c = a / b
            elif(cmd == '^'):
                c = a ** b
            
            #print(c,"=",a,cmd,b)
            return c
        
        elif(cmd in self.ops):
            
            a = self.eval(node.l_child)
            c = None

            if(cmd == 'c'):    # sin(x)
                if(self.angle):
                    c = np.sin(a*np.pi/180)
                else:
                    c = np.sin(a)

            elif(cmd == 'd'):    # cos(x)
                if(self.angle):
                    c = np.cos(a*np.pi/180)
                else:
                    c = np.cos(a)

            elif(cmd == 'e'):    # tan(x)
                if(self.angle):
                    c = np.tan(a*np.pi/180)
                else:
                    c = np.tan(a)

            elif(cmd == 'f'):    # arcsin(x)
                c = np.arcsin(a)

            elif(cmd == 'g'):    # arccos(x)
                c = np.arccos(a)

            elif(cmd == 'h'):    # arctan(x)
                c = np.arctan(a)

            elif(cmd == 'i'):    # square(x)
                c = pow(a,2)

            elif(cmd == 'j'):    # cube(x)
                c = pow(a,3)

            elif(cmd == 'k'):    # exp(x)
                c = np.exp(a)

            elif(cmd == 'l'):    # square_root(x)
                c = pow(a,(1/2))

            elif(cmd == 'm'):    # cubic_root(x)
                c = pow(a,(1/3))

            elif(cmd == 'n'):    # log(x)
                c = np.log10(a)

            elif(cmd == 'o'):    # ln(x)
                c = np.log(a)

            elif(cmd == 'p'):    # abs(x)
                c = abs(a)

            elif(cmd == 'q'):    # factorial(x)
                c = math.factorial(int(abs(a)))

            elif(cmd == 'r'):    # void root
                c = a
            
            #print(c,"=",cmd,"(",a,")")
            return c

    def output(self):
        return self.eval(self.root)
        

class Calculator4:
    def __init__(self):
        self.rnd_to = 3
        self.angle = True
        self.funcs = "cdefghijklmnopq"
    
    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        

    def changeAngle(self):           # evaluate angle in degrees/radius
        self.angle = not self.angle

    def findVal(self, string):               # find value of expression withou parantheses
        #print("STRING",string)
        tree = ParseTree4(self.angle)
        tree.buildTree(string)
        return str(tree.output())

    
    def do_(self, string):    
        
        start, end = None, -1
        new_string = ""
        i = 0
        func = False
        in_par = 0

        while(i < len(string)):
            if(string[i] == '('):
                if(in_par == 0):
                    start = i
                    new_string += string[end+1: start]
                in_par += 1
          
            elif(string[i] == ')'):
                in_par -= 1
                if(in_par == 0):
                    end = i
                    new_string = new_string + "[" + str(self.do_(string[start+1:end])) + "]" 
            i += 1
        
        new_string += string[end+1:]
        return self.findVal(new_string)

    def calculate(self,string):
        #print(string)
        return str(round(float(self.do_(string)), self.rnd_to))

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

    #test = Calculator4()
    #print(test.calculate("6.685*g(((2.964/8.47*0.813/4.267))/1000)*5.291"))    

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default='./correctness/correct_1.txt',help="Input file root")
    parser.add_argument("--output", type=str, default='./ouput_1.txt', help="Output file root")
    args = parser.parse_args()
    Cal = Calculator4()
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
