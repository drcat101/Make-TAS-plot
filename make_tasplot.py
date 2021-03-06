
## Uses John Stevenson's 'tasplot' code to produce Total Alkali vs Silica (TAS) plot.
## Single group of samples only.
## Heavily based on Volcan01010 blog post "Easily plot magma compositions (TAS diagrams) in Python", January 28, 2015
## Link: http://all-geo.org/volcan01010/2015/01/easily-plot-magma-compositions-tas-diagrams-in-python/

def makeTAS(csvFile, dataLabel, outputFileName):

    # Import the required modules
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import tasplot

    # Read in .csv file to Pandas dataframe
    df = pd.read_csv(csvFile, index_col=0)
    silica = df['SiO2'].tolist()
    alk = np.array(df['Na2O']) + np.array(df['K2O'])
    alkalis = alk.tolist()

    # Change the font for all text and labels on the final plot
    plt.rcParams['font.family'] = 'Arial'

    # Set up figure
    ax1 = plt.subplot(111)  # create axes and store as variable
    tasplot.add_LeMaitre_fields(ax1)  # add TAS fields to plot

    # Plot the data
    ax1.plot(silica, alkalis, 'd', markerfacecolor='k', markeredgecolor='k', markersize=8, label=dataLabel)
    
    # Decorate the plot
    plt.xlabel(r'SiO$_2$ (wt%)')  # Use LaTeX notation for subscript
    plt.ylabel(r'Na$_2$O + K$_2$O (wt%)')
    name = outputFileName + '.pdf'
    plt.savefig(name, dpi = 300, bbox_inches = 'tight', pad_inches = 0.25)


