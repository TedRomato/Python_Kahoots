import play

text = play.new_text(x = 0, y = 0, words = '0')

def addScore():
    global score
    score = score + 1
    text.words = str(score)


@play.repeat_forever
def game_loop():
    if play.key_is_pressed('w'):
        addScore()


play.start_program()


