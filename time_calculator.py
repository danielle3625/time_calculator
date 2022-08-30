
def add_time(start, duration, day=False):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]

    weekdays_dic = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}

  
    # break out all the relevent info
    # get start time, conver to int, get start meridiem
    start_time = start.split()[0]
    start_hr = int(start_time.split(':')[0])
    start_min = int(start_time.split(':')[1])
    start_meridiem = start.split()[1]


    # get duration hrs/min, convert to int
    time_lapse = duration.split(':')
    lapse_hr = int(time_lapse[0])
    lapse_min = int(time_lapse[1])

    # set up variables for to return at the end
    end_hr = ''
    end_min = ''
    end_day = ''
    end_meridiem = ''
    

    # ensure minutes displayed is not over 60
    # convert to hours
    # determine minute value to display, formatted
    if lapse_min + start_min > 60:
        lapse_hr += 1
        time_adj = 60 - start_min
        end_min = lapse_min - time_adj
    else:
        end_min = start_min + lapse_min

    if end_min < 10:
      end_min = f'0{end_min}'
    
    # determine hour to display
    end_hr = (start_hr + lapse_hr) % 12
    if end_hr == 0:
      end_hr = 12

    # determine number of 12 hour periods, to get AM or PM
    periods_passed = (start_hr + lapse_hr) // 12


    if start_meridiem == 'AM':
      alt_meridiem = 'PM'
    else: 
      alt_meridiem = 'AM'

    if periods_passed % 2 == 0:
      end_meridiem = start_meridiem
    else:
      end_meridiem = alt_meridiem

    
    # account for days passed, 
    days_passed = lapse_hr // 24

    # account for duration going passed midnight
    if end_meridiem == 'AM' and start_hr + (lapse_hr % 12) >= 12:
      days_passed += 1

    ret_value = str(end_hr) + ':'+ str(end_min) + ' ' + str(end_meridiem)

    if day:
      day = day.lower()
      index = int(weekdays_dic[day] + days_passed) % 7
      end_day = weekdays[index]
      ret_value += ', ' + end_day

    if days_passed == 1:
      ret_value += ' (next day)'
    elif days_passed > 1:
      ret_value += ' (' + str(days_passed) + ' days later)'

    return ret_value

    

    
     
    
    
      

   



    