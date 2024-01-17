-- ggtbr trhf 
-- edfrtg eerg
SELECT id, name from cities
where state_id =(
	SELECT id from states
	where name = "California");
