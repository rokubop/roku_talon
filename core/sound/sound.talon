# volume up:                  user.volume_up()
# volume down:                user.volume_down()
# volume mute:                key(mute)

# ^playback {user.playback_device}:
#     user.notify("Playback: {playback_device}")
#     user.change_sound_device(playback_device)

# ^microphone {user.microhpone_device}:
#     user.notify("Microphone: {microhpone_device}")
#     user.change_sound_device(microhpone_device)

# ^use {user.playback_microphone_pair}:
#     user.change_sound_device_pair(playback_microphone_pair)

voice [meter] switch:
    user.switcher_focus('vb audio')
    mouse_move(1765, 487)
    mouse_click()

# os: windows
# and app.name: VB-AUDIO Virtual Audio Device Mixing Console Application
# os: windows
# and app.exe: voicemeeter.exe
