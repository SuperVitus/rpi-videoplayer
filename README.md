## Setup ##
`python3 setup.py install`

## Usage ##

| Option | Default | Description |
| --- | --- | --- |
| switch_type | 0 | Switch type - 0 for normally-open, 1 for normally-closed |
| gpio_pin | 26 | GPIO pin used for switch |
| video_a | | filepath relative to project root |
| video_b | | filepath relative to project root |
| video_c | | filepath relative to project root |
| video_d | | filepath relative to project root |
| timer_b_delay | 30 | seconds, designed to play **video b** if coffin is not opened back up within 30 seconds of being closed |
| timer_c_delay | 5 | seconds, a bit of buffer time between (**video a** completed OR opening the coffin the second time) and the start of **video c** |
| timer_complete_delay | 60 | seconds, the amount of time the coffin lid must be closed for the state to reset to the beginning |

## State Machine ##
* Videos
  * **a:** Hello there 
  * **b:** No need to be afraid
  * **c:** Main content 
  * * This should have a tail portion of the video that continues after the main content with instructions to close the coffin + any additional instructions to continue hunt
  * **d:** You know what you need to do
  * * see video c note - we can probably tail this video with the same content
  
### Timers ###
* **Timer b:**
* **Timer c:**
* **Timer complete:**

### Events ###
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
| State | initializing_closed | intializing_open | ready_closed | playing_a | introduced_closed | introduced_open | playing_b | playing_c | playing_d | played_open | played_closed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **intializing_closed** | | *lid_open* | *intitialized_closed* | | | | | | | | | | 
| **intializing_open** | *lid_close* | | | *intitialized_open* | | | | | | | | | 
| **ready_closed** | | | | *lid_open* | | | | | | | | |
| **playing_a** | | | | | *lid_close* | *video_completed* | | | | | | 
| **introduced_closed** | | | | | | *lid_open* | *timer\_b\_resolved* | | | | | 
| **introduced_open** | | | | | *lid_close* | | | *timer\_c\_resolved* | | | | 
| **playing_b** | | | | | *lid_close* | *lid_open* | | | | | | 
| **playing_c** | | | | | *lid_close* | | | | | *video_completed* | | 
| **playing_d** | | | | | | | | |  | *video_completed* | *lid_close* |
| **played_open** | | | | | | | | | | | *lid_close* |
| **played_closed** | *timer\_complete\_resolved*| | | | | | | | *lid_open* | | |

note: italicized values in the table are the events capaple of triggering a state change for each row



