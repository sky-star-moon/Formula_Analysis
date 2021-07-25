#+-* \frac \sqrt ^ \sin
from collections import defaultdict
p_level = {'+':10,'-':10,'*':15,'{':1,'}':1,'(':1,')':1,'^':20,'frac':15,'sin':1,'sqrt':50,'no_opt':-1}
p_level = defaultdict(int,p_level)
def pre_process(formula):
    ans = ['start']
    for i in range(len(formula)):
        temp = formula[i]
        if temp in ['+','-','*','{','}','(',')','^']:
            ans.append(temp)
        elif temp == '\\':
            if formula[i:i+4] in ['\\sin']:
                ans.append('sin')
            elif formula[i:i+5] in ['\\frac','\\sqrt']:
                ans.append( formula[i+1:i+5] )
        elif temp.isdigit():
            if isinstance(ans[-1],int):
                ans.append(ans.pop()*10 + int(temp))
            else:
                ans.append(int(temp))
        print('i = ',i)
    ans.append('end')
    print(ans)
    return ans
def jisuan( opt,num,i=1):
    if opt.pop() == '+':
        return num.pop() + num.pop(),i
    elif opt.pop() == '-':
        return num.pop() - num.pop(),i
    elif opt.pop() == '*':
        return num.pop() * num.pop(),i
    #-----------------------------------------
    elif opt.pop() == '^':
        x2 = num.pop()
        x1 = num.pop()
        return pow(x1 , x2),i
    #---------------------------
    elif opt.pop() == '{':
        opt.append('{')
        return num.pop(),i+1
    elif opt.pop() == '(':
        opt.append('(')
        return num.pop(),i+1
    elif opt == 'sqrt':
        return pow(num.pop(),0.5),i


if __name__ == '__main__':
    s = ['start']
    str = '\\sqrt{{(\\sqrt{3^2}+3)*(2+1)}*{6}}'
    Formula = pre_process(str)
    num = []
    opt = ['no_opt']
    #for i in range(len(Formula)):
    i = 1
    current = Formula[i]
    while(True):
        if  isinstance(current,int) or isinstance(current,float):
            num.append(current)
            if p_level[ opt[-1] ] >= p_level[ Formula[i+1] ]:#可计算
                temp,_ = jisuan( opt, num,i)
                current = temp
            else:
                i = i + 1
                current = Formula[i]
        else:
            if current == 'end':
                break
            if current == '}' or current == ')':
                temp,_ = jisuan( opt.pop(), num )
                current = temp
            else:
                opt.append(current)
                i = i + 1
                current = Formula[i]
        if i+1 == len(Formula):
            break
        print(num)
    print(num)