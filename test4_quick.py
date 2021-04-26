# 判斷input string 中是否有balance的fragment
# 所謂balance即指同時出現uppercase和lowercase
# 如果有balance fragment return fragment的最大長度，如果非balance return -1

# 較快速法
def check(checkstrings, full):
    for s in checkstrings:
        if s.islower() and s.upper() not in full:
            return False
        if s.isupper() and s.lower() not in full:
            return False
    return True

def change(s):
    if s.islower():
        return s.upper()
    if s.isupper():
        return s.lower()

def solution(S):
    # 如果全是lowercase或全是uppercase必定不balance
    if S.isupper() or S.islower():
        return -1

    strlist = list(S)
    temp_slice = ''
    result = ''

    if check(strlist[0], S) and check(strlist[0: strlist.index(change(strlist[0]))], S):
        temp_slice = strlist[0]
        result = strlist[0]

    for i in range(1, len(strlist)):
        if check(strlist[i], S):
            temp_slice += strlist[i]
            if check(temp_slice, temp_slice) and len(temp_slice) > len(result):
                result = temp_slice
        else:
            temp_slice = ""
        # print('temp_slice', temp_slice)
        # print('result:', result)

    if len(result) <= 1:
        return -1
    else:
        return len(result)

print(solution('sss'))
print(solution('FFF'))
print(solution('FsF'))
print(solution('azAaaBbaz'))
print(solution('TaccttAC'))
print(solution('aAaBazb'))
print(solution('azbbABZa'))
print(solution('GyYvugKk'))

# -1
# -1
# -1
# 6
# 8
# 3
# 8
# 2