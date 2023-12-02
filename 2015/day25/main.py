import re
r, c = map(int, re.findall(r'(\d+)',open(0).read().strip()))

n = r + c - 1 #n er hvilken diagonal vi er i
k = (n * (n-1)) // 2 + c #k er tallet på plassen 
print(20151125 * pow(252533, k-1, 33554393) % 33554393)