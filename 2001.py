from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2001, 1),
    date(2001, 2),
    date(2001, 3),
    date(2001, 4),
    date(2001, 5),
    date(2001, 6),
    date(2001, 7),
    date(2001, 8),
    date(2001, 9),
    date(2001, 10),
    date(2001, 11),
    date(2001, 12)

]
dateline.add("Total Ridership", [
    (date(2001, 1),5466079),
    (date(2001, 2),5096095),
    (date(2001, 3),5971608),
    (date(2001, 4),5257542),
    (date(2001, 5),5613988),
    (date(2001, 6),6300898),
    (date(2001, 7),6441846),
    (date(2001, 8),6794374),
    (date(2001, 9),6207468),
    (date(2001, 10),6460586),
    (date(2001, 11),7051292),
    (date(2001, 12),7363876)
])
dateline.render()