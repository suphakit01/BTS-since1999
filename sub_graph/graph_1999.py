""" Graph Total Ridership of BTS 1999 """

import pygal
def graph_1999():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        4585743])
    line_chart.title = 'Total Ridership of BTS 1999 (หน่วย : ล้านเที่ยวคน)'
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership1999.svg")

graph_1999()
