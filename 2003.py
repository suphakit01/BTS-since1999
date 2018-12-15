from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2003, 1),
    date(2003, 2),
    date(2003, 3),
    date(2003, 4),
    date(2003, 5),
    date(2003, 6),
    date(2003, 7),
    date(2003, 8),
    date(2003, 9),
    date(2003, 10),
    date(2003, 11),
    date(2003, 12)

]
dateline.add("Total Ridership", [
    (date(2003, 1),8507513),
    (date(2003, 2),7713509),
    (date(2003, 3),8538044),
    (date(2003, 4),7198802),
    (date(2003, 5),7613331),
    (date(2003, 6),8389649),
    (date(2003, 7),8816520),
    (date(2003, 8),9053085),
    (date(2003, 9),8935394),
    (date(2003, 10),8878402),
    (date(2003, 11),9246041),
    (date(2003, 12),9458407)
])
dateline.render()