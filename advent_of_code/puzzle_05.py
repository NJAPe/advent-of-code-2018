def xor(a, b):
    return (a or b) and not (a and b)


def collapse_poymer(polymer):
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


# in_val = "aAbBcCddD"
# in_val = "dabAcCaCBAcCcaDA"
# in_val = "aabAAB"
with open("05_input.txt") as f:
    in_val = f.read().strip()
ans = len(collapse_poymer(in_val))
print(f"Answer1: {ans}")

alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    tst = in_val.replace(letter.lower(), '')
    tst = tst.replace(letter.upper(), '')
    tmp = len(collapse_poymer(tst))
    if tmp < ans:
        ans = tmp
print(f"Asnwer2: {ans}")
