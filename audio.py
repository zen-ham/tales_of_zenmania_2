import random
import threading, kthread
import math
import simpleaudio
from pydub import AudioSegment


class SoundEngine:
    def __init__(self):
        self.handles = []
        self.cached_audios = {}
    
    def change_speed(self, sound, speed=1.0):
        new_frame_rate = int(sound.frame_rate * speed)
        new_sound = sound._spawn(sound.raw_data, overrides={"frame_rate": new_frame_rate})
        # Resample back to the original frame rate for compatibility with simpleaudio
        return new_sound.set_frame_rate(sound.frame_rate)
    
    class SoundHandle:
        def __init__(self, thread, stop_event):
            self.thread = thread
            self.stop_event = stop_event
        
        def stop(self):
            self.stop_event.set()
            self.thread.kill()
            self.thread.join()
    
    def play(self, file_path, volume=1.0, speed=1, loop=False):
        if type(speed) == tuple:
            speed = random.uniform(speed[0], speed[1])

        if file_path not in self.cached_audios:
            sound = AudioSegment.from_file(file_path)
            self.cached_audios[file_path] = sound
        else:
            sound = self.cached_audios[file_path]
        
        # Adjust volume: pydub uses decibels.
        # To convert a multiplier to dB change, use: gain = 20 * log10(volume)
        if volume <= 0:
            gain = -120
        else:
            gain = 20 * math.log10(volume)
        sound = sound.apply_gain(gain)
        
        if speed != 1.0:
            sound = self.change_speed(sound, speed)
        
        raw_data = sound.raw_data
        num_channels = sound.channels
        bytes_per_sample = sound.sample_width
        sample_rate = sound.frame_rate
        
        stop_event = threading.Event()
        
        def play_sound():
            try:
                while not stop_event.is_set():
                    play_obj = simpleaudio.play_buffer(raw_data, num_channels, bytes_per_sample, sample_rate)
                    play_obj.wait_done()
                    if not loop:
                        break
            except:
                play_obj.stop()
        
        # Start playback in a separate thread so it's nonblocking.
        thread = kthread.KThread(target=play_sound, daemon=True)
        thread.start()
        
        handle = self.SoundHandle(thread, stop_event)
        self.handles.append(handle)
        return handle

sound_engine = SoundEngine()