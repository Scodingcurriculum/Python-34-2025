#Start code here
import math
import pygal
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
steps = [4500, 6700, 8000, 4000, 9000, 12000, 7000]
name = pygal.Line()
name.title = "My awesome chart"
name.add("Steps", steps)
name.x_labels = days
name.render()
print("Weekly Steps Summary----------------------")
total_steps = sum(steps)
average_steps = math.floor(total_steps / 7)
min_steps = min(steps)
max_steps = max(steps)
most_active_day = days[steps.index(max_steps)]
least_active_day = days[steps.index(min_steps)]
print("Total Steps = " + str(total_steps))
print("Average steps / day = " + str(average_steps))
print("Most Active day = " + most_active_day)
print("Least Active day = " + least_active_day)
