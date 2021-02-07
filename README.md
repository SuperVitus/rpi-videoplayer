## Setup ##
`python3 setup.py install`

## State Machine ##
* Videos
  * **a:** Hello there 
  * **b:** No need to be afraid
  * **c:** Main content 
  * * This should have a tail portion of the video that continues after the main content with instructions to close the coffin + any additional instructions to continue hunt
  * **d:** You know what you need to do
  * * see video c note - we can probably tail this video with the same content
  
## Timers ##
* **Timer b:** 30 seconds, designed to play **video b** if coffin is not opened back up within 30 seconds of being closed 
* **Timer c:** 5 seconds, a bit of buffer time between (**video a** completed OR opening the coffin the second time) and the start of **video c**
* **Timer complete:** 1-2 minutes, the amount of time the coffin lid must be closed for the state to reset to the beginning

## Events ##
* `play video x`
* `video completed`
* `set timer x`
* `timer x resolved`
* `lid opened/closed`

### State ###
| State | On Enter | On Exit | Notes |
| --- | --- | --- | --- |
| **intializing_closed** | |
| **intializing_open** | 
| **ready_closed** | | | 
| **playing_a** | `play video a` | |
| **introduced_closed** | `set timer b` | `cancel timer b` |
| **introduced_open** | `set timer c` | `cancel timer c` |
| **playing_b** | `play video b` `cancel timer b` | 
| **playing_c** | `play video c` `cancel timer c` | `set timer complete` |
| **playing_d** | `play video d` | 
| **played_open** | `play video d` | 
| **played_closed** | | |

 ### Transitions ###
| | initializing_closed | intializing_open | ready_closed | playing_a | introduced_closed | introduced_open | playing_b | playing_c | playing_d | played_open | played_closed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **intializing_closed** | | *lid_opened* | *intitialized_closed* | | | | | | | | | | 
| **intializing_open** | *lid_closed* | | | *intitialized_open* | | | | | | | | | 
| **ready_closed** | | | | *lid_opened* | | | | | | | | |
| **playing_a** | | | | | *lid_closed* | *video_completed* | | | | | | 
| **introduced_closed** | | | | | | *lid_opened* | *timer\_b\_resolved* | | | | | 
| **introduced_open** | | | | | *lid_closed* | | | *timer\_c\_resolved* | | | | 
| **playing_b** | | | | | *lid_closed* | *lid_open* | | | | | | 
| **playing_c** | | | | | *lid_closed* | | | | | *video_completed* | | 
| **playing_d** | | | | | | | | |  | *video_completed* | *lid_close* |
| **played_open** | | | | | | | | | | | *lid_close* |
| **played_closed** | *timer\_complete\_resolved*| | | | | | | | *lid_opened* | | |

note: italicized values in the table are the events capaple of triggering a state change for each row



