from graphics import *

'''
Program that draws a smileyface using zelle's graphics module.
'''
def main():
    #Make a Window 400 by 400
    win = GraphWin("Draw a Smiley", 400, 400)

    #Make and draw the outline of the face
    face = Circle(Point(200, 200), 150)
    face.draw(win)

    #Make, draw and fill the right and left eyes
    righteye = Circle(Point(150, 150), 20)
    righteye.setFill("red")
    righteye.draw(win)
    lefteye = righteye.clone()
    lefteye.move(100, 0)
    lefteye.draw(win)

    #Make and draw the eyebrows
    lefteyebrow = Line(Point(130, 110), Point(180, 130))
    lefteyebrow.draw(win)
    righteyebrow = Line(Point(230, 130), Point(280, 110))
    righteyebrow.draw(win)

    #Make and draw the mouth
    mouth = Oval(Point(120, 230), Point(270, 280))
    mouth.draw(win)

    #Make it so the window doesn't disappear
    text = Text(Point(80,350), "Click to close window")
    text.draw(win)
    win.getMouse()

main()
