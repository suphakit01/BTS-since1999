from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2012, 1),
    date(2012, 2),
    date(2012, 3),
    date(2012, 4),
    date(2012, 5),
    date(2012, 6),
    date(2012, 7),
    date(2012, 8),
    date(2012, 9),
    date(2012, 10),
    date(2012, 11),
    date(2012, 12)

]
dateline.add("Total Ridership", [
    (date(2012, 1),15550730),
    (date(2012, 2),15675438),
    (date(2012, 3),16808551),
    (date(2012, 4),14830820),
    (date(2012, 5),15770635),
    (date(2012, 6),15793898),
    (date(2012, 7),16708952),
    (date(2012, 8),16582757),
    (date(2012, 9),16081386),
    (date(2012, 10),16780587),
    (date(2012, 11),16981454),
    (date(2012, 12),16547860)
])
dateline.render()