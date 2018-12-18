def calc_checksum(codes):
    twos = 0
    threes = 0
    for code in codes:
        has_two = False
        has_three = False
        for c in code:
            occ = code.count(c)
            if occ == 2:
                has_two = True
            elif occ == 3:
                has_three = True
            if has_two and has_three:
                break
        if has_two:
            twos += 1
        if has_three:
            threes += 1

    return twos * threes


def find_similar_brute(codes):
    searched = set()
    for code in codes:
        for s in searched:
            differences = 0
            for idx, c in enumerate(code):
                if c != s[idx]:
                    differences += 1
                if differences > 1:
                    break
            if differences <= 1:
                return code, s
        searched.add(code)
    return 0, 0


def solve_part2(codes):
    m1, m2 = find_similar_brute(codes)
    ans = ""
    for i in range(len(m1)):
        if m1[i] == m2[i]:
            ans += m1[i]
    return ans
