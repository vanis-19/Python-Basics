s=input("enter name")
s=s.split()
s=s[::-1]
output=''.join(s)
print(output)

'''i=len(s)-1
output=" "
while i>0:
    output=output+s[i]
    i=i-1
print(output)

r=reversed(s)
output="".join(r)
print(output)'''

i=len(s)-1
while i>0:
    print(s[i])
    i=i-1


