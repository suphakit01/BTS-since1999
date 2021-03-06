import pygal
import pandas

def graph():

    #import src
    data = pandas.read_excel("D:/PSIT/WEB/graph/srcdataridrship.xls")

    #append to list
    passenger = []
    for i in data["Total Ridership1"]:
        if not str(i).isalpha():
            passenger.append(i)

    #print graph
    line_chart = pygal.Line()
    line_chart.title = 'Total Ridership of BTS (since 1999)'

    line_chart.x_labels = map(str, range(1999, 2018))
    line_chart.add('Total Ridership', passenger)
    line_chart.render_to_file("D:/PSIT/WEB/graph/total_ridership.svg")
graph()
