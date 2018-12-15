from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2000, 1),
    date(2000, 2),
    date(2000, 3),
    date(2000, 4),
    date(2000, 5),
    date(2000, 6),
    date(2000, 7),
    date(2000, 8),
    date(2000, 9),
    date(2000, 10),
    date(2000, 11),
    date(2000, 12)

]
dateline.add("Total Ridership", [
    (date(2000, 1),4454948),
    (date(2000, 2),3915835),
    (date(2000, 3),4469294),
    (date(2000, 4),4017524),
    (date(2000, 5),4029665),
    (date(2000, 6),4236755),
    (date(2000, 7),4520399),
    (date(2000, 8),5013489),
    (date(2000, 9),4770950),
    (date(2000, 10),4884270),
    (date(2000, 11),5328457),
    (date(2000, 12),5451085)
])
dateline.render()