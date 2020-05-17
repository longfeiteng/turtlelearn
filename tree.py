"""
    作者：liutf
    日期：20200517
    功能：画树
    版本：1.0
"""

import turtle


def draw_tree(current_lenth):
    if current_lenth > 15:
        turtle.forward(current_lenth)
        turtle.right(20)
        draw_tree(current_lenth-15)

        turtle.left(40)
        draw_tree(current_lenth-15)

        turtle.right(20)
        turtle.back(current_lenth)


def main():
    turtle.left(90)
    turtle.penup()
    turtle.back(200)
    turtle.pendown()
    turtle.pencolor('brown')

    draw_tree(100)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
