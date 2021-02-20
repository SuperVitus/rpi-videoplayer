#!/usr/bin/python

# Raspberry Pi GPIO-controlled video player
# Copyright (c) 2021 Devin Despain
# All rights reserved
from transitions import Machine, State

# video_a 'Hello there'
# video_b 'No need to be afraid'
# video_c 'Main content'
# video_d 'You know what you need to do'

states=[
    State(name='initializing_closed'),
    State(name='initializing_open'),
    State(name='ready_closed'),
    State(name='playing_a', on_enter=['play_video_a']),
    State(name='introduced_closed', on_enter=['set_timer_b'], on_exit=['cancel_timer_b']),
    State(name='introduced_open', on_enter=['set_timer_c'], on_exit=['cancel_timer_c']),
    State(name='playing_b', on_enter=['play_video_b']),
    State(name='playing_c', on_enter=['play_video_c','cancel_timer_c']),
    State(name='playing_d'),
    State(name='played_closed'),
    State(name='played_open'),
    State(name='completed')
]

transitions = [
    # [name, source, destination],

    # initialization transitions
    ['initialized', 'initializing_closed', 'ready_closed' ],
    ['initialized', 'initializing_open', 'playing_a' ],

    ['lid_open', 'intializing-closed', 'intializing-open' ],
    ['lid_open', 'introduced-closed', 'intializing-open' ],



    ['lid_closed', 'intializing-open', 'intializing-closed' ],

    ['video_complete', 'playing_a', 'introduced_open' ],
    ['lid_closed', 'playing_a', 'introduced_closed' ],

    ['video_complete', 'playingb', 'completed' ]
]

class VideoPlayer:
    def play_video_a(self): print("trigger video a")
    
    def play_video_b(self): print("trigger video b")
    def set_video_timer_b(self): print("play video b in thirty seconds")
    def cancel_video_timer_b(self): print("cancel video b timer")
    
    def play_video_c(self): print("trigger video c")
    
    def play_video_d(self): print("trigger video d")
    def set_video_timer_d(self): print("play video d in thirty seconds")
    def cancel_video_timer_d(self): print("cancel video d timer")

    def stop_video(self): print("stop video")
    pass

model = VideoPlayer()

def main():
    machine = Machine(
        model=model, 
        states=states, 
        initial='initializing_closed', 
        transitions=transitions, 
        ignore_invalid_triggers=True
    )
    print(model.state)
    model.initialized()
    model.play()
    print(model.state)
    model.video_complete()
    print(model.state)
    model.play()
    print(model.state)
    model.video_complete()
    print(model.state)

if __name__ == '__main__':
    main()