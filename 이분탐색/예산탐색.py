def cal_budgets(budgets, cap):
    total = 0
    for budget in budgets:
        if budget < cap:
            total += budget
        if budget >= cap:
            total += cap
    return total


def solution(budgets, M):
    max_b = max(budgets)
    min_b = 1

    if sum(budgets) <= M:
        return max_b

    while True:
        median = (max_b + min_b) // 2
        estimated_budget = cal_budgets(budgets, median)
        estimated_budget_2 = cal_budgets(budgets, median + 1)

        if estimated_budget <= M and estimated_budget_2 >= M:
            break
        if estimated_budget > M:
            max_b = median
        if estimated_budget < M:
            min_b = median

    return median