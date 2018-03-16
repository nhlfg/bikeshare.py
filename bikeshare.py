
import datetime
import time
import sys
import csv

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's
    bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''

    file_name = ''

    while True:
        try:
            city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                         'Would you like to see data for '
                         'Chicago, New York, or Washington?\n')

            if city.lower() == 'chicago' or city.lower() == 'washington':
                file_name = str(city.lower() + '.csv')
                break
            elif city.lower() == 'new york':
                file_name = str(city.lower().replace(' ','_') + '_city.csv')
                break
            else:
                print ('That does not compute!\n')

        except KeyboardInterrupt:
            sys.exit()

        finally:
            if not KeyboardInterrupt:
                pass

    return file_name


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str)'month','day' or 'none'
    '''

    time_filter = ''

    while True:
        try:
            time_period = input('\nWould you like to filter the data by '
                                'month, day, weekday or not at all? '
                                'Type "none" for no time filter.  \n')

            if (time_period.lower() == 'month'
            or time_period.lower() == 'day'
            or time_period.lower() == 'weekday'
            or time_period.lower() == 'none'):
                time_filter = time_period.lower()
                break
            else:
                print ('Try again, please type one of the options listed.  \n')


        except KeyboardInterrupt:
            sys.exit()

        finally:
            if not KeyboardInterrupt:
                pass

    return time_filter


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str)name of the month selected
    '''

    month_selected = ''
    possible_answers = ['january', 'february',
                        'march', 'april',
                        'may', 'june']

    while True:
        try:
            month = input('\nWhich month? January, February, March, April, '
                          'May, or June?  \n')

            if month.lower() in possible_answers:
                month_selected = month.lower()
                break
            else:
                print ('Try again, please type one of the months listed.  \n')

        except KeyboardInterrupt:
            sys.exit()

        finally:
            if not KeyboardInterrupt:
                pass

    return month_selected


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        month
    Returns:
        (str)day number
    '''

    day_selected = ''

    while True:
        try:
            day = int(input('\nWhich day? Please type your response as '
                        'an integer.  \n'))

            if ((month == 'january'
                 or  month == 'march'
                 or  month == 'may')
                 and day > 0
                 and day < 32):
                day_selected = str(day)
                break
            elif ((month == 'april'
                   or  month == 'june')
                   and day > 0
                   and day < 31):
                day_selected = str(day)
                break
            elif  month == 'febraury' and  day > 0 and day < 29:
                day_selected = str(day)
                break
            else:
                print ('Are you sure there is a '
                       + str(str(day))
                       + ' day in '
                       + str(month).title() + '?\n')

        except ValueError:
            print ('Integers only, please.')

        except KeyboardInterrupt:
            sys.exit()

        finally:
            if not KeyboardInterrupt:
                pass

    return day_selected


def get_weekday():
    '''Asks the user for a day and returns the specified day.

    Args:
        month
    Returns:
        (str)day number
    '''

    weekday_selected = ''
    possible_answers = ['sunday', 'monday', 'tuesday',
                        'wednesday, thursday, friday',
                        'saturday']

    while True:
        try:
            weekday = (input('\nWhich weekday? \n'))

            if weekday.lower() in possible_answers:
                weekday_selected = weekday.title()
                break

            else:
                print ('Please type Sunday, Monday, Tuesday, Etc.\n')

        except KeyboardInterrupt:
            sys.exit()

        finally:
            if not KeyboardInterrupt:
                pass
    return weekday_selected


def data_compiler(city_file, time_period, month, month_number, day, weekday):
    '''Extracts data from original csv file according to user input,
    and makes the neccesary lists for the rest of functions to work

    arguments
        city_file, time_period, month, month_number, day
    Returns
        start_time_list, trip_duration_list, start_station_list,
        end_station_list, trip_list, user_list, gender_list, birth_list
    '''

    start_time_list = []
    trip_duration_list = []
    start_station_list = []
    end_station_list = []
    user_list = []
    gender_list = []
    birth_list = []

    with open(city_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            if time_period == 'none':

                start_time_list.append(row['Start Time'])
                trip_duration_list.append(row['Trip Duration'])
                start_station_list.append(row['Start Station'])
                end_station_list.append(row['End Station'])

                if len(str(row['User Type'])) > 1:
                    user_list.append(row['User Type'])

                if city_file != 'washington.csv':

                    if len(str(row['Gender'])) > 1:
                        gender_list.append(row['Gender'])

                    if len(str(row['Birth Year'])) > 1:
                        birth_list.append(str(row['Birth Year'])
                                          .replace('.0',''))

            elif time_period == 'month':

                if row['Start Time'].startswith('2017-0' + str(month_number)):

                    start_time_list.append(row['Start Time'])
                    trip_duration_list.append(row['Trip Duration'])
                    start_station_list.append(row['Start Station'])
                    end_station_list.append(row['End Station'])

                    if len(str(row['User Type'])) > 1:
                        user_list.append(row['User Type'])

                    if city_file != 'washington.csv':

                        if len(str(row['Gender'])) > 1:
                            gender_list.append(row['Gender'])

                        if len(str(row['Birth Year'])) > 1:
                            birth_list.append(str(row['Birth Year'])
                                              .replace('.0',''))

            elif time_period == 'day':

                if row['Start Time'].startswith('2017-0' + str(month_number)
                   + '-0' + str(day)) or row['Start Time'].startswith('2017-0'
                   + str(month_number) + '-' + str(day)):

                    start_time_list.append(row['Start Time'])
                    trip_duration_list.append(row['Trip Duration'])
                    start_station_list.append(row['Start Station'])
                    end_station_list.append(row['End Station'])

                    if len(str(row['User Type'])) > 1:
                        user_list.append(row['User Type'])

                    if city_file != 'washington.csv':

                        if len(str(row['Gender'])) > 1:
                            gender_list.append(row['Gender'])

                        if len(str(row['Birth Year'])) > 1:
                            birth_list.append(str(row['Birth Year'])
                                      .replace('.0',''))

            elif time_period == 'weekday':
                start_time_list.append(row['Start Time'])
                trip_duration_list.append(row['Trip Duration'])
                start_station_list.append(row['Start Station'])
                end_station_list.append(row['End Station'])
                user_list.append(row['User Type'])
                if city_file != 'washington.csv':
                    gender_list.append(row['Gender'])
                    birth_list.append(str(row['Birth Year']).replace('.0',''))

    trip_list = [str(start_station_list[i])
                 + ' and ending at '
                 + str(end_station_list[i])
                 for i in range(len(start_station_list))]

    if time_period == 'weekday':

        weekday = (datetime.datetime.strptime(str(weekday), '%A')
                   .weekday())

        weekday_list = [str(x).split(' ')[0] for x in start_time_list]
        weekday_list = [datetime.datetime.strptime(x, '%Y-%m-%d').weekday()
                        for x in weekday_list]

        for i in range (len(weekday_list)):
            if weekday_list[i] != int(weekday):
                start_time_list[i] = None
                trip_duration_list[i] = None
                start_station_list[i] = None
                end_station_list[i] = None
                trip_list[i] = None
                user_list[i] = None
                if city_file != 'washington.csv':
                    gender_list[i] = None
                    birth_list[i] = None

    start_time_list = [x for x in start_time_list if x is not None]
    trip_duration_list = [x for x in trip_duration_list if x is not None]
    start_station_list = [x for x in start_station_list if x is not None]
    end_station_list = [x for x in end_station_list if x is not None]
    trip_list = [x for x in trip_list if x is not None]
    user_list = [x for x in user_list if x is not None]
    user_list = [x for x in user_list if len(str(x)) > 3]

    if city_file != 'washington.csv':
        gender_list = [x for x in gender_list if x is not None]
        birth_list = [x for x in birth_list if x is not None]
        gender_list = [x for x in gender_list if len(str(x)) > 2 ]
        birth_list = [x for x in birth_list if len(str(x)) > 2 ]

    return (start_time_list, trip_duration_list, start_station_list,
            end_station_list, trip_list, user_list, gender_list, birth_list)


def popular_month(start_time_list, city_file, time_period):
    '''start_time_list is processed by a dictionary generator that generates a
    key for every month. To answer the question 'What is the most popular month
    for start time?'the max() built-in function is applied to the dictionary.
    Results, are formated and printed (including count of trips and line a
    reminding the city and time period previously selected)

    arguments:
        city_file, time_period, start_time_list
    returns:
        none
    '''

    popular_month_start = {}
    for date in start_time_list:
        if str(date[5:7]) not in popular_month_start:
            popular_month_start[str(date[5:7])] = 1
        else:
            popular_month_start[str(date[5:7])] += 1

    answer_index = max(popular_month_start, key=popular_month_start.get)
    answer_count = popular_month_start[answer_index]

    answer = datetime.datetime.strptime(str(answer_index), '%m').strftime('%B')

    print ('City: '+ city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: '+ time_period
           + '\nDuring the first six months of 2017, the most popular '
           'month for start time was:\n{} ({} trips).'
           .format(answer, answer_count))


def popular_day(start_time_list, city_file, time_period, month):
    '''Formats every element on the argument list as days (0[monday] to 6
    [sunday]) using the datetime library. A dictionary is generated from
    that list, assigning a key for each day. To answer the question
    'What is the most popular day of week (Monday, Tuesday, etc.) for
    start time?'' The max() function is applied to the resulting dictionary.
    Results are printed on the screen.

    arguments:
        start_time_list, city_file, time_period, month
    returns:
        none
    '''
    start_time_list = [str((x).split(' ')[0]) for x in start_time_list]
    start_time_list = [datetime.datetime.strptime(x, '%Y-%m-%d').weekday()
                      for x in start_time_list]

    p_day_st = {}
    for day in start_time_list:
        if day not in p_day_st:
            p_day_st[day] = 1
        else:
            p_day_st[day] += 1

    answer = max(p_day_st, key=p_day_st.get)
    answer_count = p_day_st[answer]
    answer = datetime.datetime.strptime(str(answer), '%d').strftime('%A')

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period
           + ', Month: ' + month.title()
           + '\nThe most popular day for start time was {}.\nWith a total '
           'of {} trips started.'.format(answer, answer_count))


def popular_hour(start_time_list, city_file, time_period, month, day, weekday):
    ''' A dictionary is generated from the list start_time_list,
    assigning a key for each of the 24 hs. in a day. To answer the question
    'What is the most popular hour for start time?', the max() function is
    applied to the resulting dictionary. Results are printed on the screen.

    arguments:
        start_time_list, city_file,
        time_period, month,
        day, month_number,
        weekday
    returns:
        none
    '''

    start_time_list = [str(x).split(' ')[1].split(':')[0]
                       for x in start_time_list]

    pop_start = {}
    for start in start_time_list:
        if start not in pop_start:
            pop_start[start] = 1
        else:
            pop_start[start] += 1

    answer = max(pop_start, key=pop_start.get)
    answer_count = pop_start [answer]

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period + ', Month: ' + month.title()
           + ', Day: ' + str(day)
           + ', Weekday: ' + str(weekday)
           +'.\nThe most popular time for start time '
           'was {}:00 hs.\nWith a total of {} trips started in that hour.'
           .format(answer, answer_count))


def trip_duration(trip_duration_list, city_file,
                  time_period, month,
                  day, weekday):
    '''To answer the question 'What is the total trip duration and average
    trip duration?', the elements in trip_duration_list are added and avarege
    durations is calculated. Finally, total time is calculated in days, hours,
    minutes and seconds. Results are printed on the screen.

    arguments:
        trip_duration_list, city_file, time_period, month, month_number
    returns:
        none
    '''

    trip_duration_list = [ float(x) for x in trip_duration_list ]
    total_duration = sum(trip_duration_list)

    td_seconds = total_duration % 60
    td_minutes = (total_duration // 60) % 60
    td_hours = ((total_duration // 60) // 60) % 24
    td_days = ((total_duration // 60) // 60) // 24

    average_trip = total_duration / len(trip_duration_list)
    at_minutes =  (average_trip // 60)
    at_seconds = average_trip % 60

    print ('City: '
           + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: '+ time_period
           + ', Month: '+ month.title()
           + ', Day: '+ str(day)
           + ', Weekday: ' + str(weekday) + '.\n'
           'Trips started during the selected time period accounted '
           'for a total \nduration of {} days(s), {} hour(s), {} minutes(s) '
           'and {} second(s).\nTheir average duration was {} minutes(s) and '
           '{} second(s).'.format(int(td_days), int(td_hours),
           int(td_minutes), int(td_seconds), int(at_minutes),
           int(at_seconds)))


def popular_stations(start_station_list, end_station_list,
                     city_file, time_period,
                     month, day,
                     weekday):
    ''' two dictionaries are generated one for start_station_list and one for
    end_station_list assigning a key for each station. To answer the question
    'What is the most popular start station and most popular end station?',
    The max() function is applied to each dictionary. Results are printed on
    the screen.

    arguments:
        start_station_list, end_station_list,
        city_file, time_period,
        month, day
    returns:
        none
    '''

    start_station_count = {}
    for sstation in start_station_list:
        if sstation not in start_station_count:
            start_station_count[sstation] = 1
        else:
            start_station_count[sstation] += 1

    end_station_count = {}
    for estation in end_station_list:
        if estation not in end_station_count:
            end_station_count[estation] = 1
        else:
            end_station_count[estation] += 1

    answer1 = max(start_station_count, key=start_station_count.get)
    answer1_count = start_station_count[answer1]
    answer2 = max(end_station_count, key=end_station_count.get)
    answer2_count = end_station_count[answer2]

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period + ', Month: ' + month.title()
           + ', Day: ' + str(day)
           + ', Weekday: ' + str(weekday)
           + '.\nThe most popular start station was {} ({} trips)\n'
           'and the most popular end station was {} ({} trips).'
           .format(answer1, answer1_count, answer2, answer2_count))


def popular_trip(trip_list, city_file, time_period, month, day, weekday):
    '''A dictionary is generated from trip_list, assigning a key for every trip.
    To answer the question 'What is the most popular trip?', the max() function
    is applied to the resulting dictionary. Results are printed on the screen.

    arguments:
        trip_list, city_file, time_period, month, month_number
    returns:
        none
    '''

    popular_trip = {}
    for trip in trip_list:
        if trip not in popular_trip:
            popular_trip[trip] = 1
        else:
            popular_trip[trip] += 1

    answer = (max(popular_trip, key=popular_trip.get))
    answer_count = popular_trip[answer]

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period
           + ', Month: ' + month.title()
           + ', Day: ' + str(day)
           + ', Weekday: ' + str(weekday)
           + '.\nThe most popular trip was starting at {}.\n'
           'With a total of {} trips.'
           .format(answer, answer_count))


def users(user_list, city_file, time_period, month, day, weekday):
    '''A dictionary is generated from user_list assigning a key to each user
    type. To answer the question 'What are the counts of each user type?',
    the max() function is applied to the resulting dictionary.
    Results are printed on the screen.

    arguments:
        user_list, city_file, time_period, month, month_number
    returns:
        none
    '''

    user_type_count = {}
    for u_type in user_list:
        if u_type not in user_type_count:
            user_type_count[u_type] = 1
        else:
            user_type_count[u_type] += 1

    answer1 = max(user_type_count, key=user_type_count.get)
    answer_count1 = user_type_count[answer1]

    answer2 = min(user_type_count, key=user_type_count.get)
    answer_count2 = user_type_count[answer2]

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period
           + ', Month: ' + month.title()
           + ', Day: ' + str(day)
           + ', Weekday: ' + str(weekday)
           + '.\n{}s were the most common user type, making {} trips total.\n'
           'While {}s accounted for {} trips.'
           .format(answer1, answer_count1, answer2.lower(), answer_count2))


def gender(gender_list, city_file, time_period, month, day, weekday):
    '''To answer the question 'What are the counts of gender?', a
    count variable is made for each option, counting ocurrences in gender_list.
    The results are printed on the screen.

    arguments:
        gender_list, city_file, time_period, month, month_number
    returns:
        none
    '''

    malecount = 0
    femalecount = 0

    for x in gender_list:
        if 'Male' in x:
            malecount += 1
        elif 'Female' in x:
            femalecount += 1

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period
           + ', Month: ' + month.title()
           + ', Day: ' + str(day)
           + ', weekday: ' + str(weekday)
           + '.\nMale users completed {} trips.\nFemale users completed '
           '{} trips.'.format(malecount,femalecount))


def birth_years(birth_list, city_file, time_period, month, day, weekday):
    '''A dictionary is generated from birht_list assigning a key to each user
    type. To answer the questions 'What are the earliest, most recent, and most
    popular birth years?', the min() and max() functions are applied to the
    resulting dictionary. Results are printed on the screen.

    arguments:
        city_file, time_period, month, month_number
    returns:
        none
    '''

    popular_birth = {}
    for year in birth_list:
        if year not in popular_birth:
            popular_birth[year] = 1
        else:
            popular_birth[year] += 1

    answer_earliest = min(birth_list)
    answer_most_recent = max(birth_list)
    answer_popular = (max(popular_birth, key=popular_birth.get))
    popular_count = popular_birth[answer_popular]

    print ('City: ' + city_file.replace('.csv','').replace('_',' ').title()
           + ', Time Period: ' + time_period
           + ', Month: ' + month.title()
           + ', Day: '+ str(day)
           + ', Weekday: ' + str(weekday)
           + '.\nEarliest birth year was {}.\nMost recent birth '
           'year was {}.\nThe most common birth year was {}, users born in '
           'that year completed {} trips.'
           .format(answer_earliest, answer_most_recent,
            answer_popular, popular_count))


def display_data(city_file):
    '''If the user inputs 'yes', displays five lines of data for the selected
    city. After displaying five lines, ask the user if they would like to see
    five more, continuing asking until input == 'no'.

    Args:
        city_file
    Returns:
        none.
    '''
    try:
        display = input('Would you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')

        if display.lower() == 'yes':

            city = open(city_file, 'r')
            header = city.readline()
            linecount = 0

            for line in city:
                while linecount < 5:
                    if linecount == 0:
                        print ('\n' + header)
                    print (city.readline())
                    linecount += 1

                    if linecount > 4:
                        try:
                            display = input('Would you like to view '
                                            'individual trip data? '
                                            'Press \'Enter\' to continue '
                                            'or type \'no\' to end. \n')
                            if display.lower() == 'yes':
                                linecount = 0
                                continue
                            elif display.lower() == 'no':
                                break
                            else:
                                linecount = 0
                                continue
                        except KeyboardInterrupt:
                            sys.exit()

                        finally:
                            if not KeyboardInterrupt:
                                break
            city.close()

        elif display.lower() == 'no':
            pass

        else:
            print('Invalid input\n')
            display_data(city_file)

    except KeyboardInterrupt:

        sys.exit()

    finally:
        if not KeyboardInterrupt:
            display_data(city_file)


def statistics():
    '''Calculates and prints out the descriptive statistics about a city
    and time period specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''

    city_file = get_city()
    time_period = get_time_period()
    day = ''
    month = ''
    month_number = ''
    weekday = ''

    if time_period == 'month' or time_period == 'day':
        month = get_month()

    if time_period == 'day':
        day = get_day(month)

    if time_period == 'weekday':
        weekday = get_weekday()

    if time_period == 'month' or time_period == 'day':
        month_number = (str(int(datetime.datetime.strptime(str(month), '%B')
                        .strftime('%m'))))

    print ('')
    print('Extracting data from csv file...')

    start_time = time.time()

    (start_time_list,
    trip_duration_list,
    start_station_list,
    end_station_list,
    trip_list,
    user_list,
    gender_list,
    birth_list) = data_compiler(city_file,
                                time_period,
                                month,
                                month_number,
                                day,
                                weekday)

    print ('')
    print("That took %s seconds." % (time.time() - start_time))

    if time_period == 'none':
        print ('')
        print('Calculating the first statistic...')
        print ('')

        start_time = time.time()

        popular_month(start_time_list, city_file, time_period)

        print ('')
        print("That took %s seconds." % (time.time() - start_time))
        print ('')
        print("Calculating the next statistic...")
        print ('')

    elif time_period == 'month':
        print ('')
        print('Calculating the first statistic...')
        print ('')

    start_time = time.time()

    if time_period == 'none' or time_period == 'month':
        popular_day(start_time_list, city_file, time_period, month)

        print ('')
        print("That took %s seconds." % (time.time() - start_time))
        print ('')
        print("Calculating the next statistic...")
        print ('')

    else:
        print ('')
        print('Calculating the first statistic...')
        print ('')

    start_time = time.time()

    popular_hour(start_time_list, city_file, time_period, month, day, weekday)

    print ('')
    print("That took %s seconds." % (time.time() - start_time))
    print ('')
    print("Calculating the next statistic...")
    print ('')

    start_time = time.time()

    trip_duration(trip_duration_list, city_file,
                  time_period, month,
                  day, weekday)

    print ('')
    print("That took %s seconds." % (time.time() - start_time))
    print ('')
    print("Calculating the next statistic...")
    print ('')

    start_time = time.time()

    popular_stations(start_station_list,
                     end_station_list,
                     city_file,
                     time_period,
                     month,
                     day,
                     weekday)

    print ('')
    print("That took %s seconds." % (time.time() - start_time))
    print ('')
    print("Calculating the next statistic...")
    print ('')

    start_time = time.time()

    popular_trip(trip_list, city_file, time_period, month, day, weekday)

    print ('')
    print("That took %s seconds." % (time.time() - start_time))
    print ('')
    print("Calculating the next statistic...")
    print ('')

    start_time = time.time()

    users(user_list, city_file, time_period, month, day, weekday)

    print ('')
    print("That took %s seconds." % (time.time() - start_time))
    if city_file != 'washington.csv':
        print ('')
        print("Calculating the next statistic...")
        print ('')
        start_time = time.time()
        gender(gender_list, city_file, time_period, month, day, weekday)

        print ('')
        print("That took %s seconds." % (time.time() - start_time))
        print ('')
        print("Calculating the next statistic...")
        print ('')
        start_time = time.time()
        birth_years(birth_list, city_file, time_period, month, day, weekday)

        print ('')
        print("That took %s seconds." % (time.time() - start_time))
        print ('')

    display_data(city_file)

    while True:
        try:
            restart = input('\nWould you like to restart? '
                            'Type \'yes\' or \'no\'. \n')

            if restart.lower() == 'yes':
                statistics()
                break
            elif restart.lower() == 'no':
                print('\nThank you for reviewing this project!\n')
                break
            else:
                print ('Couldn\'t understand that.')
        finally:
            pass


if __name__ == "__main__":
	statistics()
