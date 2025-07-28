#Start code here
import pygal
years = ["2021", "2022", "2023", "2024"]
ph_levels = [5.5, 5.2, 5.0, 4]
line_chart = pygal.Line()
line_chart.title = "Average Rainwater pH over years:"
line_chart.add("pH Levels", ph_levels)
line_chart.x_labels = years
line_chart.render()
bar_chart = pygal.Line()
pie_chart = pygal.Pie()
pie_chart.title = "Rain Composition in 2024"
pie_chart.add("Neutral Water", [60])
pie_chart.add("Sulphuric Acid", [25])
pie_chart.add("Nitric acid", [15])
pie_chart.render()
