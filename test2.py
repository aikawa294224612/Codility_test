# test2: 驗證安全密碼，條件:
# 1. 長度至少要6字
# 2. 不能包含空白
# 3. 至少要有一lower case
# 4. 至少要有一upper case
# 5. 至少要有一特殊字元(忘記有哪些了，以'!', '*', '%', '&'代表)
# 6. 至少包含一數字

special = ['!', '*', '%', '&']

def solution(S):
    check = {'lower': 0, 'upper': 0, 'digit': 0, 'special': 0}
    for s in S:
        if s.isupper():
            check['upper'] = 1
        if s.islower():
            check['lower'] = 1
        if s.isdigit():
            check['digit'] = 1
        if s in special:
            check['special'] = 1
    if len(S) >= 6 and ' ' not in S:
        for v in check.values():
            if v != 1:
                return False
    else:
        return False
    return True


print(solution('Du0 *'))
print(solution('Fu55*ss'))
print(solution('Fu55*'))
print(solution('fu55*fff'))

# Output:
# False
# True
# False
# False