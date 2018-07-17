import re

# 1-2 * ((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))

source = input('>>')

def check(s):
    flag = True
    if  re.findall('[a-zA-Z]',s):
        print('Invalid')
        flag = False
    return flag

def format(s):
    s = s.replace(' ','')
    s = s.replace('++','+')
    s = s.replace('+-', '-')
    s = s.replace('--', '+')
    s = s.replace('-+', '-')
    return s

def cal_mul_div(s):
    while  re.search('[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*',s):
        # print(re.search('[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*',s))
        ret1 = re.search('[\-]?\d+\.?\d*[*/][\-]?\d+\.?\d*', s).group()
        x, y = re.split('[*/]', ret1)
        if ret1.find('*') != -1:
            ret2 = float(x) * float(y)
        else:
            ret2 = float(x) / float(y)
        ret2 = str(ret2)
        s = s.replace(ret1, ret2)
    return s

def cal_add_sub(s):
    while re.search('[\-]?\d+\.?\d*[+\-][\-]?\d+\.?\d*', s):
        ret1 = re.search('[\-]?\d+\.?\d*[+\-][\-]?\d+\.?\d*', s).group()
        if ret1.find('+') != -1:
            x, y = re.split('[+]', ret1)
            ret2 = float(x) + float(y)
        else:
            numbers = re.split('[\-]', ret1)
            if  len(numbers) == 3:
                ret2 = 0
                for v in numbers:
                    if  v:
                        ret2 -= float(v)
            else:
                x, y = re.split('[\-]', ret1)
                ret2 = float(x) - float(y)
        ret2 = str(ret2)
        s = s.replace(ret1, ret2)
    return s

if check(source):
    source = format(source)
    while re.search('\(',source):
        strs = re.search('\([^()]+\)',source).group()
        strs1 = cal_mul_div(strs)
        strs1 = cal_add_sub(strs1)
        source = format(source.replace(strs,strs1[1:-1]))
    else:
        strs = cal_mul_div(source)
        strs = cal_add_sub(strs)
    print(strs)
