def is_lapindrome(s):
    mid = len(s) // 2

    first_half = sorted(s[:mid])
    second_half = sorted(s[mid:] if len(s) % 2 == 0 else s[mid + 1:])

    return first_half == second_half

print("gaga:", is_lapindrome("gaga"))
print("rotor:", is_lapindrome("rotor"))
print("hello:", is_lapindrome("hello"))
