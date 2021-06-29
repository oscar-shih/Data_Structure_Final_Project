# translates notations used in code to readable ones for verification in google calculator
# Input:  string
# Output: string

def translate(input):
    output = ""
    cube, cbrt = 0, 0 
    cube_par, cbrt_par = [],[]
    # cube: 'j'/cube()
    # cbrt: 'm'/cube_root()

    for char in input:
        if(char == 'a'):      # pi
            output += "pi"

        elif(char == 'b'):
            output += "e"

        elif(char == 'c'):    # sin(x)
            output += "sin"

        elif(char == 'd'):    # cos(x)
            output += "cos"

        elif(char == 'e'):    # tan(x)
            output += "tan"

        elif(char == 'f'):    # arcsin(x)
            output += "arcsin"

        elif(char == 'g'):    # arccos(x)
            output += "arccos"

        elif(char == 'h'):    # arctan(x)
            output += "arctan"

        elif(char == 'i'):    # square(x)
            output += "sqr"

        elif(char == 'j'):    # cube(x)
            cube += 1
            cube_par.append([])

        elif(char == 'k'):    # exp(x)
            output += "exp"

        elif(char == 'l'):    # square_root(x)
            output += "sqrt"

        elif(char == 'm'):    # cubic_root(x)
            cbrt += 1
            cbrt_par.append([])

        elif(char == 'n'):    # log(x)
            output += "log"

        elif(char == 'o'):    # ln(x)
            output += "ln"

        elif(char == 'p'):    # abs(x)
            output += "abs"

        elif(char == 'q'):    # factorial(x)
            output += "factorial"
    
        elif(char == 'r'):
            continue
    
        else:
            output += str(char)
            if(cube):
                if(char == '('):
                    cube_par[-1].append(1)
                elif(char == ')'):
                    cube_par[-1].pop()
                    if(not cube_par[-1]):
                        cube -= 1
                        cube_par.pop()
                        output += "^3"
  
            if(cbrt):
                if(char == '('):
                    cbrt_par[-1].append(1)
                elif(char == ')'):
                    cbrt_par[-1].pop()
                    if(not cbrt_par[-1]):
                        cbrt -= 1   
                        cbrt_par.pop()         
                        output += '^(1/3)'
    return output

if __name__ == "__main__":
    expr1 = "a+b+c(50)+d(40-e(20))"
    expr2 = "f(g(0.4)^h(0.2)/100)"
    expr3 = "i(2)+j(45+j(20-5))*k(15-j(2))+l(15-m(m(24)))"
    expr4 = "p(r(a/4)*s(45)-q(2)+n(100)-o(b^2))"
    
    print(translate(expr1))
    print(translate(expr2))
    print(translate(expr3))
    print(translate(expr4))

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
#   r(): deg()
#   s(): rad()
#   +:   addition
#   -:   subtraction
#   *:   multiplication
#   /:   division
#   ^:   power
#   .:   decimal point