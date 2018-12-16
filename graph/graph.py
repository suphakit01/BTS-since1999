import pygal
import pandas

def main():
    data = pandas.read_excel("20181214-ridershipData-201811.xls")
    # print(data["Total Ridership1 "])

    passenger = list()
    for i in data["Total Ridership1 "]:
        if not str(i).isalpha():
            passenger.append(i)

    # print(passenger)

    line_chart = pygal.HorizontalLine()
    line_chart.title = 'You know? Jack is so fat!'
    # line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Jack', passenger)
    # line_chart.range = [0, 100]
    line_chart.render_to_file("graph/jack_fat.svg")

main()
