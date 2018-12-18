""" Graph Total Ridership of BTS 2000 """

import pygal
def graph_2000():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2000 (หน่วย : เที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [4454948,
        3915835,
        4469294,
        4017524,
        4029665,
        4236755,
        4520399,
        5013489,
        4770950,
        4884270,
        5328457,
        5451085])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2000.svg")

graph_2000()
