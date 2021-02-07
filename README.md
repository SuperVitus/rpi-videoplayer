### Setup ###
`python3 setup.py install`

### State Machine ###
* Videos
  * **a:** Hello there 
  * **b:** No need to be afraid
  * **c:** Main content
  * **d:** You know what you need to do

| State | On Enter | On Exit | Notes |
| --- | --- | --- | --- |
| **intializing_closed** | |
| **intializing_open** | 
| **ready_closed** | | | 
| **playing_a** | `play video a` | |
| **introduced_closed** | `set timer b` | `cancel timer b` |
| **introduced_open** | `set timer c` | `cancel timer c` |
| **playing_b** | `play video b` | 
| **playing_c** | `play video c` | `set timer d` |
| **playing_d** | `play video d` | 
| **played_open** | `play video d` | 
| **played_closed** | `cancel timer d` | |

 
| | initializing_closed | intializing_open | ready_closed | playing_a | introduced_closed | introduced_open | playing_b | playing_c | playing_d | played_open | played_closed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **intializing_closed** | | *lid_open* | *intitialized_closed* | | | | | | | | | | 
| **intializing_open** | *lid_closed* | | | *intitialized_open* | | | | | | | | | 
| **ready_closed** | | | | *lid_open* | | | | | | | | |
| **playing_a** | | | | | *lid_closed* | *video_complete* | | | | | | 
| **introduced_closed** | | | | | | *lid_open* | *timer\_b\_resolved* | | | | | 
| **introduced_open** | | | | | *lid_closed* | | | *timer\_c\_resolved* | | | | 
| **playing_b** | | | | | *lid_closed* | *lid_open* | | | | | | 
| **playing_c** | | | | | *lid_closed* | | | | | *video_complete* | | 
| **playing_d** | | | | | | | | |  | *video_complete* | *lid_close* |
| **played_open** | | | | | | | | | | | *lid_close* |
| **played_closed** | *timer\_complete\_resolved*| | | | | | | | *lid_open* | | |



