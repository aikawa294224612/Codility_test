# 判斷input string 中是否有balance的fragment
# 所謂balance即指同時出現uppercase和lowercase
# 如果有balance fragment return fragment的最小長度，如果非balance return -1

# 因不注意效能，先使用窮舉法代替
def check(checkstrings):
    for s in checkstrings:
        if s.islower() and s.upper() not in checkstrings:
            return False
        if s.isupper() and s.lower() not in checkstrings:
            return False
    return True

def solution(S):
    # 如果全是lowercase或全是uppercase必定不balance
    if S.isupper() or S.islower():
        return -1
    strlist = list(S)
    result = []
    for i in range(len(strlist)):
        for j in range(i+1, len(strlist)+1):
            if check("".join(strlist[i:j])):
                result.append("".join(strlist[i:j]))
    if not result:
        return -1
    return max([len(i) for i in result])

print(solution('sss'))
print(solution('FFF'))
print(solution('FsF'))
print(solution('azAaaBbaz'))
print(solution('TaccttAC'))
print(solution('aAaBazb'))