def solution(total_lambs):
    if total_lambs < 125:
        return 1
    if total_lambs  <10:
        return 0
    if total_lambs>=pow(10,9):
        return 0
    
    max_count = 1 
    max_sum = 1
    index1 = 0
    max_list=[max_sum]

    while(max_sum+max_list[index1]*2<=total_lambs):
        temp = max_list[index1]*2
        max_sum+=temp
        index1+=1
        max_count+=1
        max_list.append(temp)

    #fibo
    t1 = 1
    t2 = 1
    min_count=2
    min_sum = 2
    min_list=[t1, t2]
    index2 = 1
    while(min_sum<=total_lambs):
        temp = min_list[index2]+min_list[index2-1]
        if temp+min_sum>total_lambs:
            break
        min_list.append(temp)
        index2+=1
        min_sum+=temp
        min_count+=1
    return (min_count-max_count)
