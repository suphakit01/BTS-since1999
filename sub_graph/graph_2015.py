""" Graph Total Ridership of BTS 2015 """

import pygal
def graph_2015():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2015 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [18632116,
        17851582,
        19904455,
        17990474,
        18462711,
        19433834,
        20186771,
        19249095,
        19066402,
        19746844,
        19831415,
        19497894
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2015.svg")

graph_2015()
