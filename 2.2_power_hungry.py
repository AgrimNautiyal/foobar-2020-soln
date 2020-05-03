def solution(xs):
    #first find product of all positive values in xs
    l=[i for i in xs if i>0]
    zero_test = [0 for i in xs if i == 0]
    if l == zero_test:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])
    #to test for presence of single power drain source:
    count_neg = 0
    count_zero = 0
    for i in xs:
        if i<0:
            count_neg+=1
        elif i == 0:
            count_zero+=1
    if count_neg == 1 and count_zero == len(xs)- 1:
        return str(0)
    product = 1
    for i in l:
        product*=i

    #now to find product of negative values and select even no of values (from large to small)
    k = [i for i in xs if i<0]
    if len(k) < 2:
        return str(product) #no scope of increasing value of product
    else:
        k = sorted(k)
        if len(k)%2==0: #in case of even no of negative values, directly find product
            product2 = 1
            for i in k:
                product2*=i
            return str(product*product2)
        else:
            len_consider = len(k)-1 #this is the most immediate lesser even no to the odd length of the negative value list
            k = k[0:len_consider]
            product2 = 1
            for i in k:
                product2*=i
            return str(product*product2)
