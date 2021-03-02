-- list cities in data base 
SELECT id, name FROM cities  WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
