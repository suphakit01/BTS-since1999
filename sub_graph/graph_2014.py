""" Graph Total Ridership of BTS 2014 """

import pygal
def graph_2014():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2014 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [19862660,
        18691403,
        18530048,
        16746945,
        17249385,
        17282436,
        18136104,
        18407367,
        18099020,
        18939493,
        18714014,
        18763492
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2014.svg")

graph_2014()
