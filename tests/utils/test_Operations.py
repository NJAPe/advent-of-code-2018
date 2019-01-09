from advent_of_code.utils.Operations import *
from nose.tools import assert_equal, raises

registers = [10, 11, 12, 13]


def test_addr():
    assert_equal(addr(0, 1, registers), 21)


@raises(IndexError)
def test_addr_invalid_index_A():
    addr(4, 2, registers)


@raises(IndexError)
def test_addr_negative_index_A():
    addr(-1, 2, registers)


@raises(IndexError)
def test_addr_invalid_index_B():
    addr(1, 4, registers)


@raises(IndexError)
def test_addr_negative_index_B():
    addr(1, -1, registers)


def test_addi():
    assert_equal(addi(3, 20, registers), 33)


@raises(IndexError)
def test_addi_invalid_index_A():
    addi(4, 3, registers)


@raises(IndexError)
def test_addi_negative_index_A():
    addi(-1, 2, registers)


def test_mulr():
    assert_equal(mulr(0, 1, registers), 110)


@raises(IndexError)
def test_mulr_invalid_index_A():
    mulr(4, 0, registers)


@raises(IndexError)
def test_mulr_negative_index_A():
    mulr(-1, 2, registers)


@raises(IndexError)
def test_mulr_invalid_index_B():
    mulr(0, 4, registers)


@raises(IndexError)
def test_mulr_negative_index_B():
    mulr(2, -1, registers)


def test_muli():
    assert_equal(muli(1, 4, registers), 44)


@raises(IndexError)
def test_muli_invalid_index_A():
    muli(4, 1, registers)


@raises(IndexError)
def test_muli_negative_index_A():
    muli(-1, 1, registers)


def test_banr():
    assert_equal(banr(0, 1, registers), 10)


@raises(IndexError)
def test_banr_invalid_index_A():
    banr(4, 1, registers)


@raises(IndexError)
def test_banr_negative_index_A():
    banr(-1, 1, registers)


@raises(IndexError)
def test_banr_invalid_index_B():
    banr(1, 4, registers)


@raises(IndexError)
def test_banr_negative_index_B():
    banr(1, -1, registers)


def test_bani():
    assert_equal(bani(0, 2, registers), 2)


@raises(IndexError)
def test_bani_invalid_index_A():
    bani(4, 0, registers)


@raises(IndexError)
def test_bani_negative_index_A():
    bani(-1, 1, registers)


def test_borr():
    assert_equal(borr(0, 1, registers), 11)


@raises(IndexError)
def test_borr_invalid_index_A():
    borr(4, 1, registers)


@raises(IndexError)
def test_borr_negative_index_B():
    borr(-1, 1, registers)


@raises(IndexError)
def test_borr_invalid_index_B():
    borr(0, 4, registers)


@raises(IndexError)
def test_borr_negative_index_B():
    borr(0, -1, registers)


def test_bori():
    assert_equal(bori(0, 1, registers), 11)


@raises(IndexError)
def test_bori_invalid_index_A():
    bori(4, 1, registers)


@raises((IndexError))
def test_bori_negative_index_A():
    bori(-1, 1, registers)


def test_setr():
    assert_equal(setr(0, 1, registers), 10)
    assert_equal(setr(0, 4, registers), 10)


@raises(IndexError)
def test_setr_invalid_index_A():
    setr(4, 1, registers)


@raises(IndexError)
def test_setr_negative_index_A():
    setr(-1, 1, registers)


def test_seti():
    assert_equal(seti(0, 1, registers), 0)
    assert_equal(seti(0, 4, registers), 0)


def test_gtir():
    assert_equal(gtir(100, 0, registers), 1)
    assert_equal(gtir(10, 0 , registers), 0)


@raises(IndexError)
def test_gtir_invalid_index_B():
    gtir(0, 4, registers)


@raises(IndexError)
def test_gtir_negative_index_B():
    gtir(0, -1, registers)


def test_gtri():
    assert_equal(gtri(0, 9, registers), 1)
    assert_equal(gtri(0, 10, registers), 0)


@raises(IndexError)
def test_gtri_invalid_index_A():
    gtri(4, 0, registers)


@raises(IndexError)
def test_gtri_negative_index_A():
    gtri(-1, 0, registers)


def test_gtrr():
    assert_equal(gtrr(0, 1, registers), 0)
    assert_equal(gtrr(1, 0, registers), 1)
    assert_equal(gtrr(3, 3, registers), 0)


@raises(IndexError)
def test_gtrr_invalid_index_A():
    gtrr(0, 4, registers)


@raises(IndexError)
def test_gtrr_negative_index_A():
    gtrr(-1, 0, registers)


@raises(IndexError)
def test_gtrr_invalid_index_B():
    gtrr(0, 4, registers)


@raises(IndexError)
def test_gtrr_negative_index_B():
    gtrr(0, -1, registers)


def test_eqir():
    assert_equal(eqir(10, 0, registers), 1)
    assert_equal(eqir(11, 0, registers), 0)


@raises(IndexError)
def test_eqir_invalid_index_B():
    eqir(0, 4, registers)


@raises(IndexError)
def test_eqir_negative_index_B():
    eqir(0, -1, registers)


def test_eqri():
    assert_equal(eqri(0, 10, registers), 1)
    assert_equal(eqri(0, 11, registers), 0)


@raises(IndexError)
def test_eqri_invalid_index_A():
    eqri(4, 0, registers)


@raises(IndexError)
def test_eqri_negative_index_A():
    eqri(-1, 0, registers)


def test_eqrr():
    assert_equal(eqrr(0, 0, registers), 1)
    assert_equal(eqrr(0, 1, registers), 0)


@raises(IndexError)
def test_eqrr_invalid_index_A():
    eqrr(4, 0, registers)


@raises(IndexError)
def test_eqrr_negative_index_A():
    eqrr(-1, 0, registers)


@raises(IndexError)
def test_eqrr_invalid_index_B():
    eqrr(0, 4, registers)


@raises(IndexError)
def test_eqrr_negative_index_B():
    eqrr(0, -1, registers)
