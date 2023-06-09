# App running instruction

## Runing with docker-compose

1.  Copy .flaskenv to working space main directory
2.  Run `docker-compose build` in CMD
3.  Next `docker-compose up` or `docker-compose up -d` to run in deamon mode.
4.  App should be listening on http://127.0.0.1:5005/


## Connection with dbase

# Each time a user starts a session, they are required to pass username information. After the user submits the data, SocketIO captures this information and saves it to the ElephantSQL database (Psql), and into the flask-session. 

# There are three tables in the database. The first table is called "user" and it contains information such as username, points, lives, and a connection to the "statistics" table. The second table, "statistics" captures all the relevant information regarding wins, losses, and draws. Lastly, there is a table to store Flask session data.
