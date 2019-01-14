from gpiozero import LED, Button
import spotipy, spotipy.util
from signal import pause

# Credentials
client_id = "..."
client_secret = "..."
username = "..."

# Button inputs
previous_track = Button(21)
play = Button(20)
next_track = Button(16)
shuffle = Button(12)
repeat = Button(25)
favorite = Button(24)

# LED outputs
playing = LED(26)
shuffling = LED(19)
repeating = LED(13)


def login_to_spotify():
	print("Logging in to Spotify...")

	token = spotipy.util.prompt_for_user_token(
		username = username,
		scope = "user-modify-playback-state,user-read-playback-state,user-read-currently-playing",
		redirect_uri = "http://localhost/",
		client_id = client_id,
		client_secret = client_secret
	)

	spotify = spotipy.Spotify(auth = token)

	user = spotify.current_user()
	print("Logged in as " + user["id"])

	return spotify


def refresh_leds():
	currentPlayback = spotify.current_playback()

	if currentPlayback["is_playing"]:
		playing.on()
	else:
		playing.off()

	if currentPlayback["shuffle_state"]:
		shuffling.on()
	else:
		shuffling.off()

	if currentPlayback["repeat_state"] == "off":
		repeating.off()
	else:
		repeating.on()


def toggle_shuffle():
	if shuffling.is_lit:
		spotify.shuffle(False)
	else:
		spotify.shuffle(True)

	refresh_leds()


def toggle_repeat():
	if repeating.is_lit:
		spotify.repeat("off")
	else:
		spotify.repeat("context")

	refresh_leds()


def toggle_play():
	if playing.is_lit:
		spotify.pause_playback()
	else:
		spotify.start_playback()

	refresh_leds()


def play_favorite():
	print("This is your task")


# Main program starts here

# Login to spotify
spotify = login_to_spotify()

# Refresh states of LEDs
refresh_leds()

# Define actions for buttons
play.when_pressed = toggle_play
next_track.when_pressed = spotify.next_track
previous_track.when_pressed = spotify.previous_track

shuffle.when_pressed = toggle_shuffle
repeat.when_pressed = toggle_repeat

favorite.when_pressed = play_favorite

print("Waiting for input...")
pause()
