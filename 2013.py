from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2013, 1),
    date(2013, 2),
    date(2013, 3),
    date(2013, 4),
    date(2013, 5),
    date(2013, 6),
    date(2013, 7),
    date(2013, 8),
    date(2013, 9),
    date(2013, 10),
    date(2013, 11),
    date(2013, 12)

]
dateline.add("Total Ridership", [
    (date(2013, 1),16963328),
    (date(2013, 2),15558348),
    (date(2013, 3),18585107),
    (date(2013, 4),16093002),
    (date(2013, 5),17008360),
    (date(2013, 6),17169349),
    (date(2013, 7),17658955),
    (date(2013, 8),18610028),
    (date(2013, 9),17256273),
    (date(2013, 10),18149207),
    (date(2013, 11),18423715),
    (date(2013, 12),17289299)
])
dateline.render()