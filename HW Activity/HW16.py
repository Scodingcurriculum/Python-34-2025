#Start code here
import pygal
import math
name = pygal.Line()
name.title = "Marks Comparison"
labels = ["Test1", "Test2", "Test3", "Test4"]
name.x_labels = labels
John = [85, 78, 94]
Meera = [90, 75, 85]
Harry = [68, 63, 70]
Ginny = [90, 85, 88]
name.add("John", John)
name.add("Meera", Meera)
name.add("Harry", Harry)
name.add("Ginny", Ginny)
name.render()
