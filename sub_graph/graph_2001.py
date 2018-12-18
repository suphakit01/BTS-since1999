""" Graph Total Ridership of BTS 2001 """

import pygal
def graph_2001():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2001 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [5466079,
        5096095,
        5971608,
        5257542,
        5613988,
        6300898,
        6441846,
        6794374,
        6207468,
        6460586,
        7051292,
        7363876])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2001.svg")

graph_2001()
