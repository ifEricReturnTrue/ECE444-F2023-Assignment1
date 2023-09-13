def reversed(num):
    num_list=[]
    neg = False
    result = 0
    if num < 0:
        neg = True
        num = num * -1
    while num != 0:
        num_list.append(num%10)
        num = num // 10
    for i in range (len(num_list)):
        result = result + num_list[i] * (10**(len(num_list) - i - 1))
    if neg == True:
            result = result*-1
    return result

def formatter(num):
    return bin(num), oct(num)