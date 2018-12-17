""" Graph Total Ridership of BTS 2007 """

import pygal
def graph_2007():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2007'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [11175939,
        10659843,
        11496036,
        9622967,
        10660186,
        11138186,
        11184445,
        11391791,
        10854799,
        11325870,
        11663120,
        10897320])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2007.svg")

graph_2007()
