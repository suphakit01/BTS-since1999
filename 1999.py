from datetime import date
dateline = pygal.DateLine(x_label_rotation=25)
dateline.x_labels = [
    date(1999, 1),
    

]
dateline.add("Total Ridership", [
    (date(1999, 1),4585743),
    
])
dateline.render()