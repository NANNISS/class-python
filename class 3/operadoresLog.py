'''
OPERADORES LOGICOS
'''

a=30
b=40
c=30

r=((a<b) and (b>c))
print("r:",r) #AND

print("-----------------")
r=((a<b) or (b>c))
print("r:",r) #OR

print("-----------------")
r=not(a<b) or (c<a)
print("r:",r) #NOT

#print("-----------------")
#r=(a<b)

