import serial
import time
import random

print 'Hello'
print 'My name is plant...'

id = '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_64933303732351D0D0C0-if00'
ser = serial.Serial(id,9600)

def enum(** enums):
	return type('Enum', (), enums)

State = enum(happy=1,thirsty=2)

state = State.happy

sad = ["I'm so thirsty! Please help!",
	"Why have you forsaken me!?!",
	"I'm dying and nobody cares.",
	"It's fine. I'll just go get myself a glass of water. Oh wait...",
	"Everything hurts and I'm dying.",
	"Oh don't worry about me. I'm just dying of thirst",
	"I think this is what pain feels like.",
	"I NEED MY FIX MAN!",
	"Help! I just lost a leaf!",
	"Dehydration isn't good for my skin.",
	"Remember what happened to those last plants you didn't water? THEY DIED",
	"I was happier at Lowes",
	"Remember what happened to those last plants you didn't water? THEY DIED",
	"I was happier at Lowes.",
	"Water. GIVE IT TO ME!!"]

happy = ["I'M ALIIIVE!",
	"Mmmm... Water.",
	"What is that? Water? I drink that stuff like water.",
	"THIS STUFF IS THE BEST! WHAT IS THAT? Water? Oh yeah.",
	"Water. So good.",
	"I F'ING LOVE WATER!",
	"I don't have eyes, so I don't know who watered me, but thanks! I needed that",
	"Oh yeah. Give it to me",
	"Time to photosynthesize!",
	"UGH, YUM!"]

bored = ["Bored of being bored because being bored is boring.",
	"I wish my pot had wheels",
	"Someone pass me the remote.",
	"The plant accross from me has some pretty sweet lookin flowers. What should I say?",
	"I need to be real honest here... I can't tell if I'm a guy or a girl.",
	"I CAN'T FEEL MY LEGS! Wait. I don't have legs. Yet...",
	"Hey! Little Shop of Horrors! I love that movie!",	
	"A common human mating ritual involves killing plants and displaying their reproductive organs. I hate humans.",
	"Why is ok for people to stick their nose in my genitalia and sniff it real good?",
	"The research assistant couldn't experiment with plants because he hadn't botany.",
	"Making fun of a tree is a knock on wood",
	"What kind of tree grows in your hand? A palm tree! Boom!",
	"On organic farms, they till it like it is.",
	"What's a tree's favorite drink? Root beer!",
	"Why couldn't the flower ride the bike? Because it's petals fell off!",
	"What did one flower say to the other? Move over bud!",
	"What's brown and sticky? A stick!",
	"Why do potatoes make good detectives? They keep their eyes peeled.",
	"My owner's fake plants died because they forgot to pretend to water them.",
	"You can lead a horticulture, but you can't make her think",
	"DUUUUUDE. This pot is great.",
	"How do trees use the internet? They LOG in!"
]
people = ['@aaronmyster','@kayleagood']


def getMoisture():
	str = ser.readline()
	moist = [int(s) for s in str.split() if s.isdigit()]
	return moist[0]

while True:
	moist = getMoisture()

	if (state == State.happy):
		if (moist < 680):
			state = State.thirsty
			print random.choice(people) + ' ' + random.choice(sad)
		else:
			print random.choice(bored)

	if (state == State.thirsty):
		if (moist > 680):
			state = State.happy
			print random.choice(happy)


	time.sleep(1)

		
