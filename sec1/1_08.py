def cipher(n:str):
    s =""
    for x in n:
        if 'a' <= x <= 'z':
            x = chr(219 - ord(x))
        s = s+x
    return s

"""
def cipher(s: str) -> str:
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)
"""

input_s = input("暗号化するよ")
output_s = cipher(input_s)
print(output_s)