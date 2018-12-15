from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2004, 1),
    date(2004, 2),
    date(2004, 3),
    date(2004, 4),
    date(2004, 5),
    date(2004, 6),
    date(2004, 7),
    date(2004, 8),
    date(2004, 9),
    date(2004, 10),
    date(2004, 11),
    date(2004, 12)

]
dateline.add("Total Ridership", [
    (date(2004, 1),9157683),
    (date(2004, 2),8876415),
    (date(2004, 3),9471957),
    (date(2004, 4),8324894),
    (date(2004, 5),9253209),
    (date(2004, 6),9904816),
    (date(2004, 7),10387786),
    (date(2004, 8),10111236),
    (date(2004, 9),9829292),
    (date(2004, 10),9736271),
    (date(2004, 11),10454794),
    (date(2004, 12),10173095)
])
dateline.render()