from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2017, 1),
    date(2017, 2),
    date(2017, 3),
    date(2017, 4),
    date(2017, 5),
    date(2017, 6),
    date(2017, 7),
    date(2017, 8),
    date(2017, 9),
    date(2017, 10),
    date(2017, 11),
    date(2017, 12)

]
dateline.add("Total Ridership", [
    (date(2017, 1),19685157),
    (date(2017, 2),18906338),
    (date(2017, 3),21469176),
    (date(2017, 4),18197128),
    (date(2017, 5),19303645),
    (date(2017, 6),20541021),
    (date(2017, 7),20178041),
    (date(2017, 8),21402153),
    (date(2017, 9),20600395),
    (date(2017, 10),19352649),
    (date(2017, 11),21078853),
    (date(2017, 12),20352638)
])
dateline.render()