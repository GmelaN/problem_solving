def solution(answers):
    patterns = ((1,2,3,4,5), (2,1,2,3,2,4,2,5), (3,3,1,1,2,2,4,4,5,5))
    correct_count = [0, 0, 0]
    n_problem = 0

    for answer in answers:
        for n in range(len(patterns)):
            if patterns[n][n_problem % len(patterns[n])] == answer:
                correct_count[n] += 1

        n_problem += 1

    res = []
    max_correct_count = max(correct_count)

    for i in range(len(correct_count)):
        if correct_count[i] == max_correct_count:
            res.append(i + 1)
    
    return res
