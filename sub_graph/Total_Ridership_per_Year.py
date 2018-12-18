""" Total Ridership per Year """
import pygal
def graph():
    """ creat graph Total Ridership per Year """

    line_chart = pygal.Bar(legend_at_bottom=True)
    line_chart.title = 'Total Ridership per Year (หน่วย : ล้านเที่ยวคน)'
    line_chart.add('1999', 4585743)
    line_chart.add('2000', 55092671)
    line_chart.add('2001', 74025652)
    line_chart.add('2002', 93493981)
    line_chart.add('2003', 102348697)
    line_chart.add('2004', 115681448)
    line_chart.add('2005', 127350084)
    line_chart.add('2006', 140048849)
    line_chart.add('2007', 132070502)
    line_chart.add('2008', 136350007)
    line_chart.add('2009', 140957969)
    line_chart.add('2010', 143102971)
    line_chart.add('2011', 167348070)
    line_chart.add('2012', 194113068)
    line_chart.add('2013', 208764971)
    line_chart.add('2014', 219422367)
    line_chart.add('2015', 229853593)
    line_chart.add('2016', 237047435)
    line_chart.add('2017', 241067194)
    line_chart.add('2018', 219803745)


    line_chart.render_to_file("D:/PSIT/WEB/sub_graph/Total_Ridership_per_Year.svg")
graph()
