import time



Name = ['AbuTalha', 'Khalil', 'Osman', 'konen']

calculus = [75, 86, 78, 90]
English = [91, 88, 87, 90]
Programming = [87, 90, 95, 89]


total = []

for i in range(3):
    print(Name[i])
    sum = calculus[i] + English[i] + Programming[i]
    total.append(sum)
    print(sum)
