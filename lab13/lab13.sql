.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
    FROM students AS a, students AS b
    WHERE a.pet = b.pet AND a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT a.seven
  FROM students AS a, numbers AS b
  WHERE a.time = b.time AND a.number = 7 AND b.'7' = "True";


CREATE TABLE avg_difference AS
  SELECT round(avg(abs(smallest - number)))
  FROM students;

