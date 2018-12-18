""" Graph Total Ridership of BTS 2004 """

import pygal
def graph_2004():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2004 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [9157683,
        8876415,
        9471957,
        8324894,
        9253209,
        9904816,
        10387786,
        10111236,
        9829292,
        9736271,
        10454794,
        10173095])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2004.svg")

graph_2004()
