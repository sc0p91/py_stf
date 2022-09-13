dots = []
for i in range(500):
    dots.append(".")

for i in range(len(dots)):
    if (i+1) % 20 == 0:
        print(dots[i-19:i+1])
    
