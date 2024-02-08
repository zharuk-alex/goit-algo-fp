import turtle


def draw_branch(t, size=70, level=6):
    angle = 45
    sub_size = 0.75 * size

    if level > 0:
        level -= 1
        t.forward(size)
        t.right(angle)
        draw_branch(t, sub_size, level)
        t.left(2 * angle)
        draw_branch(t, sub_size, level)
        t.right(angle)
        t.forward(-size)


def init_tree(size, level):
    t = turtle.Turtle()
    window = turtle.Screen()
    margin_bottom = 50
    turtle.setup(800, 600)

    height = window.window_height()
    t.pencolor("red")
    t.penup()
    t.goto(0, -height / 2 + margin_bottom)
    t.pendown()
    t.right(-90)
    t.speed("fastest")
    draw_branch(t, size=size, level=level)

    window.mainloop()


if __name__ == "__main__":
    is_active = True
    while is_active:
        try:
            level = int(input("Enter the level of recursion: "))
            if level <= 0:
                raise ValueError("Value must be greater than 0")
            init_tree(size=90, level=level)
            is_active = False
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            print("\nHave a nice day")
            is_active = False
