import time

def countdown_timer(seconds):
    print(f"Time remaining: {seconds} seconds")
    time.sleep(seconds)
    seconds -= 1

    print("Times up")

duration = 10
countdown_timer(duration)