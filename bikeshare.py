import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }




def get_filters():
    city = None
    month = None
    day = None
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    cities = ['chicago', 'new york city','washington']
    while city not in cities:
        city = input('Would you like to see data for Chicago, New York City, or Washington?: ').lower().strip()
        if city not in cities:
            print('That is not a valid choice, please try again.')


    # TODO: check for 1st letter month capitals
    # get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months:
        month = input('Choose a month between Jan and June or type all:').lower().strip()
        if month not in months:
            print('That is not a valid choice, please try again.')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
            day = input('Choose a day of the week or type all:').lower().strip()
            if day not in days:
                print('That is not a valid choice, please try again.')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
  # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df = df.dropna()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most popular month: ', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is:' , common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most popular hour to ride is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is', end_station)

    # display most frequent combination of start station and end station trip
    df['Frequent Combo'] = df['Start Station'] + ', ' + df['End Station']
    freq = df['Frequent Combo'].mode()[0]
    print('Most popular trip: ', freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # df['Birth Year'] = df['Birth Year'].astype(int)

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nWhat is the breakdown of users?\n', user_type)

    # Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nWhat is the breakdown of gender?\n', user_gender)
    except KeyError:
        print('No data to show for gender.')

    # Display earliest, most recent, and most common year of birth
    try:
        early_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest birth year: ', early_year)
        print('Most recent birth year: ', recent_year)
        print('Most common birth year: ', common_year)
    except KeyError:
        print('No data to show for birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays five lines of raw data at a time."""
    count = 5
    start = 0
    while True:
        answer = input('Do you want to see the raw data?')
        if answer == 'yes':
            print(df[start:count])
            count += 5
            start += 5
        else:
            break

def main():
    """Main function that runs the program."""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        """Option for user to quit or restart the program."""
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
