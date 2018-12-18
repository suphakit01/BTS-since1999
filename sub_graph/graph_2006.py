""" Graph Total Ridership of BTS 2006 """

import pygal
def graph_2006():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line(legend_at_bottom=True)
    line_chart.title = 'Total Ridership of BTS 2006 (หน่วย : เที่ยวคน)'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [11532519,
        10665446,
        12628541,
        10133987,
        11300664,
        12067062,
        12312414,
        12617203,
        11410102,
        11752087,
        12004291,
        11624533])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership2006.svg")

graph_2006()
