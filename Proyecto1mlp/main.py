import matplotlib.pyplot as plt

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

################################################################ líneas

#plt.figure(figsize=(12,6))

#pais 1
x1 = [2016,2017,2018,2019,2020,2021]
y1 = [45, 46, 48, 51, 55, 62 ]

#pais 1
x2 = [2016,2017,2018,2019,2020,2021]
y2 = [40, 41, 42, 46, 54, 72 ]

'''plt.plot(x1,y1, marker = 'o', linestyle='--', color = 'r', label="País A",linewidth=2)
plt.plot(x2,y2, marker = 'o', linestyle='--', color = 'b', label="País B",linewidth=2)
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Evolution of Population')
plt.yticks([40, 45, 50, 55, 60, 65, 70, 75])
plt.legend(loc='lower right')
plt.grid(visible=True, which='major',linestyle="--", color='k',linewidth=0.5)
plt.show()'''

################################################################ barras

x= ['ESP', 'ARG', 'PER', 'COL']
y= [ 47, 40, 33, 30 ]
'''plt.bar(x,y)
plt.show()'''

################################################################ tarta

'''plt.pie(y, labels=x)
plt.show()'''

################################################################ histograma

edades = [15,16,18,20,23,24,25,28,31,33,34,36]
bins = [10, 20, 23, 29, 31]
'''plt.hist(edades,bins,edgecolor='black')
plt.show()'''

################################################################ scatterplots
'''plt.scatter(a,b)
plt.show()'''

################################################################ subplots

fig, ax = plt.subplots(2,1, sharey=True)
ax[0].plot(x1,y1,marker = 'o', linestyle='--', color = 'r', label="País A",linewidth=2)
ax[0].legend(loc='lower right')
ax[0].grid(visible=True)

ax[1].plot(x2,y2, marker = 'o', linestyle='--', color = 'b', label="País B",linewidth=2)
ax[1].legend(loc='lower right')
ax[1].grid(visible=True)


#plt.ylabel('Population')

#plt.yticks([40, 45, 50, 55, 60, 65, 70, 75])

plt.show()