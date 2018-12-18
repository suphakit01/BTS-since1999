""" Graph Total Ridership of BTS 2013 """

import pygal
def graph_2013():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2013 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [16963328,
        15558348,
        18585107,
        16093002,
        17008360,
        17169349,
        17658955,
        18610028,
        17256273,
        18149207,
        18423715,
        17289299
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2013.svg")

graph_2013()
