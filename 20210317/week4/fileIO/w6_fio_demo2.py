fn2 = 'TrainStationFlow_2005-2017.csv' #define the path to the file
#open the file as read mode, using with to ensure that it will be closed after access
with open(fn2, 'r', encoding='utf-8') as fid2:
    data2 = fid2.readlines() # read all lines into the data list


data3 = [] #set up an empty list for saving the splitted strings
for d in data2: #loop through the text list
    data3.append(d.rstrip().split(','))


#inquire information
station = '台東'
datestr = '201501'
passenger_N = 0
dc = 0
for d in data3:
    if (datestr in d[0]) and (station in d[2]):
    #if station in d[2]:
        print(d)
        passenger_N += (int(d[3]) + int(d[4])) #number of passengers in/out
        dc += 1 #number of dates having records

print("""\nThere were totally %d passengers visiting %s
during %s, which is %.1f each day.
""" % (passenger_N, station, datestr, passenger_N/float(dc)))
