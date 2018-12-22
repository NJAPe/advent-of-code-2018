from advent_of_code.utils.DoubleLinkedLIst import DoubleLinkedList


def perform_move(current, next_marble):
    points = 0
    if next_marble % 23 == 0:
        current = current.move_counter_clockwise(7)
        points = next_marble + current.get_value()
        current = current.remove_node()
    else:
        new_node = DoubleLinkedList(next_marble)
        current = current.move_clockwise()
        current.insert_node(new_node)
        current = new_node
    return current, points


def play_game(number_of_players, max_marble):
    current = DoubleLinkedList(0)
    scoreboard = dict()
    for i in range(1, max_marble+1):
        current, points = perform_move(current, i)
        player = ((i-1) % number_of_players) + 1
        if player in scoreboard:
            scoreboard[player] += points
        else:
            scoreboard[player] = points

    max_score = 0
    for score in scoreboard.values():
        if score > max_score:
            max_score = score
    return max_score
