from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2015, 1),
    date(2015, 2),
    date(2015, 3),
    date(2015, 4),
    date(2015, 5),
    date(2015, 6),
    date(2015, 7),
    date(2015, 8),
    date(2015, 9),
    date(2015, 10),
    date(2015, 11),
    date(2015, 12)

]
dateline.add("Total Ridership", [
    (date(2015, 1),18632116),
    (date(2015, 2),17851582),
    (date(2015, 3),19904455),
    (date(2015, 4),17990474),
    (date(2015, 5),18462711),
    (date(2015, 6),19433834),
    (date(2015, 7),20186771),
    (date(2015, 8),19249095),
    (date(2015, 9),19066402),
    (date(2015, 10),19746844),
    (date(2015, 11),19831415),
    (date(2015, 12),19497894)
])
dateline.render()