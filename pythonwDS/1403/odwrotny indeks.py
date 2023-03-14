

def reversse_index(text, index):
    if 0 <= index <= (len(text) - 1):
        return index - len(text)
    else:
        return -999

print(reversse_index("hello",0))
print(reversse_index("hello",2))
print(reversse_index("hello",6))