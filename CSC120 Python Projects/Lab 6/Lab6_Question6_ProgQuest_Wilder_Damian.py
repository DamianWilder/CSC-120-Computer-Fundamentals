# Given the string
# SCORES = [40,91,85,15]
# Write a program to find all the pairs of scores in the above list. The output should be
# 40,91
# 40,85
# 40,15
# 91.85
# 91,15
# 85,15

SCORES = [40, 91, 85, 15]
already_matched = []
for score in SCORES:
    for match in SCORES:
        if [score, match] not in already_matched and [match, score] not in already_matched and score != match:
            already_matched.append([score, match])

for match in already_matched:
    print(match)
