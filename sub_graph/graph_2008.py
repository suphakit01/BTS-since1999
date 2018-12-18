""" Graph Total Ridership of BTS 2008 """

import pygal
def graph_2008():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2008 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [11267371,
        10846156,
        12032367,
        10366739,
        10930375,
        11647620,
        11679567,
        11838300,
        11071320,
        11976189,
        11647462,
        11046541])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2008.svg")

graph_2008()
