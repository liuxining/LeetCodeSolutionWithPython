#liuxining
#2017年08月03日23:22:39



def thirdMax(nums):
    ns = set(nums)
    n = 1;
    max_val = ns.pop()
    max2_val = 'null'
    max3_val = 'null'
    for val in ns:
        if(val > max_val):
            max3_val = max2_val
            max2_val = max_val
            max_val = val
            if(n < 3):
                n += 1
        elif(n == 1 or val > max2_val):
            max3_val = max2_val
            max2_val = val
            n = 3
        elif(n == 2 or val > max3_val):
            max3_val = val
    if(n < 3):
        return max_val
    return max3_val

if __name__ == '__main__':
    print(thirdMax([2,2,3]))

