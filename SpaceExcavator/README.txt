README.TXT INFO									                                       -----------------------------
CPSC 386 CSUF PROJECT #5: VIDEO GAME
CONTACT: RECHEVERRIA04@CSU.FULLERTON.EDU
CWID: 891720195
AUTHOR: RICHARD ECHEVERRIA
This program was built to create a video game space shooter when you shoot down asteroids in order to excavate power stars. According to legend you need to collect 7 power stars to make your wildest dreams come true. Power Stars reside within asteroids, but sometimes they can contain hibernating aliens who will attack when awoken during slumber. Play now, and realize your dreams come to reality. 
FILES INCLUDED								            ------------------------
SpaceExcavator.py
SpaceExcavatorSummary.pdf											           
IMAGES FOLDER:
Samus.png										                     Rock.png	        		                                                                                          Explosionpurple.png							                                                      Space.jpg   										 Menuscreen.jpg										 victorypage.jpg										 sonicexplosion(00,01,02,03,04,05,06,07,and 08).png	 regularexplosion(00,02,03,04,05,06,07,08, and 09).png		          meteorbrown_tiny1.png							    meteorbrown_small1.png								 meteorbrown_small2.png								 meteorbrown_med1.png								 meteorbrown_big1.png								 meteorbrown_big2.png							   	 meteorbrown_big3.png					                                   laserred16.png									              alien.png											 star.png										           boost.png											
SOUNDS FOLDER:
Menu.wav      									                                Gameplay.wav							                                                                Gameover.wav										                        Select.wav									                                       Crash.wav											                    pew.wav											       pow4.wav										          expl3.wav											                               expl6.wav											  pow5.wav											 starget.wav										         victory.wav
FONT FOLDER:
Space_invaders.ttf

RUNNING THE GAME:
This program was created in the Gedit text editor and under the Python 2.7.12 language
After downloading all the files into the same directory, make sure each is in the same path/folder that holds all the sub folders inside. 
Open up the terminal and use these two commands to play the game:
1.) cd SpaceExcavator
2.) python SpaceExcavator.py
FEATURES and BUGS:
The program has active buttons that use that can select. Includes a quit option, controls page, and start game button. The program features music, images, and sounds borrowed from other video games such as Star Fox and Metroid. All rights to these sounds, images, and music belong to Nintendo, and their distributors. The program also features a score keeper to keep track of the points scored by destroying the asteroids. Depending on the size of the asteroid you will get more points the larger the asteroid. If you reach 1500 points, you gain the ability to make your lasers travel at double the speed. If you reach 3000 points you gain the ability to shoot at a faster rate. The program utilizes a random brain by calculating a random positon for which the asteroid will appear in. There is no pattern to which the asteroids will appear or drop from. I implemented a random generator to calculate a random position on the screen the asteroid will appear in. An animation is played when you destroy an asteroid, or when you crash into an alien, or rock. Sounds play when you shoot, destroy an asteroid, and collect a power star.
One thing that is not a bug but is important in working the game is the directory of the files used. If you want to use the images and sounds please change the directories according to your appropriate username. For example:
All the files used in code are implemented like this “/home/username/SpaceExcavator/Images/samus.png”
Please replace ‘username’ with the username on your computer to have full access to the files.



CONTRIBUTES AND REFERENCES:
All images and sounds belong to Nintendo, and I hold no ownership of any of these images or sounds.
The making of this program was helped largely to learning pygame and looking up tutorials online on how to use pygame.
Some third party materials that helped me understand pygame and implanting functions are:
Stackoverflow.com
Nerdparadise.com
Pygame.org
https://www.youtube.com/user/sentdex - Great tutorials on pygame for beginners 
https://www.youtube.com/user/KidsCanCode  
http://www.starfox-online.net/Media/sfx-sf64/
http://www.soundboard.com/sb/Star_Fox_64
https://www.spriters-resource.com/

