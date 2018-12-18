def xor(a, b):
    return (a or b) and not (a and b)


def collapse_polymer(polymer):
    pos = 0
    while pos + 1 < len(polymer):
        first = polymer[pos]
        second = polymer[pos + 1]
        if first.lower() == second.lower() and xor(first.isupper(), second.isupper()):
            if pos + 2 >= len(polymer):
                polymer = polymer[0:pos]
            else:
                polymer = polymer[0:pos] + polymer[pos + 2:]
            pos = max(0, pos - 1)
        else :
            pos += 1
    return polymer


def find_shortest_poly_by_removing_one_type(polymer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ans = polymer
    for letter in alphabet:
        tst = polymer.replace(letter.lower(), '')
        tst = tst.replace(letter.upper(), '')
        tmp = collapse_polymer(tst)
        if len(tmp) < len(ans):
            ans = tmp
    return ans
