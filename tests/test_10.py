import advent_of_code.puzzle_10 as p10
from nose.tools import assert_equal
import os

sample_input = ["position=< 9,  1> velocity=< 0,  2>",
                "position=< 7,  0> velocity=<-1,  0>",
                "position=< 3, -2> velocity=<-1,  1>",
                "position=< 6, 10> velocity=<-2, -1>",
                "position=< 2, -4> velocity=< 2,  2>",
                "position=<-6, 10> velocity=< 2, -2>",
                "position=< 1,  8> velocity=< 1, -1>",
                "position=< 1,  7> velocity=< 1,  0>",
                "position=<-3, 11> velocity=< 1, -2>",
                "position=< 7,  6> velocity=<-1, -1>",
                "position=<-2,  3> velocity=< 1,  0>",
                "position=<-4,  3> velocity=< 2,  0>",
                "position=<10, -3> velocity=<-1,  1>",
                "position=< 5, 11> velocity=< 1, -2>",
                "position=< 4,  7> velocity=< 0, -1>",
                "position=< 8, -2> velocity=< 0,  1>",
                "position=<15,  0> velocity=<-2,  0>",
                "position=< 1,  6> velocity=< 1,  0>",
                "position=< 8,  9> velocity=< 0, -1>",
                "position=< 3,  3> velocity=<-1,  1>",
                "position=< 0,  5> velocity=< 0, -1>",
                "position=<-2,  2> velocity=< 2,  0>",
                "position=< 5, -2> velocity=< 1,  2>",
                "position=< 1,  4> velocity=< 2,  1>",
                "position=<-2,  7> velocity=< 2, -2>",
                "position=< 3,  6> velocity=<-1, -1>",
                "position=< 5,  0> velocity=< 1,  0>",
                "position=<-6,  0> velocity=< 2,  0>",
                "position=< 5,  9> velocity=< 1, -2>",
                "position=<14,  7> velocity=<-2,  0>",
                "position=<-3,  6> velocity=< 2, -1>"]
sample_answer = """#...#..###
#...#...#.
#...#...#.
#####...#.
#...#...#.
#...#...#.
#...#...#.
#...#..###
"""
real_answer = """.####...#####......###..#.......#.......#.......#.......#....#
#....#..#....#......#...#.......#.......#.......#.......#....#
#.......#....#......#...#.......#.......#.......#.......#....#
#.......#....#......#...#.......#.......#.......#.......#....#
#.......#####.......#...#.......#.......#.......#.......######
#..###..#...........#...#.......#.......#.......#.......#....#
#....#..#...........#...#.......#.......#.......#.......#....#
#....#..#.......#...#...#.......#.......#.......#.......#....#
#...##..#.......#...#...#.......#.......#.......#.......#....#
.###.#..#........###....######..######..######..######..#....#
"""
input_file_path = os.path.join(os.path.dirname(__file__), "..", "inputs", "10_input.txt")


def test_sample_input():
    my_points = p10.parse_input(sample_input)
    assert_equal(len(my_points), 31, f"expexted there to be 31 points, but there was {len(my_points)}")
    seconds, img_str = p10.step_and_print_image(my_points)
    assert_equal(seconds, 3, f"expected 3 seconds to have appeared, not {seconds}")
    assert_equal(img_str, sample_answer)


def test_real_input():
    with open(input_file_path) as f:
        real_input = f.read().strip().split("\n")
    my_points = p10.parse_input(real_input)
    assert_equal(len(my_points), 290, f"expexted there to be 290 points, but there was {len(my_points)}")
    seconds, img_str = p10.step_and_print_image(my_points)
    assert_equal(seconds, 10515, f"expected 10515 seconds to have appeared, not {seconds}")
    assert_equal(img_str, real_answer)
