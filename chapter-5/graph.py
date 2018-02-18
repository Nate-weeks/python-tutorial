from graphics import *

def createGraph(fileName):
    testScores = open(fileName, "r")
    lineNumber = testScores.readline()
    graph = GraphWin("test scores", 400, 400)
    graph.setCoords(-15, 0, 100, int(lineNumber) * 3)
    #rectangle = Rectangle(Point(0, 0), Point(50, 1))
    #rectangle.draw(graph)
    yAxisCount = 1
    for line in testScores:
        splitLine = line.split()
        testScore = int(splitLine[1])
        name = splitLine[0]
        bar = Rectangle((Point(0, yAxisCount)), (Point(testScore, yAxisCount + 2)))
        bar.setFill("purple")
        bar.draw(graph)
        text = Text(Point(-7, yAxisCount + 1), name)
        text.draw(graph)
        yAxisCount += 3
    graph.getMouse()

createGraph("graph.txt")
