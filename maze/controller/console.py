"""Test saisie clavier."""

while True:  # making a loop
    try:  # if user pressed other than the given key error will not be shown
        if keyboard.is_pressed("q"):  # if key 'q' is pressed
            print("You Pressed a key !")
            break  # finishing the loop
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break
