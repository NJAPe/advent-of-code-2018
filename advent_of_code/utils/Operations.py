def addr(A, B, registers):
    if A < 0 or B < 0:
        raise IndexError
    return registers[A] + registers[B]


def addi(A, B, registers):
    if A < 0:
        raise IndexError
    return registers[A] + B


def mulr(A, B, registers):
    if A < 0 or B < 0:
        raise IndexError
    return registers[A] * registers[B]


def muli(A, B, registers):
    if A < 0:
        raise IndexError
    return registers[A] * B


def banr(A, B, registers):
    if A < 0 or B < 0:
        raise IndexError
    return registers[A] & registers[B]


def bani(A, B, registers):
    if A < 0:
        raise IndexError
    return registers[A] & B


def borr(A, B, registers):
    if A < 0 or B < 0:
        raise IndexError
    return registers[A] | registers[B]


def bori(A, B, registers):
    if A < 0:
        raise IndexError
    return registers[A] | B


def setr(A, B, registers):
    if A < 0:
        raise IndexError
    return registers[A]


def seti(A, B, registers):
    return A


def gtir(A, B, registers):
    if B < 0:
        raise IndexError
    if A > registers[B]:
        return 1
    else:
        return 0


def gtri(A, B, registers):
    if A < 0:
        raise IndexError
    if registers[A] > B:
        return 1
    else:
        return 0


def gtrr(A, B, registers):
    if A < 0 or B < 0:
        raise IndexError
    if registers[A] > registers[B]:
        return 1
    else:
        return 0


def eqir(A, B, registers):
    if B < 0:
        raise IndexError
    if A == registers[B]:
        return 1
    else:
        return 0


def eqri(A, B, registers):
    if A < 0:
        raise IndexError
    if registers[A] == B:
        return 1
    else:
        return 0


def eqrr(A, B, registers):
    if A < 0 or B < 0:
        raise IndexError
    if registers[A] == registers[B]:
        return 1
    else:
        return 0
