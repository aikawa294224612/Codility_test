# Codility_test
人生第一次考這種，雖然結束了然後緊張爆就亂寫，但事後該做的還是要做，就在把這四題平心靜氣寫完吧

### Test 1: 限制字數，輸出須完整字，且結尾不可為空白
input: message, K

output: string (完整字，且結尾不可為空白)

- message: string 
- K: 限制的字數

### Test 2: 驗證安全密碼，條件:

1. 長度至少要6字
2. 不能包含空白
3. 至少要有一lower case
4. 至少要有一upper case
5. 至少要有一特殊字元(忘記有哪些了，以'!', '*', '%', '&'代表)
6. 至少包含一數字

input: S (string)

output: True/ Fasle

### Test 3: 給一數字，在其中加一個5使其最大

這題在作答時太粗心了...負數完全沒判斷(完全不知道在幹嘛...)

input: N (int)

output: int (加上5的數字)

### Test 4: 判斷input string 中是否有balance的fragment，所謂balance即指同時出現uppercase和lowercase

考試的時候寫道這題還有半小時，想說太好了還有時間回去驗證...結果這題爆掉了...
在最後8分鐘才想到要用甚麼方法，直接用飆的，(當然最後沒寫完，0分收場)

input: S (string)

output: int (如果有balance fragment return fragment的最小長度，如果非balance return -1)
