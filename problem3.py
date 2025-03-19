f=open("poem.txt")
content=f.read()
if("twinkle" in content):
    print("twinkle is present in the poem")
else:
    print("twinkle is not present in the poem")
f.close()