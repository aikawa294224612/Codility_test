# 給一數字，在其中加一個5使其最大

def solution(N):
    if N == 0:
        return int('5'+str(N))
    # 考時時完全沒去判斷負數...
    if N < 0:
        listN = list(str(-N))
        for i in range(len(listN)):
            if int(listN[i]) > 5:
                listN.insert(i, '5')
                return -int(''.join(listN))
        # 如果都沒配到，最後面加5
        listN.append('5')
        return -int(''.join(listN))
    if N > 0:
        listN = list(str(N))
        for i in range(len(listN)):
            if int(listN[i]) < 5:
                listN.insert(i, '5')
                return int(''.join(listN))
        listN.append('5')
        return int(''.join(listN))


print(solution(263))
print(solution(653))
print(solution(528))
print(solution(999))
print(solution(-999))
print(solution(-535))
print(solution(-253))
print(solution(0))

# Output:
# 5263
# 6553
# 5528
# 9995
# -5999
# -5355
# -2535
# 50
