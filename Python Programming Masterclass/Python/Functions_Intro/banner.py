def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("The Text is too long to fit in the spefied width")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)

banner_text("*")
banner_text("I know that I've imagined love before")
banner_text("And how it could be with you")
banner_text("Really hurt me, baby, really cut me, baby")
banner_text("How can you have a day without a night?")
banner_text("You're the book that I have opened")
banner_text("And now I've got to know much more")
banner_text("The curiousness of your potential kiss")
banner_text(" ")
banner_text("Has got my mind and body aching")
banner_text("Really hurt me, baby, really cut me, baby")
banner_text("How can you have a day without a night?")
banner_text("You're the book that I have opened")
banner_text("And now I've got to know much more")
banner_text("Like a soul without a mind")
banner_text("In a body without a heart")
banner_text("I'm missing every part, hey")
banner_text("*")