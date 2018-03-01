from graphics import *

# function that takes a text file of test scores and draws a graph
def createGraph(fileName):
    testScores = open(fileName, "r")                    # list of scores
    lineNumber = testScores.readline()
    graph = GraphWin("test scores", 400, 400)
    graph.setCoords(-15, 0, 100, int(lineNumber) * 3)
    #rectangle = Rectangle(Point(0, 0), Point(50, 1))
    #rectangle.draw(graph)


    #loop through the scores in the file to draw a graph

    yAxisCount = 1                      #start the y-axis at coordinate point 1
    for line in testScores:
        splitLine = line.split()            # split the lines to isolate name and score
        testScore = int(splitLine[1])
        name = splitLine[0]
        #initiate graph bars
        bar = Rectangle((Point(0, yAxisCount)), (Point(testScore, yAxisCount + 2)))
        bar.setFill("purple")
        bar.draw(graph)
        #initiate text
        text = Text(Point(-7, yAxisCount + 1), name)
        text.draw(graph)
        yAxisCount += 3
    graph.getMouse()

createGraph("graph.txt")
