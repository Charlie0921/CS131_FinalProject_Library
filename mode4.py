# library4
# ratio 순으로 sort (selection / merge ...)

def sortlist(ratio_comparison):
    order = len(ratio_comparison)
    for i in range(0, order):
        for j in range(0, order-i-1):
            if(ratio_comparison[j][1] < ratio_comparison[j+1][1]):
                temp = ratio_comparison[j]
                ratio_comparison[j] = ratio_comparison[j+1]
                ratio_comparison[j+1] = temp
    return ratio_comparison
