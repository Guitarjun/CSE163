"""
Arjun Srivastava
Section AB
HW 3: Data Analysis
Contains methods, graphs, and a regression model for
dealing with an Education dataset
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from cse163_utils import assert_equals
sns.set()


# Part 0: Statistical Functions with Pandas

def compare_bachelors_1980(df):
    """
    Compares the difference between men and woman for completion of
    a bachelor's degree in 1980, with the result as a
    DataFrame with a row for men and a row for women with the
    columns "Sex" and "Total"
    """
    year = df['Year'] == 1980
    degree = df['Min degree'] == "bachelor's"
    genders = df['Sex'].isin(['M', 'F'])
    filtered_df = df[year & degree & genders]
    return filtered_df.loc[:, ['Sex', 'Total']]


def top_2_2000s(df):
    """
    For the given DataFrame, returns the top two values of a Series
    of most commonly awarded levels of education and their respective
    percentage
    """
    year = (df['Year'] >= 2000) & (df['Year'] <= 2010)
    sex = df['Sex'] == 'A'
    return df[year & sex].groupby('Min degree')['Total'].mean().nlargest(2)


def percent_change_bachelors_2000s(df, sex='A'):
    """
    For the given DataFrame and sex (default "all genders"),
    returns the difference between total percent of bachelor's
    degrees received in 2000 as compared to 2010 as a float
    """
    century = df['Year'] == 2000
    decade = df['Year'] == 2010
    gend = df['Sex'] == sex
    first = df[century & gend].groupby('Min degree')['Total'].sum()
    second = df[decade & gend].groupby('Min degree')['Total'].sum()
    return second["bachelor's"] - first["bachelor's"]


# Part 1: Plotting with Seaborn
def line_plot_bachelors(df):
    """
    Plots the total percentages of all people of bachelor's
    degree as minimal completion with a line chart over years
    based on the given DataFrame
    """
    degree = df['Min degree'] == "bachelor's"
    gend = df['Sex'] == 'A'
    filtered_df = df[degree & gend]
    sns.relplot(x='Year', y='Total', data=filtered_df, kind='line')
    plt.title("Percent Earning Bachelor's over Time")
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(df):
    """
    Plots the total percentages of women, men, and total people
    with a minimum education of high school degrees in the year 2009
    based on the given DataFrame
    """
    high = df['Min degree'] == 'high school'
    year = df['Year'] == 2009
    filtered_df = df[high & year]
    sns.catplot(x='Sex', y='Total', data=filtered_df, kind='bar')
    plt.title('Percentage Completed High School by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(df):
    """
    Plots the results of how the percent of Hispanic individuals
    with degrees has changed between 1990 and 2010 (inclusive)
    for high school and bachelor's degrees with a scatter plot
    based on the given DataFrame
    """
    filtered_df = df[['Min degree', 'Total', 'Hispanic', 'Year']]
    degree = (filtered_df['Min degree'] == 'high school') | (
        filtered_df['Min degree'] == "bachelor's")
    filtered_df = filtered_df[degree]
    sns.relplot(
        x='Year', y='Total', data=filtered_df, hue='Min degree', kind='line')
    plt.title(
        "Percent of Hispanics earning \
        High School and Bachelor's Degrees over Time")
    plt.xlabel('Year')
    plt.ylabel('Percengage')
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


# Part 2: Machine Learning using scikit-learn
def fit_and_predict_degrees(df):
    """
    Takes in a DataFrame and returns the mean squared error
    of the model fitting year, degree type, and sex to predict
    the percent of individuals of the specified sex to achieve
    that degree type in the specified year
    """
    filtered_df = df[['Year', 'Min degree', 'Total', 'Sex']]
    filtered_df = filtered_df.dropna()
    features = filtered_df.loc[:, filtered_df.columns != 'Sex']
    features = pd.get_dummies(features)
    labels = filtered_df['Sex']
    labels = pd.get_dummies(labels)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    test_predictions = model.predict(features_test)
    return mean_squared_error(labels_test, test_predictions)


def main():
    # Parsed data
    data = pd.read_csv('/home/hw3-nces-ed-attainment.csv', na_values='---')

    # Part 0 Methods
    print('Running tests...')
    assert_equals(24.0, compare_bachelors_1980(data).loc[112, 'Total'])
    assert_equals(2.5999, percent_change_bachelors_2000s(data))
    assert_equals(
        {'high school': 87.557143, "associate's": 38.757143},
        dict(top_2_2000s(data)))
    print('All tests passed!')

    # Part 1 Graphs
    print('Creating graphs...')
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    print('Graphs created!')

    # Part 2 Machine Learning
    print('Fitting model...')
    print('Mean squared error:', fit_and_predict_degrees(data))
    print('Model finished!')


if __name__ == '__main__':
    main()
