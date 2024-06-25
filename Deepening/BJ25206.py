grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

sum = 0
grade_sum = 0

for i in range(20):
    subject = list(map, str(input().split()))

    if subject[2] != "P":
        sum += float(subject[1])
        grade_sum += (float(subject[1])* grade[subject[2]])

print(round(grade_sum/sum, 6))