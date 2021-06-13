import matplotlib.pyplot as plt
import pandas as pd

# ----  ---- Graph 1 ---- ----
# reference: https://ourworldindata.org/causes-of-death
# The share of deaths from injuries, infectious diseases, and non-communicable diseases

# Creating labels and percentage for deaths by cause in 1990.
l_1990 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_1990 = [9, 58, 33]

# Creating labels and percentage for deaths by cause in 2000.
l_2000 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_2000 = [9, 62, 29]

# Creating labels and percentage for deaths by cause in 2010.
l_2010 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_2010 = [9, 67, 24]

# Creating labels and percentage for deaths by cause in 2017.
l_2017 = ['Injuries', 'Non-communicable\ndiseases', 'Communicable\ndiseases']
p_2017 = [8, 73, 19]

# Creating a figure with dimension of 2 rows and 2 columns for subplotting.
fig, axs = plt.subplots(2, 2, figsize = (11, 9))

# Creating a bar chart with the label and percentage of 1990 and storing it in variable 'bars_1990'.
bars_1990 = axs[0, 0].bar(l_1990, p_1990, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[0, 0].set_title('Deaths by cause in the world in 1990', fontdict = {'fontweight': 'bold', 'fontsize':13}) # Setting a title for the bar chart.
axs[0, 0].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13}) # Setting xlabel
axs[0, 0].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_1990[0].set_hatch('.') # Setting the hatch for the first bar in the bar chart.

bars_2000 = axs[0, 1].bar(l_2000, p_2000, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[0, 1].set_title('Deaths by cause in the world in 2000', fontdict = {'fontweight': 'bold', 'fontsize':13})
axs[0, 1].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
axs[0, 1].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_2000[0].set_hatch('.')

bars_2010 = axs[1, 0].bar(l_2010, p_2010, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[1, 0].set_title('Deaths by cause in the world in 2010', fontdict = {'fontweight': 'bold', 'fontsize':13})
axs[1, 0].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
axs[1, 0].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_2010[0].set_hatch('.')

bars_2017 = axs[1, 1].bar(l_2017, p_2017, width = 0.4, color = ['#edf25e', '#3299e3', '#e32b31'], edgecolor = 'black', linewidth = 2)
axs[1, 1].set_title('Deaths by cause in the world in 2017', fontdict = {'fontweight': 'bold', 'fontsize':13})
axs[1, 1].set_xlabel('Death causes', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
axs[1, 1].set_ylabel('Percentage of deaths', fontdict = {'fontstyle': 'italic', 'fontsize': 13})
bars_2017[0].set_hatch('.')


# Setting yticks for the bar charts.
for ax in axs.flat:
    ax.set(yticks = [10, 20, 30, 40, 50, 60, 70])
    
# Removing xlabels and y labels between the bar charts.
#for ax in axs.flat:
#    ax.label_outer()

# Setting the space between each bar chart.
fig.tight_layout(pad = 4.0)

#plt.savefig('intro.png', dpi = 150)
plt.show()


# ----  ---- Graph 2 ---- ----
# reference: https://ourworldindata.org/suicide
# Share of deaths from suicide

# Importing information from .csv file to a variable 'data'.
data = pd.read_csv('share-deaths-suicide.csv')

# Creating new column 'Death' and removing long column of 'Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)'.
data['Deaths'] = data['Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)']
data = data.drop(columns=['Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)'])

# Removing data rows of countries which are not Greenland, the USA, Russia, Sri Lanka, South Korea, or Uzbekistan. 
data = data.drop(index=data[(data['Entity'] != 'Greenland') & (data['Entity'] != 'United States') & (data['Entity'] != 'Russia') & (data['Entity'] != 'Sri Lanka') & (data['Entity'] != 'South Korea') & (data['Entity'] != 'Uzbekistan')].index)

# Locating data year by year. (If loop method is available, it is welcome)
year_1990 = data.loc[data['Year'] == 1990]
year_1991 = data.loc[data['Year'] == 1991]
year_1992 = data.loc[data['Year'] == 1992]
year_1993 = data.loc[data['Year'] == 1993]
year_1994 = data.loc[data['Year'] == 1994]
year_1995 = data.loc[data['Year'] == 1995]
year_1996 = data.loc[data['Year'] == 1996]
year_1997 = data.loc[data['Year'] == 1997]
year_1998 = data.loc[data['Year'] == 1998]
year_1999 = data.loc[data['Year'] == 1999]
year_2000 = data.loc[data['Year'] == 2000]
year_2001 = data.loc[data['Year'] == 2001]
year_2002 = data.loc[data['Year'] == 2002]
year_2003 = data.loc[data['Year'] == 2003]
year_2004 = data.loc[data['Year'] == 2004]
year_2005 = data.loc[data['Year'] == 2005]
year_2006 = data.loc[data['Year'] == 2006]
year_2007 = data.loc[data['Year'] == 2007]
year_2008 = data.loc[data['Year'] == 2008]
year_2009 = data.loc[data['Year'] == 2009]
year_2010 = data.loc[data['Year'] == 2010]
year_2011 = data.loc[data['Year'] == 2011]
year_2012 = data.loc[data['Year'] == 2012]
year_2013 = data.loc[data['Year'] == 2013]
year_2014 = data.loc[data['Year'] == 2014]
year_2015 = data.loc[data['Year'] == 2015]
year_2016 = data.loc[data['Year'] == 2016]
year_2017 = data.loc[data['Year'] == 2017]

# Start plotting a graph.
x = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
y = [year_1990.Deaths, year_1991.Deaths, year_1992.Deaths, year_1993.Deaths, year_1994.Deaths, year_1995.Deaths, year_1996.Deaths, year_1997.Deaths, year_1998.Deaths, year_1999.Deaths, year_2000.Deaths, year_2001.Deaths, year_2002.Deaths, year_2003.Deaths, year_2004.Deaths, year_2005.Deaths, year_2006.Deaths, year_2007.Deaths, year_2008.Deaths, year_2009.Deaths, year_2010.Deaths, year_2011.Deaths, year_2012.Deaths, year_2013.Deaths, year_2014.Deaths, year_2015.Deaths, year_2016.Deaths, year_2017.Deaths]

plt.figure(figsize = (10, 6))
plt.title('Share of deaths from suicide, 1990 to 2017', fontdict = {'size': 15, 'weight': 'bold'})
plt.ylabel('Percentage of deaths from suicide', fontdict = {'size': 12})
plt.xticks([1990, 1995, 2000, 2005, 2010, 2015, 2017])
plt.yticks([2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 8, 10, 12, 13, 14])
plt.plot(x, y, '.-', label=['Greenland', 'South Korea', 'Sri Lanka', 'Russia', 'United States', 'Uzbekistan'])
plt.legend()
#plt.savefig('deaths-from-suicide.png', dpi = 150)
plt.show()
