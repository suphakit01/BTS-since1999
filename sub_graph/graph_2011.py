""" Graph Total Ridership of BTS 2011 """

import pygal
def graph_2011():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2011'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [12834282,
        12057577,
        14446555,
        12288263,
        12933305,
        14209653,
        14291257,
        15657342,
        15163713,
        14243396,
        13484379,
        15738348
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2011.svg")

graph_2011()
