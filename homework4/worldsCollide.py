import sqlite3
import mariadb
mconn = mariadb.connect(user="umwstud",
    password="davies4ever",
    host="stephendavies.org", port=3306, database="galactic")

mcur = mconn.cursor()

sconn = sqlite3.connect("rcloughl_airline.sqlite")
scur = sconn.cursor()

mcur.execute("select * from capacities")
stock = mcur.fetchall()
try:
    idcount=0
    for x in stock:
        make=x[0]
        model=x[1]
        capacity=x[2]
        scur.execute("insert into plane (make, model, AID) values (?,?,?)",(make,model,idcount))
        idcount=idcount+1
        scur.execute("insert into stock (make, model, capacity) values (?,?,?)",(make,model,capacity))
        sconn.commit()
except:
    print("stock already added")

mcur.execute("select * from flightplans")
flight = mcur.fetchall()
try:
    for x in flight: 
        airline=x[0]
        flightNum=x[1]
        departTime=x[3]
        arriveTime=x[4]
        departPort=x[5]
        arrivePort=x[6]
        scur.execute("insert into flight (airline, flightNum,departTime,departPort,arriveTime,arrivePort) values (?,?,?,?,?,?)",(airline,flightNum,departTime,departPort,arriveTime,arrivePort))
        sconn.commit()
except:
    print("flights already added")

mcur.execute("select * from trips")
trips= mcur.fetchall()
try:
    for x in trips:
        day = x[0]
        airline=x[1]
        flightNum=x[2]
        pilot=x[3]
        copilot=x[4]
        make=x[5]
        model=x[6]
        arriveGate=x[8]
        departGate=x[7]
        AIDTup=scur.execute("select AID from plane where make=? and model=?",(make,model))
        AID=AIDTup[0][0]
        scur.execute("insert into specificFlight (day,airline,flightNum,AID,departGate,arriveGate,pilot,copilot) values (?,?,?,?,?,?,?,?)",(day,airline,flightNum,AID,departGate,arriveGate,pilot,copilot))
        sconn.commit()
        try:
            scur.execute("insert into employee (empID) values (?)",(pilot))
        except:
            print("Already added")
        sconn.commit()
        try:
            scur.execute("insert into employee (empID) values (?)",(copilot))
        except:
            print("Already added")
        sconn.commit()
        try:
            scur.execute("insert into canOperate (employee,make,model) values (?,?,?)",(pilot,make,model))
        except:
            print("Already added")
        sconn.commit()
        try:
             scur.execute("insert into canOperate (employee,make,model) values (?,?,?)",(copilot,make,model))
        except:  
            print("Already added")
        sconn.commit()
except:
    print("trips already added")

try:
    scur.execute("update specificFlight set copilot=null where AID=(select AID from plane,stock where plane.make=stock.make and plane.model=stock.model and capacity=1)")
    sconn.commit()
except:
    print("One Seaters ammended")


mcur.execute("select flight_date,spaceline,flightnum,type,count(type) from sales group by flight_date, spaceline, flightnum,type")
sales= mcur.fetchall()
for x in sales:
    day=x[0]
    airline=x[1]
    flightNum=x[2]
    trans=x[3]
    num=x[4]
    if (trans=='purchase'):
        scur.execute("update specificFlight set ticketsSold=? where day=? and airline=? and flightNum=?",(num,day,airline,flightNum))
        sconn.commit()
    if(trans=='refund'):
        scur.execute("update specificFlight set ticketsSold=(ticketsSold-?) where day=? and airline=? and flightNum=?",(num,day,airline,flightNum))
        sconn.commit()


mcur.execute("select * from flightplans")
flight = mcur.fetchall()
try:
    for x in flight:
        airline=x[0]
        flightNum=x[1]
        departTime=x[3]
        arriveTime=x[4]
        departPort=x[5]
        arrivePort=x[6]
        scur.execute("update specificFlight set departGate=?,arriveGate=? where airline=? and flightNum=?",(departPort,arrivePort,airline,flightNum))
        sconn.commit()
except:
    print('done')

