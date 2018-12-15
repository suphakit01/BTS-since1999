from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2005, 1),
    date(2005, 2),
    date(2005, 3),
    date(2005, 4),
    date(2005, 5),
    date(2005, 6),
    date(2005, 7),
    date(2005, 8),
    date(2005, 9),
    date(2005, 10),
    date(2005, 11),
    date(2005, 12)

]
dateline.add("Total Ridership", [
    (date(2005, 1),10181516),
    (date(2005, 2),9223454),
    (date(2005, 3),10884480),
    (date(2005, 4),9036912),
    (date(2005, 5),9854319),
    (date(2005, 6),10914039),
    (date(2005, 7),10735889),
    (date(2005, 8),11292852),
    (date(2005, 9),10774389),
    (date(2005, 10),10697773),
    (date(2005, 11),11682804),
    (date(2005, 12),12071657)
])
dateline.render()