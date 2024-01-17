-- drtfgh
-- sr6th ed
CREATE database if not exists hbtn_0d_usa;
USE hbtn_0d_usa
CREATE table if not exists hbtn_0d_usa.states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name varchar(256) not null);
