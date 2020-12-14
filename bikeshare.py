import numpy as np
import time
import pandas as pd
import datetime as dt

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US BikeShare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter name of the city to analyze: chicago,new york city, washington. \n ").lower()

    while city not in CITY_DATA:
        print("the city you Entered dose not exist! chose from these three cities: chicago,new york city, washington.\n ")
        city = input("Enter name of the 'City' to analyze:\n ").lower()

    # Ask user what he/she like to filter with..
    filter = input("Would you like to filter the data by 'month', 'day', or 'both'.\n").lower()

    while filter not in (['month', 'day', 'both']):
        print("You provided invalid filter")
        filter = input("Would you like to filter the data by 'month', 'day', or 'both'.\n").lower()

    # Use if statement and a while loop to handel user input..
    months = ['January', 'February', 'March', 'April', 'May', 'June']

    if filter == 'month' or filter == 'both':
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input("Which'Month'? January','February','March','April','May','June \n").capitalize()

        # Use while loop to handle invalid inputs..
        while month not in months:
            print("the month you Entered dose not exist! Try again ")
            month = input("Which'Month'? January','February','March','April','May','June\n").capitalize()
    else:
        month = 'all'

    # Use if statement and a while loop to handel user input..
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    if filter == 'day' or filter == 'both':
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Which'Day'? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday. \n").capitalize()

        # Use while loop to handle invalid inputs..
        while day not in days:
            print("the day you Entered dose not exist! Try again ")
            day = input("Which'Day'? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday. \n").capitalize()
    else:
        day = 'all'

    print('-' * 40)
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
    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new DataFrame
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # extract start_hour from Start Time to create new columns
    df['Start_hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    common_start_hour = df['Start_hour'].mode()[0]

    print(f"Month = {common_month}\nDay of Week = {common_day}\nPopular Start Hour = {common_start_hour}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    start_station = df["Start Station"].mode()[0]

    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    combination = 'From ' + df['Start Station'] + ' To ' + df['End Station']
    popular_trip = combination.mode()[0]

    print(f"Start Station: {start_station}\nEnd Station: {end_station}\nPopular Trip: {popular_trip}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    Total = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    Mean = Total / len(df['Trip Duration'])

    print(f"Total Travel Time = {Total}\nMean Travel Time = {Mean}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on BikeShare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"User Type: \n{user_type}\n")

    # TO DO:Chick if the city has Gender column then display counts of gender
    if 'Gender' in (df.columns):
        gender = df['Gender'].value_counts()
        print(f"Gender: \n{gender}\n")

    # TO DO: Chick if the city has Gender column then display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        popular_year = df['Birth Year'].mode()[0]
        print(f"Year Birth States:\nEarliest_year = {earliest_year}, Most_recent_year = {most_recent_year}, Popular_year = {popular_year}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    

def ask_user(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')

        start_loc = 0
        end_loc = 5

        while view_data == 'yes':
            print(df.iloc[start_loc:end_loc])

            view_display = input("Do you wish to continue?: ").lower()

            if view_display == 'yes':
                print("You say yes .. So i will shaw you another 5 rows :)\n")
                start_loc += 5
                end_loc += 5
                continue
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_user(df)

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
