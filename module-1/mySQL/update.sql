# THE UPDATE STATEMENT IS DIFFERENT FROM WHAT WAS ASKED BECAUSE MY DATABASE DESIGN IS A BIT DIFFERENT.
UPDATE stores SET city = 'Amsterdam' WHERE store_id = 2;

# UPDATING EMAILS OF CUSTOMERS
UPDATE customers set email = 'noemail@noprovider.com' where customer_id = 2;
UPDATE customers set email = 'email@emailprovider.com' where customer_id = 4;
UPDATE customers set email = 'that@email.com' where customer_id = 3;