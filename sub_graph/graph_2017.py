""" Graph Total Ridership of BTS 2017 """

import pygal
def graph_2017():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line()
    line_chart.title = 'Total Ridership of BTS 2017'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [19685157,
        18906338,
        21469176,
        18197128,
        19303645,
        20541021,
        20178041,
        21402153,
        20600395,
        19352649,
        21078853,
        20352638
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2017.svg")

graph_2017()
