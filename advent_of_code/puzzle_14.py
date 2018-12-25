import math


def perform_recipe_iteration(recipes, worker_1, worker_2):
    combined = recipes[worker_1] + recipes[worker_2]
    if combined < 10:
        recipes.append(combined)
    else:
        recipes.append(math.floor(combined / 10))
        recipes.append(combined % 10)


def get_ten_after_x(x):
    recipes = [3, 7]
    worker_1 = 0
    worker_2 = 1
    while len(recipes) < x + 10:
        perform_recipe_iteration(recipes, worker_1, worker_2)
        worker_1 = (worker_1 + 1 + recipes[worker_1]) % len(recipes)
        worker_2 = (worker_2 + 1 + recipes[worker_2]) % len(recipes)
    last_10 = recipes[x: x+10]
    answer = ""
    for c in last_10:
        answer += str(c)
    return answer


def get_find_number_of_recipes_to_get_x(x):
    recipes = [3, 7, 1, 0]
    worker_1 = 0
    worker_2 = 1
    recipes_before_x = -1
    while recipes_before_x < 0:
        curr_len = len(recipes)
        perform_recipe_iteration(recipes, worker_1, worker_2)
        worker_1 = (worker_1 + 1 + recipes[worker_1]) % len(recipes)
        worker_2 = (worker_2 + 1 + recipes[worker_2]) % len(recipes)
        if len(recipes) < len(x):
            continue
        for i in range(max(0, curr_len-len(x)), len(recipes)-len(x)):
            answer = ""
            for j in range(len(x)):
                answer += str(recipes[i + j])
            if answer == x:
                recipes_before_x = i
                break
    return recipes_before_x
