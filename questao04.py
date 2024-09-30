#questao04   sequencias em python.

# a) 1, 3, 5, 7, ___ 
a = [1, 3, 5, 7]
a.append(a[-1] + 2)  

# resposta 9

# b) 2, 4, 8, 16, 32, 64, ____ 
b = [2, 4, 8, 16, 32, 64]
b.append(b[-1] * 2) 

# resposta 128

# c) 0, 1, 4, 9, 16, 25, 36, ____ 
c = [0, 1, 4, 9, 16, 25, 36]
c.append((len(c)) ** 2)

# resposta 49

# d) 4, 16, 36, 64, ____ 
d = [4, 16, 36, 64]
next_even = (len(d) + 2) * 2  
d.append(next_even ** 2) 

# resposta 144

# e) 1, 1, 2, 3, 5, 8, ____ 
e = [1, 1, 2, 3, 5, 8]
e.append(e[-1] + e[-2])  

# resposta 13

# f) 2, 10, 12, 16, 17, 18, 19, ____ 
f = [2, 10, 12, 16, 17, 18, 19]
f.append(f[-1] + 1)  

# resposta 20

print(a)

print(b)

print(c)

print(d)

print(e)

print(f)
