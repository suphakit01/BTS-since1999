""" Graph Total Ridership of BTS 2018 """

import pygal
def graph_2018():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2018'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [20182918,
        19137720,
        20861139,
        17874684,
        19292454,
        19979712,
        19728982,
        21548827,
        19948031,
        20094644,
        21154634,
        None])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2018.svg")

graph_2018()
