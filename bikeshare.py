# Modify as requested by git project
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def see_city(see):
   try:
    i=0
    df=pd.read_csv(CITY_DATA[see])   
    pd.set_option('display.max_columns',200)                
    print(df[i:i+5])
    next = False
    while next==False:
        more=input("Would you like to see next 5 rows of " + see +" city (yes/no)?: ").lower().strip()               
        while more not in ['yes','no']:
            more=input("Please type yes/no only to see next 5 rows of " + see +" city !!!: ").lower().strip()                       
        while True:
            if more=='yes': 
               # print("The next 5 rows of chicago city as following: ")                                    
                i +=5
                print(df[i:i+5])
                break
            else:
                print("you select not to see any more rows of " + see + " city")
                next=True
                break
                    
   except Exception as e:
      print(e)            

def display_raw_data():
    """ Let user see the raw data if they like """

    raw=input("Would you like to see the raw data (yes/no) ?").lower().strip()
    while raw not in ['yes','no']:
        raw=input("Please type yes/no only !!!").lower().strip()
        
   
   # while True:
    if raw=='yes':
        see=input("Which city would you like to see (chicago, washington, new york city) ?: ").lower().strip()
        while see not in ['chicago','washington','new york city']:
           see=input("Please type city as chicago, washington, new york city only !!!: ").lower().strip()
           
        if see=='chicago':
            see_city('chicago')
        elif see=='washington':
             see_city('washington')
        else:
             see_city('new york city')
        
    else:
        print("you select no")

                            

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    try:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('Enter chicago city or washington city or new york city for your analyst : ').lower().strip()
        while city not in ['chicago','washington','new york city']:
            city = input('Please enter chicago city or washington city or new york city for your analyst only!!! : ').lower().strip()
        
   # if check1==True:
    #    break
    
    # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Enter month as one of first 6 months (only january, february, march, april, may, june or all): ')
        while month not in ['january','february','march','april','may','june','all']:
            month = input('Please enter month (only january, february, march, april, may, june or all): ')
        
        #if check2==True:
         #   break
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Enter day of week (monday, tuesday, wednesday, thursday, friday, saturday, sunday or all): ')
        while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            day = input('Pleaseenter day of week (monday, tuesday, wednesday, thursday, friday, saturday, sunday or all): ')
    
        #if check3==True:
         #   break
    
        print('-'*40)
        return city, month, day

    except Exception as e:
        print(e)
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
    try:
    # extract data by city name
        df=pd.read_csv(CITY_DATA[city])

    # Make column 'Start Time' as datetime format
        df['Start Time']=pd.to_datetime(df['Start Time'])

    # create a new column as named 'month'
        df['month']=df['Start Time'].dt.month

    # create a new column as named 'week_of_day'
        df['week_of_day']=df['Start Time'].dt.day_name()
        if(city=='washington'):
            df['Gender']='Not Available'
            df['Birth Year']='Not Availble'

    # condition to get data by month

        if month !='all':
            months=['january','febuary','march','april','may','june']
        # get a right month plus 1, cause array starts 0
            month=months.index(month)+1
        # to get dat by month in column 'month'
            df=df[df['month']==month]
    
    # condition to get data by day of week
        if day !='all':
            df=df[df['week_of_day']==day.title()]
         

        return df
    except Exception as e:
        print(e)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('the most common month: ',popular_month)

    # TO DO: display the most common day of week
    popular_day=df['week_of_day'].mode()[0]
    print('the most common day of week: ',popular_day)
    
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('the most common start hour: ',popular_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_sation=df['Start Station'].mode()[0]
    print('most commonly used start station:',popular_start_sation)

    # TO DO: display most commonly used end station
    popular_end_sation=df['End Station'].mode()[0]
    print('most commonly used end station:',popular_end_sation)
    
    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_sation=df[['Start Station','End Station']].mode().loc[0]
    print('most frequent combination of start station and end station trip:',popular_start_end_sation)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time: ',round(total_travel_time,3))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time: ',round(mean_travel_time,3))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_type_count=df['User Type'].value_counts()
    print('The counts of user types:',user_type_count)

    # TO DO: Display counts of gender
    gender_count=df['Gender'].value_counts()
    print('The sum of gender:',gender_count)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    
    erliest_year=df['Birth Year'].min()
    
    recent_year=df['Birth Year'].max()

    common_year=df['Birth Year'].value_counts().idxmax()
    
    print('The earliest, most recent, and most common year of birth:',erliest_year,recent_year,common_year)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def main():
    while True:
        display_raw_data()
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
