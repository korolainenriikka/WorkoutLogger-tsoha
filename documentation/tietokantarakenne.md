# Tietokantarakenne

## Tietokantakaavio

<img src="https://github.com/korolainenriikka/WorkoutLogger-tsoha/blob/master/documentation/kuvat/dbdiagram.png" />

## SQL-skeema

```
CREATE TABLE usergroup (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password_hash VARCHAR(144), 
	PRIMARY KEY (id), 
	UNIQUE (username)
);

CREATE TABLE workout (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS "UserUsergroup" (
	user_id INTEGER NOT NULL, 
	usergroup_id INTEGER NOT NULL, 
	PRIMARY KEY (user_id, usergroup_id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(usergroup_id) REFERENCES usergroup (id)
);

CREATE TABLE session (
	id INTEGER NOT NULL, 
	date DATE NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE result (
	id INTEGER NOT NULL, 
	session_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(session_id) REFERENCES session (id)
);

CREATE TABLE conditioning (
	id INTEGER NOT NULL, 
	distance INTEGER NOT NULL, 
	time TIME NOT NULL, 
	workout_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES result (id), 
	FOREIGN KEY(workout_id) REFERENCES session (id)
);

CREATE TABLE strength (
	id INTEGER NOT NULL, 
	reps INTEGER NOT NULL, 
	weight INTEGER NOT NULL, 
	workout_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES result (id), 
	FOREIGN KEY(workout_id) REFERENCES workout (id)
);
```
