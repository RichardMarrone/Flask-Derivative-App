def get_vals(eq,s,r):
    X = []
    Y = []
    for x in range(s,r+1):
        X.append(x)
        Y.append(eval_func(eq,x))

    return X,Y


def eval_func(eq,x):
    res = 0
    for item in eq:
        res+= item[0]*(x ** item[1])

    return res

##perform the power rule on formated eq list
def derive(eq):
    d = []
    for i in range(len(eq)):
        if eq[i][1] == 0:
            pass
        else:
            co = eq[i][0]
            power = eq[i][1]
            d.append((co*power,power-1))

    return d
##take string of user input and convert to format for evaluation
def parse_input(inp):
    e = []
    inp = inp.split()
    #coefficient and power
    co = 0
    power = 0

    #keeps track of whether or not term is negative. 1 = positive, -1 = negative
    negative = 1
    
    for term in inp:
        if term == '+':
            continue

        if term == '-':
            negative = -1
            continue

        
        if 'x' in term:
            temp = term.split('x')[0]
            if temp == '':
                co = 1
            elif temp == '-':
                co = -1
            else:
                co = float(temp)* negative

            if '^' in term:
                power = float(term.split('^')[1])
                if power < 0:
                    raise Exception
            else:
                power = 1
            
        else:
            co = float(term) * negative
            power = 0
            
        e.append((co,power))
        
        #reset negative back to one
        negative = 1

    return e

def print_func(eq):
    res = ''
    item_count = 0
    negative = 1
    for item in eq:
        if item_count != 0:
            if item[0] < 0:
                res += '-'
                negative = -1
            else:
                res += '+'
                negative = 1
        if item[1] == 0:
            if item[0] != 0:
                res += ' {} '.format(item[0]*negative)
        elif item[1] == 1:
            if item[0] == 1:
                res+= ' x '
            else:
                res += ' {}x '.format(item[0]*negative)
        else:
            if item[0] == 1:
                res += 'x^{}'.format(item[1])
            else:
                res+= ' {}x^{} '.format(item[0]*negative,item[1])
            
        negative = 1
        item_count += 1

    if len(res) == 0:
        res = 0
    return res

def gen_latex(eq):
    res = '\('
    item_count = 0
    negative = 1
    for item in eq:
        if item_count != 0:
            if item[0] < 0:
                res += '-'
                negative = -1
            else:
                res += '+'
                negative = 1
        if item[1] == 0:
            if item[0] != 0:
                res += ' {} '.format(item[0]*negative)
        elif item[1] == 1:
            if item[0] == 1:
                res += ' x '
            else:
                res += ' {}x '.format(item[0]*negative)
        else:
            if item[0] == 1:
                res += " x^{"+str(item[1])+'}'
            else:
                res+= " {}x^".format(item[0]*negative)+'{'+str(item[1])+'}'
            
        negative = 1
        item_count += 1

    if res == '\(':
        res += '0'
    
    res += '\)'
    return res
