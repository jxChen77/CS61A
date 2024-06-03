.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = 'blue' AND pet = 'dog' ;

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(*) = 1;   


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b where a.pet = b.pet and a.song = b.song and a.time<b.time;


CREATE TABLE sevens AS
  SELECT students.seven from students inner join numbers on students.time=numbers.time where students.number=7 and numbers.'7' = 'True';


CREATE TABLE average_prices AS
  SELECT category, round(sum(msrp) / count(*)) from products group by category;  


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory group by item;


CREATE TABLE shopping_list AS
  SELECT  products.name, lowest_prices.store 
  from products join lowest_prices on products.name=lowest_prices.item
  group by products.category having min(products.MSRP/products.rating);

CREATE TABLE total_bandwidth AS
  SELECT sum(stores.Mbs) from shopping_list join stores on stores.store=shopping_list.store; 
