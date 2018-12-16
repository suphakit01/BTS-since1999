from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2014, 1),
    date(2014, 2),
    date(2014, 3),
    date(2014, 4),
    date(2014, 5),
    date(2014, 6),
    date(2014, 7),
    date(2014, 8),
    date(2014, 9),
    date(2014, 10),
    date(2014, 11),
    date(2014, 12)

]
dateline.add("Total Ridership", [
    (date(2014, 1),19862660),
    (date(2014, 2),18691403),
    (date(2014, 3),18530048),
    (date(2014, 4),16746945),
    (date(2014, 5),17249385),
    (date(2014, 6),17282436),
    (date(2014, 7),18136104),
    (date(2014, 8),18407367),
    (date(2014, 9),18099020),
    (date(2014, 10),18939493),
    (date(2014, 11),18714014),
    (date(2014, 12),18763492)
])
dateline.render()