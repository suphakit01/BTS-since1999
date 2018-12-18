""" Graph Total Ridership of BTS 2003 """

import pygal
def graph_2003():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2003 (หน่วย : เที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [8507513,
        7713509,
        8538044,
        7198802,
        7613331,
        8389649,
        8816520,
        9053085,
        8935394,
        8878402,
        9246041,
        9458407])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2003.svg")

graph_2003()
