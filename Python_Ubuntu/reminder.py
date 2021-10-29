import time
from pygame import mixer

while True:
	time.sleep(120)
		
	print('Drink 200ml water!!')
	mixer.init()
	mixer.music.load('/home/vishal/Desktop/Learning_Python/Python_Ubuntu/music/Water.mp3')
	mixer.music.play(-1)

	while True:
		query = input("Press 'Done' to stop the music!!\n").lower()
		if query == 'done':			
			mixer.music.stop()
			break

	time.sleep(300)
		
	print('Massage your eyes!!')
	mixer.init()
	mixer.music.load('/home/vishal/Desktop/Learning_Python/Python_Ubuntu/music/close_eyes.mp3')
	mixer.music.play(-1)

	while True:
		query = input("Write 'Done' to stop the music!!\n").lower()
		if query == 'done':			
			mixer.music.stop()
			break

	time.sleep(600)
		
	print('Do Some Physical Activity!!')
	mixer.init()
	mixer.music.load('/home/vishal/Desktop/Learning_Python/Python_Ubuntu/music/Workout.mp3')
	mixer.music.play(-1)


	while True:
		query = input("Press 'Done' to stop the music!!\n").lower()
		if query == 'done':			
			mixer.music.stop()
			break





