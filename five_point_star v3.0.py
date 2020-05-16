"""
    作者：liutf
    日期：20200516
    功能：画五角星
    新增功能：画多个五角星
    新增功能：使用递归算法
    版本：3.0
"""

import turtle


def draw_5_star(size):
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    size += 20
    if size <= 100:
        draw_5_star(size)


def main():
    size = 20
    draw_5_star(size)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
