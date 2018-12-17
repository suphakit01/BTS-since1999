""" Graph Total Ridership of BTS 2012 """

import pygal
def graph_2012():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2012'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [15550730,
        15675438,
        16808551,
        14830820,
        15770635,
        15793898,
        16708952,
        16582757,
        16081386,
        16780587,
        16981454,
        16547860
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2012.svg")

graph_2012()
