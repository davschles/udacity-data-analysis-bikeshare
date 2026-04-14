import pandas as pd

def question(input_dict, topic):
    """Shows the user the different values that can be chosen and record his selection
    INPUT:
    input_dict: dictionnary. Contains values to be chosen.
    topic: string. Used to display the right topic into the asked question
    OUTPUT:
    question_result: int. Selected number by the user.
    """
    # Make a list out the input dictionnary 
    list_q = sorted(input_dict.keys())
    
    # Formulate question for user input, incl. selection list.
    question = '\nSelect the {} that you are interrested in ?\n'.format(topic).upper()
    for i in list_q:
        question += '{} - {}\n'.format(i, input_dict[i].title())

    # Ask user for value and force that an integer is enterred
    return int(input(question))

def question_check_entry(input_dict, topic):
    """Ensures the the correct handling of incorrect inputs given by the user
    to answer the question. Question in asked again if exception and entered value
    is verified in dedicated dictionnary.
    INPUT:
    input_dict: dictionnary. Contains values to be chosen by the user.
    topic: string. Used to display the right topic into the asked question
    OUTPUT:
    question_result: int. Selected number by the user (checked).
    """

    # Usage of zip to make a list out of input dictionnary (.keys() method also possible)
    a, b = zip(*input_dict.items())
    a = sorted(a)
    
    # Main loop
    while True: 

        # Loop for treatment of exceptions (new user input if exception)   
        while True:
            try:
                entry = question(input_dict, topic)
                break
            except:
                print( 'invalid entry - please enter a correct number for your selection'.upper() )

        # Check that user entry is meaningfull (exists in corresponding dictionnary)
        if (entry >= 0) and (entry <= max(a)):
            break
        else:
            print( 'invalid number entered, please retry'.upper() )
    
    # Checked user entry returned
    return input_dict[entry]

def load_data(file, month, day):
    """Load Dataframe from specified .csv file, filters the rows 
    according to user selections and create two columns inside.
    Exceptions managed (eg. wrong file name)
    INPUT:
    file: string. .csv file to import as dataframe
    month: string. Month selected by user.
    day: string. Day selected by user.
    OUTPUT:
    df: dataframe. Filtered dataframe accoring to user selections.
    """

    # Main loop including exception handling
    while True:
        try:
            # Load data file into a dataframe
            df = pd.read_csv(file)
                
            # Convert the Start Time column to datetime
            df['Start Time'] = pd.to_datetime(df['Start Time'])
    
            # Extract month and day of week from Start Time to create new columns"
            df['month'] = df['Start Time'].dt.month_name()
            df['day_of_week'] = df['Start Time'].dt.day_name()
    
            # Filter by month if applicable
            if month != 'all':
                df = df[df['month'] == month.title()]
    
            # Filter by day of the week if applicable
            if day != 'all':
                df = df[df['day_of_week'] == day.title()]

        # Exception if wrong file name and stay in the loop
        except:
            print('please enter a right file name (file should be located in project folder)')
            break
        # Exit the loop if file loading is fine.
        else:
            break

    # Dataframe returned
    return df

def infos_dataset(df):
    """Display useful datafrme informations and returns its size
    INPUT:
    df: Dataframe. Dataframe to be considered
    OUTPUT:
    df_size: int. Number of rows in df.
    """
    # Display header
    print( '\n' + 'Infos about dataset'.upper() + '\n' + '='*40 )
    
    # Display size of df 
    print( 'Size:            {} samples'.format(df.shape[0]) )
    
    # Display soonest and latest records of df
    print( 'Earliest record: {}'.format(df['Start Time'].min()) )
    print( 'Latest record:   {}'.format(df['Start Time'].max()) )
    
    # Return size of df
    return df.shape[0]

def popular_times_of_travel(df, header, month_select, day_select):
    """Computes and displays required statistics about popular times of travel
    INPUT:
    df: Dataframe. Dataframe to be considered
    header: str. Content of the diplayed header.
    month_select: string. Month selected by user.
    day_select: string. Day selected by user.
    """
    
    # Display header
    print( '\n' + header.upper() )
    print( '=' * 40 )

    # Statistics diplayed depending on user selection
    if month_select == 'all':
        print('Most common month:       {}'.format(df['Start Time'].dt.month_name().mode()[0]))
    if day_select == 'all':
        print('Most common day of week: {}'.format(df['Start Time'].dt.day_name().mode()[0]))
    
    # Statistic always diplayed
    print('Most common hour of day: {}'.format(df['Start Time'].dt.hour.mode()[0]))
    
    return

def popular_stations_and_trips(df, header):
    """Computes and displays required statistics about popular station and trips.
    INPUT:
    df: Dataframe. Dataframe to be considered
    header: str. Content of the diplayed header.
    """

    # Display header
    print( '\n' + header.upper() )
    print( '=' * 40 )

    # Compute and display most common start/end stations 
    print( 'Most common Start Station: {}'.format(df['Start Station'].mode()[0]) )
    print( 'Most common End Station:   {}'.format(df['End Station'].mode()[0]) )

    # Create a serie that concatenates start / end station for each record
    a = df['Start Station'] + ' - ' + df['End Station']
    print( 'Most common Trip:          {}'.format(a.mode()[0]) )

    return

def trip_duration(df, header):
    """Computes and displays required statistics about trip duration.
    INPUT:
    df: Dataframe. Dataframe to be considered
    header: str. Content of the diplayed header.
    """

    # Display header
    print( '\n' + header.upper() )
    print( '=' * 40 )

    # Total travel time converted in hours
    print( 'Total travel time: {} hours'.format(df['Trip Duration'].sum() // 3600) )
    # Average travel time converted in min:sec
    print( 'Average travel time: {} min {} sec'.format(int(df['Trip Duration'].mean() // 60), int(df['Trip Duration'].mean()%60)) )

    return

def user_info(df, header):
    """Computes and displays required statistics about user information.
    INPUT:
    df: Dataframe. Dataframe to be considered
    header: str. Content of the diplayed header.
    """

    # Display header
    print( '\n' + header.upper() )
    print( '=' * 40 )

    # Compute and display number of each user type
    print( 'Count of User types:' )
    for i, user_type in enumerate(df['User Type'].value_counts().index):
        print( '\t' + '{}: {}'.format(user_type, df['User Type'].value_counts()[i]) )

    # If given in df, compute and display number of each gender type
    print( '\n' + 'Count of Genders:' )
    if 'Gender' in df.columns:
        for i, gender in enumerate(df['Gender'].value_counts().index):
            print( '\t' + '{}: {}'.format(gender, df['Gender'].value_counts()[i]) )
    else:
        print( '\t' + 'not available' )

    # If given in df, compute and display number age related statistics
    print( '\n' + 'Age related stats:' )
    if 'Birth Year' in df.columns:
        print( '\t' + 'Earliest year of birth:    {}'.format(int(df['Birth Year'].min())) )
        print( '\t' + 'Most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])) )
        print( '\t' + 'Most recent year of birth: {}'.format(int(df['Birth Year'].max())) )
    else:
        print( '\t' + 'not available' )
    
    return