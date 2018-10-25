import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Sequential', 'Parallel')
y_pos = np.arange(len(objects))
performance = [27.39385199546814, 21.417128324508667]

barlist = plt.bar(y_pos, performance, align='center', alpha=0.5)
barlist[0].set_color('r')
plt.xticks(y_pos, objects)
plt.ylabel('Time (s)')
plt.title('Computation Speed: Sequential vs Parallel')

plt.show()

y = np.array([27.39385199546814, 21.417128324508667])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel("Tme (s)")
ax.set_xlabel("processes")
ax.plot(objects, y)
plt.show()

labels = 'Sequential','Parallel'
sizes = [215, 130, 245, 210]
colors = ['red', 'blue']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(performance, explode = explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()