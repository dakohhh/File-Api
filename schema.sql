CREATE TABLE users( user_id VARCHAR(7) PRIMARY KEY, 
                   full_name VARCHAR(100) NOT NULL, 
                   email VARCHAR(100) UNIQUE,
                   password VARCHAR(100) NOT NULL, 
                   verified BOOLEAN DEFAULT FALSE,
                   verification_id VARCHAR(100) UNIQUE NOT NULL,
                   date_created TIMESTAMP DEFAULT NOW());

                   



CREATE TABLE files (file_id VARCHAR(100) PRIMARY KEY, 
                    file_name VARCHAR(100) NOT NULL, 
                    user_id VARCHAR(100) NOT NULL, 
                    date_added TIMESTAMP DEFAULT NOW());





