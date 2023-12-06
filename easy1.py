def lastword(s):
    word=s.split()
    if word:
        return len(word[-1])
    else:
        return 0

inputstring=input("enter a string:")
result=lastword(inputstring)
print(result)

