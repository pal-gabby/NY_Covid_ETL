# NY_Covid_ETL
Extracting the data for each county in New York state from the API, and load them into individual tables in the database. Each county table should contain following columns : Test Date, New Positives, Cumulative Number of Positives, Total Number of Tests Performed, Cumulative Number of Tests Performed, Load date.\
**For Creating Cron job:**\
Some useful commands
  1. crontab -e : for asetting up cron job.
  2. crontab -l : listing cron jobs.
  3. sudo service cron start.
  4. service cron status.\
***Below cron job will run the python file daily at 9 am***\  
<> Edit this file to introduce tasks to be run by cron.\
<>\
<> Each task to run has to be defined through a single line\
<> indicating with different fields when the task will be run\
<> and what command to run for the task\
<>\
<> To define the time you can provide concrete values for\
<> minute (m), hour (h), day of month (dom), month (mon),\
<> and day of week (dow) or use '*' in these fields (for 'any').\
<> Notice that tasks will be started based on the cron's system\
<> daemon's notion of time and timezones.\
<>\
<> Output of the crontab jobs (including errors) is sent through\
<> email to the user the crontab file belongs to (unless redirected).\
<>\
<> For example, you can run a backup of all your user accounts\
<> at 5 a.m every week with:\
<> 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/\
<>\
<> For more information see the manual pages of crontab(5) and cron(8)\
<>\
<> m h  dom mon dow   command\
***Below command will help us run the script everyday***\
 00 9 * * * /usr/bin/python3 /mnt/c/Users/pallavi/Desktop/take_home/take_home.py >> /mnt/c/Users/pallavi/Desktop/take_home/take_home_asses.log
