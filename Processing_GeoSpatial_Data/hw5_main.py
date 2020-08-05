"""
Arjun Srivastava
HW 5: Processing Geospatial Data
Section AB
Contains various methods for describing and plotting food access data
in Washington
"""
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# Part 0
def load_in_data(file_shp, file_csv):
    """
    Takes the file name of a shape file of Census Tract shapes
    and the file name of a CSV containing food access data
    Returns a GeoDataFrame that has the two datasets merged together
    """
    csv = pd.read_csv(file_csv)
    shp = gpd.read_file(file_shp)
    joined = shp.merge(csv, left_on='CTIDFP00',
                       right_on='CensusTract', how='left')
    return joined


# Part 1: data is only parameter
def percentage_food_data(data):
    """
    Returns the percentage of census tracts in Washington that there is
    data for
    """
    return float(data['CensusTract'].count() / data['CTIDFP00'].count())


def plot_map(data):
    """
    Plots a map of Washington and saves it as washington_map.png
    """
    data.plot()
    plt.title('Map of Washington')
    plt.savefig('washington_map.png')


def plot_population_map(data):
    """
    Plots a map of Washington with each census tract colored by its population
    and saves it as washington_population_map.png
    """
    fig, ax = plt.subplots(1)
    data.plot(color='#CCCCCC', ax=ax)
    data.plot(column='POP2010', legend=True, ax=ax)
    ax.set_title('Populations of Census Tracts in Washington')
    plt.savefig('washington_population_map.png')


def plot_population_county_map(data):
    """
    Plots a map of Washington with each county colored by its population
    and saves it as washington_county_population_map.png
    """
    fig, ax = plt.subplots(1)
    data.plot(color='#CCCCCC', ax=ax)
    data_copy = data[['County', 'POP2010', 'geometry']]
    data_copy = data_copy.dissolve(by='County', aggfunc='sum')
    data_copy.plot(column='POP2010', legend=True, ax=ax)
    ax.set_title('Populations of Counties in Washington')
    plt.savefig('washington_county_population_map.png')


def plot_food_access_by_county(data):
    """
    Makes 4 plots conveying different information
    about 'low access' Census Tracts in Washington
    and saves the figure as washington_county_food_access.png
    """
    # Creating clone of the data and aggregating it
    counties = data[['County', 'geometry', 'POP2010',
                    'lapophalf', 'lapop10', 'lalowihalf', 'lalowi10']].dropna()
    counties = counties.dissolve(by='County', aggfunc='sum')
    # Creating new columns in the data
    counties['lapophalf_ratio'] = counties['lapophalf'] / counties['POP2010']
    counties['lapop10_ratio'] = counties['lapop10'] / counties['POP2010']
    counties['lalowihalf_ratio'] = counties['lalowihalf'] / counties['POP2010']
    counties['lalowi10_ratio'] = counties['lalowi10'] / counties['POP2010']
    # Creating figure
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 10), ncols=2)
    # Plotting maps
    data.plot(ax=ax1, vmin=0, vmax=1, color='#CCCCCC')
    counties.plot(column='lapophalf_ratio', vmin=0,
                  vmax=1, ax=ax1, legend=True)
    ax1.set_title('Low Access: Half')
    data.plot(ax=ax2, vmin=0, vmax=1, color='#CCCCCC')
    counties.plot(column='lalowihalf_ratio', vmin=0,
                  vmax=1, ax=ax2, legend=True)
    ax2.set_title('Low Access + Low Income: Half')
    data.plot(ax=ax3, vmin=0, vmax=1, color='#CCCCCC')
    counties.plot(column='lapop10_ratio', vmin=0, vmax=1, ax=ax3, legend=True)
    ax3.set_title('Low Access: 10')
    data.plot(ax=ax4, vmin=0, vmax=1, color='#CCCCCC')
    counties.plot(column='lalowi10_ratio', ax=ax4, vmin=0, vmax=1, legend=True)
    ax4.set_title('Low Access + Low Income: 10')
    fig.savefig('washington_county_food_access.png')


def plot_low_access_tracts(data):
    """
    Plots all of the Census Tracts that are considered 'low access' on a map of
    Washington and saves the file as washington_low_access.png
    """
    data_copy = data.copy()
    laurban = (data_copy['Urban'] == 1) & \
              ((data_copy['lapophalf'] > 500) | (data_copy['lapophalf'] /
                                                 data_copy['POP2010'] > .33))
    larural = (data_copy['Rural'] == 1) & \
              ((data_copy['lapop10'] > 500) | (data_copy['lapop10'] /
                                               data_copy['POP2010'] > .33))
    data_copy['low_access'] = laurban | larural
    fig, ax = plt.subplots(1)
    data.plot(ax=ax, color='#EEEEEE')
    food_data = data_copy[data_copy['POP2010'].notnull()]
    food_data.plot(ax=ax, color='#AAAAAA')
    low_access = food_data[food_data['low_access']]
    low_access.plot(ax=ax)
    ax.set_title('Low Access Census Tracts in Washington')
    fig.savefig('washington_low_access.png')


def main():
    data = load_in_data(
            '/course/food-access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
            '/course/food-access/food-access.csv')
    plot_map(data)
    plot_population_map(data)
    plot_population_county_map(data)
    plot_food_access_by_county(data)
    plot_low_access_tracts(data)


if __name__ == '__main__':
    main()
