# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

 
# y-axis in bold
rc('font', weight='bold')
 
# Values of each group
loss =          [3, 1, 3, 1, 3, 1]
biterror =      [3, 3, 3, 3, 2, 2]
nlamdabitrate = [3, 3, 1, 3, 3, 5]
wastageorunsup= [0, 2, 0, 0, 0, 0]
unsupportedlamda = [0,0,2,0,0,0] 
# Heights of bars1 + bars2
bars1 = np.array(loss)+np.array(biterror)
print(bars1)
bars2 = np.array(bars1)+np.array(wastageorunsup)
 
# The position of the bars on the x-axis
r = [0,1.5,4,5.5,8,9.5]
 
# Names of group and bar width
names = ['Worst\nLoss','Best\nLoss','Worst\nLoss','Best\nLoss','Worst\nLoss','Best\nLoss']
barWidth = 1
 
# Create brown bars
p1=plt.bar(r, loss, color='#F4493B', edgecolor='black', width=barWidth)
# Create green bars (middle), on top of the firs ones
p2=plt.bar(r, biterror, bottom=np.array(loss), color='#1C6ED6', edgecolor='black', width=barWidth)
# Create green bars (top)
p3=plt.bar(r, nlamdabitrate, bottom=bars1, color='#A6F43B', edgecolor='black', width=barWidth)
# 
p4=plt.bar(r, wastageorunsup, bottom=bars1+np.array(nlamdabitrate), color='black', edgecolor='black', width=barWidth,hatch="/")

p5=plt.bar(r, unsupportedlamda, bottom=bars1+np.array(nlamdabitrate)+np.array(wastageorunsup), color='#A6F43B', edgecolor='black', width=barWidth,hatch="|")

        
# Custom X axis
plt.xticks(r, names, fontweight='bold',fontname="Times New Roman",fontsize=12)
#plt.xlabel("Detector Sensistiviy",fontweight='bold',fontname="Times New Roman",fontsize=15)

plt.yticks(np.arange(9), ('','','','','','','','',''))
plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0]),('Required for Insertion Loss','Required for BitError Penalty','Required for Aggregate Datarate(N$_λ$*Bitrate)','Wastage Of Power','Unsupported Datarate'),loc='lower left', bbox_to_anchor= (-0.03, 1.05), ncol=2, frameon=False,handletextpad=0.2,prop={'weight':'bold'},labelspacing=0.0,columnspacing=0.2)
plt.ylabel("Required Laser Power",fontweight='bold',fontname="Times New Roman",fontsize=15)
plt.text(0.7, -1.9,'METHOD 1',
     horizontalalignment='center',
     verticalalignment='center',color='#B67201', fontsize=14)
plt.text(4.80, -1.9,'METHOD 2',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='#099200')
plt.text(8.80, -1.9,'PROTEUS',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='#027C92')
plt.text(8.00, 8.25,'Provisioned Power',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='red')
plt.text(8.30, 8.00,'---------------------',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='red')
plt.text(4.6, 7.25,'Provisioned Power',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='red')
plt.text(4.30, 7.00,'---------------------',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='red')

plt.text(.7, 9.25,'Provisioned Power',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='red')
plt.text(0.30, 9.00,'---------------------',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='red')
plt.text(11.6, 0.5,'Detector\nSensitivity',
     horizontalalignment='center',
     verticalalignment='center', fontsize=10,color='blue')
plt.text(5.9, 0.00,'-----------------------------------------------------------------------',
     horizontalalignment='center',
     verticalalignment='center', fontsize=14,color='blue')
  


# Show graphic
plt.show()
