CREATE DATABASE
	swimDB;


GRANT ALL ON
    swimDB.*
TO
    'swimuser'@'localhost'
IDENTIFIED BY
    'swimpasswd';


-- Prompt for password
mysql -u swimuser -p swimDB
