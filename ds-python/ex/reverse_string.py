# Problem: print a string in veverse order

def print_reverse1(s):
    print(s[::-1])

def print_reverse(s):
    left = 0
    right = len(s) - 1
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1
    print(s)

if __name__ == "__main__":
    str1 = ['r', 'e', 'v', 'e', 'r', 's', 'e']
    print_reverse1(str1)
    print_reverse(str1)
