-- fhgnyrfs dfgthn
-- dthyj jed 
CREATE database if not exists hbtn_0d_usa;
USE hbtn_0d_usa
CREATE table if not exists hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id int not null,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) not null);
