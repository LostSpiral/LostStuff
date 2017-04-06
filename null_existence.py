#!/usr/bin/env python


def live(i):
    while falling_down:
        i+=1
        print ("Desire to kill myself "+str(i))

if __name__ == "__main__":
    falling_down = True
    live(0)
