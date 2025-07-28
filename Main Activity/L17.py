#Start code here
import pygal
years = ["2021", "2022", "2023", "2024"]
elephants = [85, 70, 55, 42]
tigers = [44, 39, 32, 25]
parrots = [230, 200, 170, 140]
bar_chart = pygal.Bar()
bar_chart.title = "Wildlife Population Over Years (in thousands) "
bar_chart.x_labels = years
bar_chart.add("Elephants", elephants)
bar_chart.add("Tigers", tigers)
bar_chart.add("Parrots", parrots)
bar_chart.render()
#Additional ac # your own code
pie_chart1 = pygal.Pie()
pie_chart1.title = "Elephant count"
pie_chart1.add("2021", [85])
pie_chart1.add("2022", [70])
pie_chart1.add("2023", [55])
pie_chart1.add("2024", [1])
pie_chart1.render()
