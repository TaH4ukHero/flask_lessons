def is_under_queen_attack(position, queen_position):
    transmutations = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8
    }

    for i in [position, queen_position]:
        if type(i) != str:
            raise TypeError
        if not (i[0] in transmutations.keys() and i[0].islower() and i[0].isalpha() and i[-1].isdigit() and (
                0 < int(i[-1]) <= 8) and (len(i) == 2)):
            raise ValueError

    x1, y1, x2, y2 = transmutations[position[0]], int(position[-1]), transmutations[queen_position[0]], int(
        queen_position[-1])
    if ((abs(x1 - x2) == abs(y1 - y2)) or (x1 == x2 or y1 == y2)) and (x1 != x2 or y1 != y2):
        return True
    return False
