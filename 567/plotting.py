import matplotlib.pyplot as plt
x=["IOT","CD","ML","EE"]
y=[90,85,75,64]
#line plot 
plt.plot(x,y,color="r")
plt.title("MARKS OF THE STUDENT")
plt.xlabel("SUBJECT NAMES")
plt.ylabel("MARKS")
plt.show()

#Bar plot
plt.barh(x,y,color="r")
plt.title("MARKS OF THE STUDENT")
plt.xlabel("SUBJECT NAMES")
plt.ylabel("MARKS")
plt.show()

#pie plot
plt.pie(y)
plt.title("MARKS OF THE STUDENT")
plt.legend(x)
plt.show()



