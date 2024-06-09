#level1-T5
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "123"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
