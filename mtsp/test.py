a=[0,1,2,3,4,5,6,7,8,9]
i=4
j=7
r=a[i:j+1]
a=a[:i]+a[j+1:]
print(len(a))
print(len(r))
print(10-(j-i+1))
