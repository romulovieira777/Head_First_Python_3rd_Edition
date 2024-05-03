CREATE TABLE times (
            swimmer_id INTEGER NOT NULL,  
            event_id INTEGER NOT NULL,
            time VARCHAR(16) NOT NULL,
            ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );


CREATE TABLE swimmers (
        id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(32) NOT NULL,
        age INTEGER NOT NULL
    );


CREATE TABLE events (
            id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            distance VARCHAR(16) NOT NULL,
            stroke VARCHAR(16) NOT NULL
        );
