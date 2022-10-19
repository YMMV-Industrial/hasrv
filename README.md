# Home Automation Server

This project is intended to run on a Raspberry PI using a commodity RF tranmitter to replace a keyfob or remote control to deliver RC Switch instructions via a simple web application rather than a command line. Minor code modifications from this sample could have you up and running in minutes.

If you get stuck and internet  research isn't helping contact public.projectsupport@ymmvindustrial.com,
while there is no SLA we'll try to help out.  Also check out the comments in blog postings you may find 
on the company website.


## Installation steps:

1. Create dedicated user with sudo privs,  download repository contents to a directory owned by the new user

2. Use the Python package manager to install python requirements
sudo pip3 install -r requirements.txt

3. Create SQLlite database in /var/tmp or wherever your user would normally have privileges.  
( App is hardcoded to use a specific database name /var/tmp but you can adjust both the location 
and the database file name in the file __ init __ .py ). 

Edit database load script to reflect the IO associated with your environment then create and load the database using the commands below:

```
sqlite3 /var/tmp/hasrv_io_state.sqlite3  < hasrv_io_state.sql  ( SQL load script included in repo)
sqlite3 /var/tmp/hasrv_io_state.sqlite3  < hasrv_io_data

#Connect to database & confirm content
sqlite3 /var/tmp/hasrv_io_state.sqlite3
sqlite> select * from iostate;
```

4. Setting the correct RF codes is most important for success, your app may be broadcasting but if the RC switch codes, protocol or pulse length are wrong it wont work.  Try the RF monitor script in our main GIT repo to identify your valid code information.

Once you think you have the change codes identifed modify the txlist assignments in the gettxcodedata function of the applogic.py program


```
def gettxcodedata(iotarget):
    txlist=[]
    if iotarget == 0:
        txlist=[12345,100,12]
    elif iotarget == 1:
        txlist=[67890,200,6]
    elif iotarget == 2:
        txlist=[234765,300,3]
    else:
        txlist=[987654,400,1]
    return txlist
```


## Start flask server as sudo user

Note, you need to be one directory above hasrv directory or what ever you have named the application. Export the two flask variables as shown below, (note capitalization), and start up the application.  By default flask only listens on the local host interface, if you want to control devices from a remote web browser start the application using the -h 0.0.0.0  argument. You can also change the default port using the -p argument but be if you are running over WiFi be certain your network is secure, (warning below), YMMV can not be held responsible for any physical damage that may occur to devices maliciously powered on or off. 

** Warning, this application has no authentication and all HTTP transmissions are clear text **

```
export FLASK_APP=hasrv  
export FLASK_ENV=development  
flask run -p 8080 -h 0.0.0.0
```