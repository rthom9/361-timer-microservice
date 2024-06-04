# Timer Microservice

---

## Description
The timer microservice was implemented for CS 361 Software Engineering I class. The microservice allows users to submit
a total countdown time, an initial alert time, and a second alert time. This microservice allows users to pause and 
restart the timer. The microservice returns alerts to users at both specified alert times and once the timer is complete. 
This microservice utilizes text files for users to make and receive requests.

### Communication Contract

---

####How to request data from this microservice

To request data from the timer microservice, the timer.py file will first need to placed within the same directory as 
the user's main program.  The 
functions set_timer, start_timer, pause_timer, cancel_timer and monitor_timer can be imported and used as needed.
The text files, "time.txt", "alerts.txt" and "controller.txt" will be created upon setting and starting timer.
```python
# This example completes a countdown of 5s.
# Time must be entered in HHMMSS format.
set_timer("000050")
start_timer()
monitor_timer()
```

```python
# This example completes a countdown of 10s with alerts at 5s and 3s.
set_timer("000010", "000005", "000003")
start_timer()
monitor_timer("000005", "000003")
```

```python
# pause_timer will pause the timer countdown.
# In this example, the timer is paused at 8s for 2s duration and then resumed.
# Note: time.sleep is simply used for demonstration purposes.
set_timer("000010", "000005", "000003")
start_timer()
monitor_timer("000005", "000003")
time.sleep(2)
pause_timer()
time.sleep(2)
start_timer()
```

```python
# This example completes a countdown of 20s. With the timer being cancelled at 15s.
# This corresponds to an example case of a user submitting a timed form entry after 5s. 
set_timer("000020")
start_timer()
time.sleep(5)
cancel_timer()
```

###How to receive data from the microservice
Data is received through the alerts.txt file. When the timer reaches the specified alert times and subsequently 0s, the 
respective time(s) will be written in the alerts.tx file. Monitor_timer() can be used to await changes in alert.txt file. 
Presently, monitor_timer() will create window box alerts. 

Example:
```python
set_timer("00000010","000005","000003")
start_timer()
monitor_timer("000010","000005","000003"
```
In this case,```000005```, ```000003```, and ```0s``` will be written/over-written to alerts.txt at those respective times 
with window alerts to notify user.

Example:
```python
set_timer("00000010")
monitor_timer()
```

In this case, ```0s``` will be written to alerts.txt when countdown is complete with window alert to notify user..

####UML Sequence Diagram

![UML Diagram](UML%20Diagram.png)

