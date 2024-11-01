import sys

input = sys.stdin.readline

def main():
    s = input().rstrip()
    ans = ''
    
    for i in s:
        if i.isalpha():  
            base = ord('A') if i.isupper() else ord('a')  
            tmp = ord(i) - base + 13
            tmp = tmp % 26 + base  
            ans += chr(tmp)
        else:
            ans += i  
    return ans
                
if __name__ == "__main__":
    print(main())