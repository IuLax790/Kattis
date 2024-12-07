def find_easiest_problem(problem_names, scores):
    total_points = [0] * len(problem_names)

    for team_scores in scores:
        for i, score in enumerate(team_scores):
            total_points[i] += score

    max_points = 0
    easiest_problem = ""
    for i, points in enumerate(total_points):
        if points > max_points:
            max_points = points
            easiest_problem = problem_names[i]

    return easiest_problem

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    problem_names = input().split()
    scores = []
    for _ in range(M):
        scores.append(list(map(int, input().split())))

    easiest_problem = find_easiest_problem(problem_names, scores)
    print(easiest_problem)
