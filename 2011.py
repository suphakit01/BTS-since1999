from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(2011, 1),
    date(2011, 2),
    date(2011, 3),
    date(2011, 4),
    date(2011, 5),
    date(2011, 6),
    date(2011, 7),
    date(2011, 8),
    date(2011, 9),
    date(2011, 10),
    date(2011, 11),
    date(2011, 12)

]
dateline.add("Total Ridership", [
    (date(2011, 1),12834282),
    (date(2011, 2),12057577),
    (date(2011, 3),14446555),
    (date(2011, 4),12288263),
    (date(2011, 5),12933305),
    (date(2011, 6),14209653),
    (date(2011, 7),14291257),
    (date(2011, 8),15657342),
    (date(2011, 9),15163713),
    (date(2011, 10),14243396),
    (date(2011, 11),13484379),
    (date(2011, 12),15738348)
])
dateline.render()