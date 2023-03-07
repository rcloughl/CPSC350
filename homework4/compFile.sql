pragma foreign_keys  = off;

DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS specificFlight;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS runways;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS flightports;
DROP TABLE IF EXISTS plane;
DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS crew;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS canOperate;


pragma foreign_keys =  on;

CREATE TABLE flight(
	airline text,
	flightNum integer,
	departTime text,
	departPort text,
	arriveTime text,
	arrivePort text,
	make text,
	model integer,
	primary key (airline, flightNum)
);

CREATE TABLE specificFlight(
        day text,
	airline text,
        flightNum integer,
	AID text,
        cancelled integer,
        ticketsSold integer,
        departGate text,
        arriveGate text,
	pilot text,
	copilot text,
	primary key (day, airline, flightNum),
        foreign key (airline, flightNum) 
		references flight (airline, flightNum)
);


create table reservation(
	day text,
	startRes text,
	endRes text,
	airport text,
	primary key (startRes, endRes)
);

create table runways(
	bearing text,
	gate text,
	runwayLength real,
	instLanding int,
	airport text,
	primary key (airport, gate)
);

create table airport(
	abbreviation text,
	name text,
	city text,
	state text,
	primary key (abbreviation)
);

create table flightPorts(
	port text,
	airline text,
	flightNum integer,
	primary key (port, airline, flightNum),
	foreign key (port)
		references airport (abbreviation),
	foreign key (airline, flightNum)
		references flight (airline, flightNum)
);

create table plane(
	AID text,
	fuel real,
	totalMiles real,
	make text,
	model integer,
	year integer,
	location text,
	primary key (AID)
);

create table stock(
	make text,
	model integer,
	description text,
	capacity integer,
	fuelCap real,
	maxAlt double,
	landingLength double,
	primary key (make, model)
);

create table crew(
	crewID text,
	name text
);

create table employee(
	empId text,
	primary key (empId)
);

create table canOperate(
	employee text,
	make text,
	model integer,
	primary key (employee, make, model),
	foreign key (make, model)
		references stock (make, model)
);

insert into stock (make, model, description, capacity, maxAlt, landingLength) values
	('Boeing', 737, 'mid-sized', 189, 41000, 4500),
	('Airbus', 320, 'revolutionary', 150, 39000, 4500),
	('Boeing', 747, 'jumbo', 542, 48000, 6000),
	('Cessna', 414,'small, twin-engine', 8, 30800, 2000)	
;

insert into employee (empId) values
	('Bob'),
	('Suzie'),
	('Stan'),
	('Ken'),
	('Phyllis')
;

insert into canOperate (employee, make, model) values
	('Bob', 'Boeing', 747),
	('Bob', 'Airbus', 320),
	('Suzie', 'Boeing', 737),
	('Suzie', 'Boeing', 747),
	('Suzie', 'Cessna', 414),
	('Stan', 'Boeing', 737),
	('Phyllis', 'Boeing', 737),
	('Phyllis', 'Boeing', 747),
	('Phyllis', 'Airbus', 320)
;

insert into airport (abbreviation, name) values
	('DCA', 'Reagan National'),
	('DEN', 'Denver International Airport'),
	('CLE', 'Cleveland-Hopkins International Airport'),
	('FLL', 'Ft. Lauderdale Airport')
;

insert into runways (airport, bearing, instLanding, runwayLength) values
	('DCA', 'N', 1, 6869),
	('DCA', 'SE', 0, 5204),
	('DCA', 'NE', 0, 4911),
	('DEN', 'E', 1, 12000),
	('DEN', 'NEE', 1, 12000),
	('DEN', 'SE', 1, 12000),
	('DEN', 'S', 1, 12000),
	('DEN', 'SEE', 1, 12000),
	('DEN', 'SSE', 1, 16000),
	('CLE', 'NE', 1, 9000),
	('CLE', 'NEE', 1, 8999),
	('CLE', 'NNE', 0, 7096),
	('CLE', 'SEE', 0, 6017),
	('FLL', 'SEE', 1, 9000),
	('FLL', 'SE', 0, 6930),
	('FLL', 'E', 0, 5280)	
;

insert into plane (AID, make, model, year, fuel, totalMiles, location) values
	('#1111', 'Airbus', 320, 2009, 6850, 92000, 'DEN'),
	('#1112', 'Airbus', 320, 2009, 6850, 86000, 'DEN'),
	('#2345', 'Boeing', 737, 2006, 38, 486000, 'CLE'),
	('#5566', 'Boeing', 737, 1999, 5000, 1000000, 'AIRBORN'),
	('#52982', 'Cessna', 141, 2022, null, null, null)
;

insert into flight (airline, flightNum, departTime, departPort, arriveTime, arrivePort, make, model) values
	('American Airlines', 1865, '5:30 am', 'DCA', '10:54 am', 'DEN', 'Airbus', 320),
	('AirBlue', 101, '1:00 pm', 'DCA', '1:30 pm', 'RMN', 'Cessna', 414),
	('American', 4501, '3:15 pm', 'DCA', '4:45', 'CLE', 'Boeing', 737),
	('United', 735, '12:00 pm', 'CLE', '4:34', 'FLL', 'Boeing', 737)
;

insert into crew (crewID, name) values
	('#1', 'Suzie'),
	('#1', 'Stan'),
	('#2', 'Suzie')
;

insert into specificFlight (day, airline, flightNum, AID, pilot, copilot, ticketsSold) values
	('2021-09-08', 'United', 735, '#5566', 'Suzie','Stan', 132),
	('2021-09-17', 'AirBlue', 101, '#52982', 'Suzie', null, 1)
;

insert into runways (airport, gate) values 
	('CLE', 'C-09')
;
;
;
