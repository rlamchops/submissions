from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<a href=yourfortune><h1>Click here to get your daily fortune!</h1></a>"

@app.route("/yourfortune")
def yourfortune():
    n = random.randrange(1,21)
    t = random.randrange(1,4)
    if t == 1:
        t = "days"
    elif t == 2:
        t = "months"
    else:
        t = "years"
    w = random.randrange(1,21)
    if w == 1:
        w = "teacher"
    elif w == 2:
        w = "best friend"
    elif w == 3:
        w = "true love"
    elif w == 4:
        w = "crush"
    elif w == 5:
        w = "mother"
    elif w == 6:
        w = "father"
    elif w == 7:
        w = "uncle"
    elif w == 8:
        w = "aunt"
    elif w == 9:
        w = "cousin"
    elif w == 10:
        w = "sister"
    elif w == 11:
        w = "brother"
    elif w == 12:
        w = "friend"
    elif w == 13:
        w = "dog"
    elif w == 14:
        w = "cat"
    elif w == 15:
        w = "chinchilla"
    elif w == 16:
        w = "duck billed platypus"
    elif w == 17:
        w = "grandmother"
    elif w == 18:
        w = "grandfather"
    elif w == 19:
        w = "teddy bear"
    else:
        w = "nemesis"
    v = random.randrange(1,21)
    if v == 1:
        v = "die."
    elif v == 2:
        v = "go missing."
    elif v == 3:
        v = "turn up in Cambodia."
    elif v == 4:
        v = "send you a love letter."
    elif v == 5:
        v = "cause you great pain."
    elif v == 6:
        v = "cause you great happiness."
    elif v == 7:
        v = "deliver the best news of your life."
    elif v == 8:
        v = "change your life forever."
    elif v == 9:
        v = "give you a spectacular gift."
    elif v == 10:
        v = "kiss you passionately."
    elif v == 11:
        v = "break your heart."
    elif v == 12:
        v = "get in a car crash."
    elif v == 13:
        v = "give you a black eye."
    elif v == 14:
        v = "make you cry."
    elif v == 15:
        v = "steal your heart."
    elif v == 16:
        v = "win the lottery."
    elif v == 17:
        v = "win one million dollars on Wheel of Fortune."
    elif v == 18:
        v = "get stranded on an uninhabited island."
    elif v == 19:
        v = "kill you."
    else:
        v = "spontaneously combust."
    fortune = "In " + str(n) + " " + t + ", your " + w + " will " + v + "<p><a href=yourfortune>Click here to get ANOTHER fortune!</a></p>"
    return fortune

if __name__ == "__main__":
    app.debug = True
    app.run()

