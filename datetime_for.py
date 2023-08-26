import datetime

current_time = datetime.datetime.now()
interval = datetime.timedelta(hours=6)


for x in range(0, 6):
    scheduled_time = current_time + interval * x #https://mas.to/@tshirtman/110955411938353285
    print(f"Current Time: {current_time}, Scheduled Time : {scheduled_time}")

