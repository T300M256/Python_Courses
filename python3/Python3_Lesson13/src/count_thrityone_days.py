from datetime import datetime, timedelta
now = datetime.now()
delta = timedelta(31)
delivery = now + delta
print("Today: %s" % now.strftime("%d"))
print("Delivery: %s" % delivery.strftime("%d"))

#date = now.strftime("%d")
#delivery = int(date) + 31
#print("Today: %s" % date)
#print("Delivery:  %s" % delivery)