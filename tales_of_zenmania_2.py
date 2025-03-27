import sys, time, os
import traceback
import ctypes

def show_error_box(exc_type, exc_value, exc_traceback):
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    ctypes.windll.user32.MessageBoxW(0, error_msg, "Application Error", 0x10)

sys.excepthook = show_error_box


def maximize_console():
    kernel32 = ctypes.WinDLL("kernel32")
    user32 = ctypes.WinDLL("user32")
    
    hwnd = kernel32.GetConsoleWindow()
    if hwnd:
        user32.ShowWindow(hwnd, 3)  # 3 = SW_MAXIMIZE


if sys.platform == "win32":
    maximize_console()

from colorama import Fore, Style, init

init(convert=True, autoreset=True)

def high_precision_sleep(duration):  # I ripped this function straight from my package zhmiscellany, I just didn't want to import it to only use a single thing
    start_time = time.perf_counter()
    while True:
        elapsed_time = time.perf_counter() - start_time
        remaining_time = duration - elapsed_time
        if remaining_time <= 0:
            break
        if remaining_time > 0.02:  # Sleep for 5ms if remaining time is greater
            time.sleep(max(remaining_time/2, 0.0001))  # Sleep for the remaining time or minimum sleep interval
        else:
            pass

def resource_path(relative_path):
    return relative_path
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

def typewriter_print(text, color=Fore.WHITE, delay=0.05, sound=True, timed_sound=False):
    if sound and not dev:
        typeing_sound = sound_engine.play(resource_path('sfx/keyboard-typing-5997.mp3'), speed=(1.9, 2.1))
    
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        if not dev:
            if timed_sound:
                sound_engine.play(resource_path('sfx/typing-sound-02-229861.mp3'), speed=(1, 1.1))
            high_precision_sleep(delay)
    print(Style.RESET_ALL)
    if sound and not dev:
        typeing_sound.stop()

def slow_input(prompt, color=Fore.CYAN):
    typewriter_print(prompt, color)
    return input()

dev = False

from plot import game, title, descriptions
from audio import SoundEngine
sound_engine = SoundEngine()

sound_engine.play(resource_path('sfx/retro-audio-logo-94648.mp3'))
typewriter_print(title, Fore.MAGENTA, delay=0.002, sound=False)
typewriter_print(f"A Dystopian Coding Rebellion", Fore.YELLOW)
print()
print(f"{Fore.LIGHTBLACK_EX}At any time you can submit '?' as input and see descriptions of any recent key words. This game is somewhat educational if you want it to be.{Style.RESET_ALL}")
print()
music = sound_engine.play(resource_path('sfx/retro-streets-28824.mp3'), volume=0.15, speed=0.8, loop=True)

def decide(choices, links, sequence_number):
    choices = [c.lower() for c in choices]
    inp = -1
    
    i=0
    while inp not in choices:
        if i and inp != '?':
            print(f'{Fore.LIGHTBLACK_EX}Choose either {", ".join(choices)}.')
        inp = input().lower()
        i=1
        
        if inp == '?':
            sound_engine.play(resource_path('sfx/Ceeday _Huh__ Sound Effect.mp3'), volume=0.5, speed=(0.5, 2))
            if sequence_number in descriptions:
                print(f'{Fore.LIGHTBLACK_EX}{descriptions[sequence_number]}{Style.RESET_ALL}')
            else:
                print(f'{Fore.LIGHTBLACK_EX}Sorry, no information available for this section. Try googling it.{Style.RESET_ALL}')
    
    return links[choices.index(inp)]

endings_file = 'endings.txt'
if not os.path.exists(endings_file):
    with open(endings_file, 'w') as f:
        f.write('')

def load_endings():
    with open(endings_file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    data = [int(i) for i in data if i]
    return data

def save_ending(ending_number):
    if ending_number not in load_endings():
        with open(endings_file, 'a') as f:
            f.write(f'{ending_number}\n')

endings = 0
for event in game:
    if len(event) > 5:
        if type(event[5]) == tuple:
            endings += 1
event = game[0]
choice_events = []
backtracks = []
while True:
    typewriter_print(event[1], event[2])
    if (not event[3]) and event[4]:
        for each in game:
            if each[0] == event[4][0]:
                event = each
                break
        else:
            raise Exception('Special link error')
        typewriter_print('...', Fore.YELLOW, delay=1, sound=False, timed_sound=True)
        continue
    if event[3]:
        choice_events.append(event)
        choice = decide(event[3], event[4], event[0])
        sound_engine.play(resource_path('sfx/retro-select-236670.mp3'), volume=0.3, speed=(0.9, 1.1))  # button select sound
        for each in game:
            if each[0] == choice:
                event = each
                break
        else:
            raise Exception("Out of bounds error. Somehow you got somewhere you weren't supposed to be. The game will now close.")
    else:
        sq = event[0]
        try:
            new_event = game[game.index(event)+1]
        except IndexError:
            new_event = (-1,) # set to a sequence number that doesn't exist to force the system to detect it as an ending
        if new_event[0] == event[0]:
            event = new_event
        else:
            save_ending(event[5][0])
            print(f'{Fore.LIGHTBLACK_EX}You reached ending {event[5][0]}/{endings}, the {event[5][1]}. You\'ve found {len(load_endings())}/{endings} total endings. (P)lay again, (C)ontinue from last (unexplored) choice, or (E)xit?')
            choice = decide(('p', 'c', 'e'), (1, 2, 3), sq)
            match choice:
                case 1:
                    event = game[0]
                case 2:
                    for prev_choice_event in choice_events.__reversed__():
                        if prev_choice_event in backtracks:
                            continue
                        backtracks.append(prev_choice_event)
                        event = prev_choice_event
                        break
                    else:
                        break
                case 3:
                    break