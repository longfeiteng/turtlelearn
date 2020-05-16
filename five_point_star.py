"""
    作者：liutf
    日期：20200516
    功能：画五角星
    版本：1.0
"""

import turtle


def main():
    count = 1
    while count <= 5:
        turtle.forward(20)
        turtle.right(144)
        count += 1

    turtle.exitonclick()


if __name__ == "__main__":
    main()
