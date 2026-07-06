#Count frequency of each character in a string.
text='banana'
textDict={}
for i in text:
    textDict[i] = textDict.get(i,0)+1
print(f"frequency of characters in '{text}' is {textDict}")