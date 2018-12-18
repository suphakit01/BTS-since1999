""" Graph Total Ridership of BTS 2016 """

import pygal
def graph_2016():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2016 (หน่วย : ล้านเที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [19382612,
        18948373,
        20740242,
        17809615,
        18471103,
        20190227,
        20206492,
        21240458,
        20269768,
        19889669,
        20016026,
        19882850
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2016.svg")

graph_2016()
