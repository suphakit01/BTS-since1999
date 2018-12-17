""" Graph Total Ridership of BTS 2010 """

import pygal
def graph_2010():
    """ plot graph with pygal """
    date = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y_label = [0, 5000000, 10000000, 15000000, 20000000]

    line_chart = pygal.Line()
    line_chart.title = 'Total Ridership of BTS 2010'

    line_chart.x_labels = map(str, date)
    line_chart.y_labels = map(int, y_label)
    line_chart.add('Total Ridership', [12355949,
        12355949,
        11862466,
        13033511,
        9500859,
        6651929,
        12246670,
        12471248,
        12665313,
        12645925,
        13173405,
        13306413,
        13189283
        ])
    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/total_ridership1999.svg")

graph_2010()
