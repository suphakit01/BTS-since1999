from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2018, 1),
    date(2018, 2),
    date(2018, 3),
    date(2018, 4),
    date(2018, 5),
    date(2018, 6),
    date(2018, 7),
    date(2018, 8),
    date(2018, 9),
    date(2018, 10)

]
dateline.add("Total Ridership", [
    (date(2018, 1),20182918),
    (date(2018, 2),19137720),
    (date(2018, 3),20861139),
    (date(2018, 4),17874684),
    (date(2018, 5),19292454),
    (date(2018, 6),19979712),
    (date(2018, 7),19728982),
    (date(2018, 8),21548827),
    (date(2018, 9),19948031),
    (date(2018, 10),20094644)

])
dateline.render()