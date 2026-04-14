import bikeshare_functions as pf

# Dictionary containing data .csv files
CITY_DATA = { 'chicago': 'data/chicago.csv',
              'new york city': 'data/new_york_city.csv',
              'washington': 'data/washington.csv' 
            }

# Dictionary containing the cities and their selection numbers
cities = { 0: 'chicago',
           1: 'new york city',
           2: 'washington'
         }

# Dictionary containing the months and their selection numbers
months = { 0: 'all',
           1: 'january',
           2: 'february',
           3: 'march',
           4: 'april',
           5: 'may',
           6: 'june',
           7: 'july',
           8: 'august',
           9: 'september',
           10: 'october',
           11: 'november',
           12: 'december'
         }

# Dictionary containing the days and their selection numbers
days = { 0: 'all',
         1: 'monday',
         2: 'tuesday',
         3: 'wednesday',
         4: 'thursday',
         5: 'friday',
         6: 'saturday',
         7: 'sunday'
       }

# Dictionary containing the topics and their selection numbers
topics = { 0: 'all',
           1: 'popular times of travel',
           2: 'popular stations and trips',
           3: 'trip duration',
           4: 'user info'
         }

# Main loop to enable quit function
quit = False
while quit == False:

    # Get  and check user inputs
    city_selected = pf.question_check_entry(cities, 'city')
    month_selected = pf.question_check_entry(months, 'month')
    day_selected = pf.question_check_entry(days, 'day')
    
    # Load, check and filter data from .csv file
    data = pf.load_data(CITY_DATA[city_selected], month_selected, day_selected)
    samples = pf.infos_dataset(data)
    
    # make sure that the dataframe is not empty
    if samples > 0:
        
        # Propose display of raw data to the user
        start_raw = input('\nDo you want to display the five first rows of the raw data?'.upper() + '  yes / no\n').lower()
        if start_raw == 'yes':
            print('\nraw data'.upper() + '\n' + '='*40)
            i = 1
            while True:

                if i>1:                    
                    continue_raw = input('\nDisplay the next five raw data rows?'.upper() + '  yes / no\n').lower()
                else:
                    continue_raw = 'yes'
                    
                if continue_raw == 'yes':
                    print(data.iloc[(i-1)*5:i*5]) 
                    i += 1
                elif continue_raw == 'no':
                    break
                else:
                    print('wrong value'.upper())
            
        elif start_raw == 'no':
            print('no raw data visualization'.upper())
        
        else:
            print('wrong input - raw data visualization aborted'.upper())         

        # User selects a topic        
        topic_selected = pf.question_check_entry(topics, 'topic')

        # If selected, compute "popular times of travel" statistics
        if (topic_selected == 'popular times of travel') or (topic_selected == 'all'):
            pf.popular_times_of_travel(data, 'popular times of travel', month_selected, day_selected)

        # If selected, compute "popular stations and trips" statistics
        if (topic_selected == 'popular stations and trips') or (topic_selected == 'all'):
            pf.popular_stations_and_trips(data, 'popular stations and trips')

        # If selected, compute "trip duration" statistics
        if (topic_selected == 'trip duration') or (topic_selected == 'all'):
            pf.trip_duration(data, 'trip duration')

        # If selected, compute "user info" statistics
        if (topic_selected == 'user info') or (topic_selected == 'all'):
            pf.user_info(data, 'user info') 
        
        # Propose to quit the program
        while True:
            
            # User input to quit
            quit_selection = input('Do you want to quit?'.upper() + '    yes / no\n' ).lower()
            
            if quit_selection == 'yes':
                quit = True
                print( 'see you next time!'.upper())
                break
            elif quit_selection == 'no':
                break
            else:
                print( 'wrong entry.'.upper())

    # new cycle if dataframe empty
    else:
        print( '\nNo data recorded for {} in the selected time period, please select valid criteria.'.format(city_selected).upper() )