from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2016, 1),
    date(2016, 2),
    date(2016, 3),
    date(2016, 4),
    date(2016, 5),
    date(2016, 6),
    date(2016, 7),
    date(2016, 8),
    date(2016, 9),
    date(2016, 10),
    date(2016, 11),
    date(2016, 12)

]
dateline.add("Total Ridership", [
    (date(2016, 1),19382612),
    (date(2016, 2),18948373),
    (date(2016, 3),20740242),
    (date(2016, 4),17809615),
    (date(2016, 5),18471103),
    (date(2016, 6),20190227),
    (date(2016, 7),20206492),
    (date(2016, 8),21240458),
    (date(2016, 9),20269768),
    (date(2016, 10),19889669),
    (date(2016, 11),20016026),
    (date(2016, 12),19882850)
])
dateline.render()