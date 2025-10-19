#Afruzunova Dasha 502744
red='\u001b[41m'
white='\u001b[47m'
end='\u001b[0m'
w=40
h=8
for i in range(h//2):
    print(white + " " * w + end)
for i in range(h//2):
    print(red + " " * w + end)
