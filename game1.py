from graphics import *
Win_Width, Win_Height = 1000, 500

Window = GraphWin("Game", Win_Width, Win_Height)

level_nums = list(range(1, 11))

def Level_x(xlevel):
    if xlevel in level_nums:
        if xlevel == level_nums[0]:
            Window.setBackground("light blue")

            Draw_surface = Rectangle(Point(Win_Width - Win_Width, Win_Height), Point(Win_Width, Win_Height/(1 + (5 + 5/10)/10)))
            Draw_surface.setFill("light green")
            Draw_surface.draw(Window)

Level_x(1)


Window.getMouse()
Window.close()
