""" Graph Total Ridership of BTS 2002 """

import pygal
def graph_2002():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line()
    line_chart.title = 'Total Ridership of BTS 2002'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [7367959,
        6675243,
        7718356,
        6770104,
        7349410,
        7799468,
        8198696,
        8581773,
        7912350,
        8064071,
        8574419,
        8574419])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2002.svg")

graph_2002()
