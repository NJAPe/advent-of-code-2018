from advent_of_code.utils.Cart import Cart
from nose.tools import assert_equal


def test_intersect_rotate_left():
    cart = Cart(0, 0, "<")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "v", "expected cart to have turned left")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "v", "expected cart not to have turned")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "<", "expected cart to have turned right")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "v", "expected cart to have turned left")


def test_intersect_rotate_right():
    cart = Cart(0, 0, ">")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "^", "expected cart to have turned left")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "^", "expected cart not to have turned")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), ">", "expected cart to have turned right")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "^", "expected cart to have turned left")


def test_intersect_rotate_upp():
    cart = Cart(0, 0, "^")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "<", "expected cart to have turned left")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "<", "expected cart not to have turned")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "^", "expected cart to have turned right")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "<", "expected cart to have turned left")


def test_intersect_rotate_down():
    cart = Cart(0, 0, "v")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), ">", "expected cart to have turned left")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), ">", "expected cart not to have turned")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), "v", "expected cart to have turned right")
    cart.intersect_rotate()
    assert_equal(cart.get_direction(), ">", "expected cart to have turned left")


def test_move_forward_left():
    cart = Cart(3, 3, "<")
    cart.move_forward()
    assert_equal(cart.get_coordinates(), (2, 3), "Expected cart to have moved")


def test_move_forward_right():
    cart = Cart(3, 3, ">")
    cart.move_forward()
    assert_equal(cart.get_coordinates(), (4, 3), "Expected cart to have moved")


def test_move_forward_down():
    cart = Cart(3, 3, "v")
    cart.move_forward()
    assert_equal(cart.get_coordinates(), (3, 4), "Expected cart to have moved")


def test_move_forward_upp():
    cart = Cart(3, 3, "^")
    cart.move_forward()
    assert_equal(cart.get_coordinates(), (3, 2), "Expected cart to have moved")


def test_turn_rotate_down_forward():
    cart = Cart(0, 0, "v")
    cart.turn_rotate("/")
    assert_equal(cart.get_direction(), "<")


def test_turn_rotate_down_backward():
    cart = Cart(0, 0, "v")
    cart.turn_rotate("\\")
    assert_equal(cart.get_direction(), ">")


def test_turn_rotate_upp_forward():
    cart = Cart(0, 0, "^")
    cart.turn_rotate("/")
    assert_equal(cart.get_direction(), ">")


def test_turn_rotate_upp_backward():
    cart = Cart(0, 0, "^")
    cart.turn_rotate("\\")
    assert_equal(cart.get_direction(), "<")


def test_turn_rotate_left_forward():
    cart = Cart(0, 0, "<")
    cart.turn_rotate("/")
    assert_equal(cart.get_direction(), "v")


def test_turn_rotate_left_backward():
    cart = Cart(0, 0, "<")
    cart.turn_rotate("\\")
    assert_equal(cart.get_direction(), "^")


def test_turn_rotate_right_forward():
    cart = Cart(0, 0, ">")
    cart.turn_rotate("/")
    assert_equal(cart.get_direction(), "^")


def test_turn_rotate_right_backward():
    cart = Cart(0, 0, ">")
    cart.turn_rotate("\\")
    assert_equal(cart.get_direction(), "v")
