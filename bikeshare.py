import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            city = input('Type city name to analyze:').lower()
            if city not in CITY_DATA.keys():
                raise Exception
    # TO DO: get user input for month (all, january, february, ... , june)
            month = input('Type month name to filter data or all to apply no filter:').lower()
            if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                raise Exception
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day_of_week = input('Type day of week to filter data or all to apply no filter:').lower()
            if day_of_week not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                raise Exception
            break
        except Exception:
            print(Exception)
    print('-'*40)
    return city, month, day_of_week


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


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

    # TO DO: display the most common month
    print('mode month for travel is: '+ df['Start Time'].dt.month.mode().astype(str))

    # TO DO: display the most common day of week
    print('mode day of week for travel is:'+ df['Start Time'].dt.weekday_name.mode().astype(str))

    # TO DO: display the most common start hour
    print('mode hour of day for travel', df['Start Time'].dt.hour.mode().astype(str))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('mode of start station for travel is: ' , df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print('mode of end station for travel is: ', df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip is: ', df[['Start Station', 'End Station']].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime( df['Start Time'] )
    df['End Time'] = pd.to_datetime( df['End Time'] )
    df['Trip Time'] = df['End Time'] -df['Start Time']
    print('Total travel time equals:', sum( df['Trip Time'].astype(int) ))

    # TO DO: display mean travel time
    print('Mean travel time equals:', df['Trip Time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types equals: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Counts of gender equals: ', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    #df['Bearth Year'] = pd.to_datetime( df['Birth Year'] )
    print('Earliest, most recent, and most common year of birth equals: ', df['Birth Year'].min(), ', ' df['Birth Year'].max(), ', ' df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
