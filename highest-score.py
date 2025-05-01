student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 96, 85, 83, 53]
total_exam_score = sum(student_scores)

print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score

print(sum)


print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score= score
print(max_score)

#counting all numbers from 1 to 100
total = 0
for number in range (1,101):
    total += number
print (total)