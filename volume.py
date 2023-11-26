import pygame
import tkinter.ttk as ttk

global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file='images/volume0.png')
vol1 = PhotoImage(file='images/volume1.png')
vol2 = PhotoImage(file='images/volume2.png')
vol3 = PhotoImage(file='images/volume3.png')
vol4 = PhotoImage(file='images/volume4.png')

def slide(x):
	#slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
	song = song_box.get(ACTIVE)
	song = f'C:/gui/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())
	
	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)

	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)	
		
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)