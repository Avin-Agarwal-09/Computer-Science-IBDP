import time
def countdown_time(seconds):
    while seconds > 0:
        print("time left:",seconds)
        time.sleep(1)
        seconds = seconds - 1
    print("Time is ove")
duration = int(input("Enter a duration: "))
countdown_time(duration)