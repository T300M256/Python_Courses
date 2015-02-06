"""
Verifies that every animal in the database
easts at least one food.
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

# get list of animal
cursor.execute("""SELECT id, name FROM animal""")
animal = dict(cursor.fetchall())
#print("animal: "+str(animal))
#for a in cursor.fetchall():
remaining = animal.copy()
for anid, name in animal.items():
    try:
        cursor.execute("""SELECT COUNT(*) FROM food WHERE anid=%s""",(anid,))
    except:
        print("Problem executing: "+cursor.statement)
    c = cursor.fetchone()
    if c[0] > 0:
        print(name+" ("+str(anid)+") has a food")
        remaining.pop(anid)
    else:
        print(name+" does not have a food")
        
if len(remaining) > 0:
    print("The following are animals do not have a food entry: "+str(remaining))
else:
    print("Good to go...everyone has food.")
