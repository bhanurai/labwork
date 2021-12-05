# you live 4 miles from university,the bus drivers at 25mph but spends 2 minutes at each of the 10 stops on the way.how long
# will journey take ? alternatively, you could run to university ,you jog the first mile at 7 mph; then run the next two at
# 15mph :before jogging the last 7mph again :will this be quicker or slower than the bus ?


distance = 4
speed1 = 25
stop_T = 10*2
time = 1/speed1
time2 = time*60
total_time =time2+stop_T
print =(f"the total time to reach university by bus{total_time}")
speed2=7
time1=1/speed2
time_1=time1*60
speed3=15
time2=2/speed3
time_2=time2*60
speed4=7
time3=1/speed4
time_3=time3*60
total_time2=time_1+time_2+time_3
print(f"the total time foe walking is {total_time2}")
print(f"walking is faster to reach university")