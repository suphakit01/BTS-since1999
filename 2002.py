from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2002, 1),
    date(2002, 2),
    date(2002, 3),
    date(2002, 4),
    date(2002, 5),
    date(2002, 6),
    date(2002, 7),
    date(2002, 8),
    date(2002, 9),
    date(2002, 10),
    date(2002, 11),
    date(2002, 12)

]
dateline.add("Total Ridership", [
    (date(2002, 1),7367959),
    (date(2002, 2),6675243),
    (date(2002, 3),7718356),
    (date(2002, 4),6770104),
    (date(2002, 5),7349410),
    (date(2002, 6),7799468),
    (date(2002, 7),8198696),
    (date(2002, 8),8581773),
    (date(2002, 9),7912350),
    (date(2002, 10),8064071),
    (date(2002, 11),8574419),
    (date(2002, 12),8482132)
])
dateline.render()