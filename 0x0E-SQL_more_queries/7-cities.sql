-- fhgnyrfs dfgthn
-- dthyj jed 
CREATE database if not exists hbtn_0d_usa;
USE hbtn_0d_usa
CREATE table if not exists cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id int not null FOREIGN KEY REFERENCES states(id),
	name VARCHAR(256) not null);
