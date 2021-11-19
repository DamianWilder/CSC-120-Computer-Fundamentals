BASE_SCORE = 60
EXTRA_CREDIT = 10


def main():
    test_scores = []
    for i in range(5):
        test_scores.append(float(input('Enter a test score: ')))
    print(test_scores)
    print(f'Students who scored below {BASE_SCORE} get {EXTRA_CREDIT} extra points')
    new_scores = [x + EXTRA_CREDIT if x < float(BASE_SCORE) else x for x in test_scores]
    print(new_scores)
    print('Students whose scores have changed:')
    for i in range(len(test_scores)):
        if test_scores[i] != new_scores[i]:
            print(f'Old score: {test_scores[i]} New score: {new_scores[i]}')


main()
