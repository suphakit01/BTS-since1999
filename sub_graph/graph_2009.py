""" Graph Total Ridership of BTS 2009 """

import pygal
def graph_2009():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line()
    line_chart.title = 'Total Ridership of BTS 2009'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [10990138,
        10372901,
        12372648,
        10500829,
        11110654,
        12269615,
        11502001,
        12118293,
        11827626,
        12559220,
        12699887,
        12634157])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2009.svg")

graph_2009()