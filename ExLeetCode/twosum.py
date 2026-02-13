def isPalindrome(x: int) -> bool:

    x = str(x)
    iv = []

    for l in x:
        iv.append(l)
    iv2 = iv[::-1]

    if iv == iv2:
        return True
    else:
        return False
    

print(isPalindrome(-121))