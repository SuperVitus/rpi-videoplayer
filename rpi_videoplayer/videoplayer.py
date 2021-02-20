#!/usr/bin/python

# Raspberry Pi GPIO-controlled video player
# Copyright (c) 2021 Devin Despain
# All rights reserved
import subprocess
import sys
# import dbus
from transitions import Machine, State
from threading import Timer
from pynput import keyboard
from time import sleep

from vlc import MediaPlayer, Media, Instance

video_a_media = Media("media/hello_there.mp3") 
video_a_duration = 5
video_b_media = Media("media/no_need.mp3") 
video_b_duration = 15
video_c_media = Media("media/main_content.mp3") 
video_c_duration = 5
video_d_media = Media("media/you_know.mp3") 
video_d_duration = 5

timer_b_delay = 3
timer_c_delay = 5
timer_d_delay = 10
timer_complete_delay = 15

# video_a 'Hello there'
# video_b 'No need to be afraid'
# video_c 'Main content'
# video_d 'You know what you need to do'


vlc_instance = Instance()
player = vlc_instance.media_player_new()
media = Media("media/sample.mp4") 
player.set_media(media) 
# player.set_fullscreen(True) 
# player.play() 


states=[
    State(name='initializing_closed'),
    State(name='initializing_open'),
    State(name='ready_closed'),
    State(name='playing_a', on_enter=['play_video_a']),
    State(name='introduced_closed', on_enter=['set_timer_b'], on_exit=['cancel_timer_b']),
    State(name='introduced_open', on_enter=['set_timer_c'], on_exit=['cancel_timer_c']),
    State(name='playing_b', on_enter=['play_video_b']),
    State(name='playing_c', on_enter=['play_video_c','cancel_timer_c'], on_exit=['set_timer_d']),
    State(name='playing_d'),
    State(name='played_closed'),
    State(name='played_open'),
    State(name='completed')
]

transitions = [
    # [name, source, destination],

    # From initializing_closed
    ['lid_open', 'initializing_closed', 'intializing_open'],
    ['initialized', 'initializing_closed', 'ready_closed'],

    # From initializing_open
    ['lid_close', 'initializing_open', 'intializing_closed'],
    ['intitialized', 'initializing_open', 'playing_a'],

    # From ready_closed
    ['lid_open', 'ready_closed', 'playing_a'],

    # From playing_a
    ['lid_close', 'playing_a', 'introduced_closed'],
    ['video_completed', 'playing_a', 'introduced_open'],

    # From introduced_closed
    ['lid_open', 'introduced_closed', 'introduced_open'],
    ['timer_b_resolved	', 'introduced_closed', 'playing_b'],

    # From introduced_open
    ['lid_close	', 'introduced_open', 'introduced_closed'],
    ['timer_c_resolved	', 'introduced_open', 'playing_c'],

    # From playing_b
    ['lid_close	', 'introduced_b', 'introduced_closed'],
    ['lid_open', 'introduced_b', 'introduced_open'],

    # From playing_c
    ['lid_close	', 'introduced_c', 'introduced_closed'],
    ['video_completed', 'introduced_c', 'played_open'],

    # From playing_d
    ['video_completed', 'introduced_d', 'played_open'],
    ['lid_close', 'introduced_d', 'played_closed'],

    # From played_open
    ['lid_close', 'played_open', 'played_closed'],

    # From played_closed
    ['timer_complete_resolved', 'played_closed', 'initializing_closed'],
    ['lid_open', 'played_closed', 'playing_d'],
]

class VideoPlayer:

    is_lid_open = None
    # video_a_has_played = False
    # video_b_has_played = False
    # video_c_has_played = False
    # video_d_has_played = False
    video_timer_current = None
    video_timer_b = None
    video_timer_c = None

    # def test(self): print("test!!")

    def play_video_a(self): 
        print("play video a")
        player.set_media(video_a_media) 
        self.video_timer_current = Timer(video_a_duration, self._video_completed)
        self.video_timer_current.start()
        player.play()
    
    def play_video_b(self): 
        print("trigger video b")
        player.set_media(video_b_media) 
        self.video_timer_current = Timer(video_b_duration, self._video_completed)
        self.video_timer_current.start()
        player.play()
    
    def play_video_c(self): 
        print("trigger video c")
        player.set_media(video_c_media)
        self.video_timer_current = Timer(video_c_duration, self._video_completed)
        self.video_timer_current.start()
        player.play()
    
    def play_video_d(self): 
        print("trigger video d")
        player.set_media(video_d_media)
        self.video_timer_current = Timer(video_d_duration, self._video_completed)
        self.video_timer_current.start()
        player.play()

    def set_timer_b(self): 
        print("timer b set for {} seconds".format(timer_b_delay))
        self.video_timer_b = Timer(timer_b_delay, self.play_video_b)
        self.video_timer_b.start()

    def cancel_timer_b(self): 
        print("cancel video b timer")
        self.video_timer_b.stop()

    def set_timer_c(self): 
        print("timer c set for {} seconds".format(timer_c_delay))
        self.video_timer_c = Timer(timer_c_delay, self.play_video_c)
        self.video_timer_c.start()

    def cancel_timer_d(self): 
        print("cancel video timer d")
        self.video_timer_c.stop()

    def set_timer_d(self): 
        print("timer d set for {} seconds".format(timer_d_delay))
        self.video_timer_d = Timer(timer_c_delay, self.play_video_d)
        self.video_timer_d.start()

    def cancel_timer_c(self): 
        print("cancel video timer c")
        self.video_timer_c.stop()

    def stop_video(self): 
        print("stop video")
        player.stop_video()
        self.video_timer_current.stop()

    def _video_completed(self):
        print("video completed")
        self.video_completed()

    def _lid_open(self):
        if(self.is_lid_open == False or self.is_lid_open == None):
            self.is_lid_open = True
            print("lid opened")
            self.lid_open()

    def _lid_close(self):
        if(self.is_lid_open == True or self.is_lid_open == None):
            self.is_lid_open = False
            print("lid closed")
            self.lid_close()
        
    # video_timer_b = Timer(1, stop_video, ())

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
    print("state: {}".format(model.state))
    model.initialized()
    print("state: {}".format(model.state))


def on_press(key):
    try:
        if key.char == 'o':
            model._lid_open()
            print(model.state)
        elif key.char == 'c':
            model._lid_close()
            print(model.state)
    except AttributeError:
        pass


if __name__ == '__main__':
    listener = keyboard.Listener(
        on_press=on_press)
    listener.start()
    main()
    while 1 == 1 :
        try:
            sleep(.1)
        except KeyboardInterrupt:
            sys.exit(1)


