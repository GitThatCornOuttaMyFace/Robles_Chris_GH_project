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

    """ - This website helped me crack the data validation problem:
            https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
        - This site helped me understand 'break, pass, and continue':
            https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3#pass-statement
        - This site helped me concatenate two string columns, which is how I got the most popular route:
            http://www.datasciencemadesimple.com/concatenate-two-columns-dataframe-pandas-python-2/
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Which city would you like to analyze (chicago, new york city, washington)? '))
            if city.lower() not in ['chicago', 'new york city', 'washington']:
                print('That\'s not a valid city, try again...')
                continue
            break
        except ValueError:
            print('That\'s not a valid city')
        except :
            print('That\'s not a valid city')
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Which month would you like to analyze (all, january, february, ... , june)? '))
            if month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                print('That\'s not a valid month, try again...')
                continue
            break
        except ValueError:
            print('That\'s not a valid month')
            break



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Which day would you like to analyze (all, monday, tuesday, ... sunday)? '))
            if day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                print('That\'s not a valid day of the week, try again...')
                continue
            break
        except ValueError:
            print('That\'s not a valid day')
            break
        except KeyError:
            print('That\'s not a valid day')
            break

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

    # display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular start month:', popular_month)


    # display the most common day of week
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.weekday

    # find the most popular hour
    popular_day = df['day'].mode()[0]
    wkday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    print('Most Popular Start day:', wkday[popular_day])


    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print('popular station: ', popular_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('popular station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Start and End Stations'] = df['Start Station'] +' -- to -- ' + df['End Station']
    popular_route = df['Start and End Stations'].mode()[0]
    total_popular_route = df['Start and End Stations'].count()
    print('popular route: ', popular_route)
    print('popular route used ', total_popular_route,' times.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total = df['Trip Duration'].sum()
    print ("Total Trip Duration in seconds: ", Total)
    print ("Total Trip Duration in minutes: ", Total//60)
    print ("Total Trip Duration in hours:   ", Total//60//60)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display mean travel time
    TotalAve = df['Trip Duration'].mean()
    print ("Total Trip Average Duration in seconds: ", TotalAve)
    print ("Total Trip Average Duration in minutes: ", TotalAve//60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Total Number of User Types:\n', df['User Type'].value_counts())
    print()

    # Display counts of gender
    print('Total Riders by Gender:\n', df['Gender'].value_counts())
    print()

    # Display earliest, most recent, and most common year of birth
    print('Oldest Rider Birth Year:   ', df['Birth Year'].min())
    print('Youngest Rider Birth Year: ', df['Birth Year'].max())
    print('Most Common Birth Year:    ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        proceed = input('\nWould you like to continue? Enter yes or no.\n')
        if proceed.lower() != 'yes':
            break
        station_stats(df)
        trip_duration_stats(df)

        if city != 'washington':
            user_stats(df)
        else:
            print()
            print('-- User stats not available for Washington. --')




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
