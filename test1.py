# test1: 限制字數，輸出須完整字，且結尾不可為空白
def solution(message, K):
    # 如果input字數小於K，額需考慮直接return
    if len(message) <= K:
        return message
    str_list = message.split(' ')
    str_list_num = [len(i) for i in str_list]

    total = 0
    result = ''

    # 在考試的時候太急，寫了if total + str_list_num[i]+1 <= K+1
    # 應該是在下一次才計算空格
    for i in range(len(str_list_num)):
        if total + str_list_num[i] <= K-1:
            total += str_list_num[i]
            if result == '':
                result += str_list[i]
            else:
                result += ' ' + str_list[i]
    return result


print(solution('Be the first to submit a golden', 14))
print(solution('We announce coming challenges via newsletter', 17))

# Output:
# Be the first to a
# We announce coming