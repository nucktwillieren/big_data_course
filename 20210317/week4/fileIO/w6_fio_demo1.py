

fn1 = 'map_areacodes_states.txt' #define the path to the file
#open the file as read mode
fid1 = open(fn1, 'r')
data1 = fid1.readlines()
fid1.close() #close the file object

fn11 = 'test.txt'
fid11 = open(fn11, 'w')
fid11.writelines(data1)
fid11.close()

#write selective contents
fn12 = 'test2.txt'
fid12 = open(fn12, 'w')
for s in data1[::2]:
    fid12.write(s)
fid12.close()

fn13 = 'test3.txt'
fid13 = open(fn13, 'w')
for s in data1[1::2]:
    for t in s[::2]:
        fid13.write(t)
fid13.close()



#alternatively, using with so that fid1 is automatically closed
fn14 = 'test4.txt' #define the path to the file
#open the file as read mode
with open(fn14, 'w') as fid14:
    fid14.writelines(data1)


#The above is equivalent to the following
fid14 = open(fn14, 'w')
try:
    #fid14.writelines(data1)
    for s in data1:
        fid14.write(s)
finally:
    fid14.close()
