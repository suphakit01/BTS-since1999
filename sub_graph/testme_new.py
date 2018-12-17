import pygal
import pandas

def graph():

    #import src
    data = pandas.read_excel("D:/PSIT/WEB/sub_graph/srcdataridrship_new.xls")

    #append to list
    passenger = []
    date = []

    for i in data["Total Ridership1"]:
        if not str(i).isalpha():
            passenger.append(i)
    for j in data["Date"]:
        date.append(str(j))

    #print graph
    line_chart = pygal.Line()
    line_chart.title = 'Total Ridership of BTS (since 1999)'

    line_chart.x_labels = map(str, date)
    line_chart.add('Total Ridership', passenger)
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership.svg")
graph()
