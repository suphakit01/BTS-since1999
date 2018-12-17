""" Graph Total Ridership of BTS 2005 """

import pygal
def graph_2005():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2005'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [10181516,
        9223454,
        10884480,
        9036912,
        9854319,
        10914039,
        10735889,
        11292852,
        10774389,
        10697773,
        11682804,
        12071657])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2005.svg")

graph_2005()
