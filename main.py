import asyncio
import random
import time
import numpy as np
import cv2

computer_deck = ["ONE-SPADES", "TWO-SPADES", "THREE-SPADES", "FOUR-SPADES", "FIVE-SPADES", "SIX-SPADES", "SEVEN-SPADES",
                 "EIGHT-SPADES", "NINE-SPADES", "TEN-SPADES", "QUEEN-SPADES", "KING-SPADES", "ONE-CLUBS", "TWO-CLUBS",
                 "THREE-CLUBS", "FOUR-CLUBS", "FIVE-CLUBS", "SIX-CLUBS", "SEVEN-CLUBS", "EIGHT-CLUBS", "NINE-CLUBS",
                 "TEN-CLUBS", "QUEEN-CLUBS", "KING-CLUBS"]
random.shuffle(computer_deck)

user_deck = ["ONE-DIAMONDS", "TWO-DIAMONDS", "THREE-DIAMONDS", "FOUR-DIAMONDS", "FIVE-DIAMONDS", "SIX-DIAMONDS",
             "SEVEN-DIAMONDS", "EIGHT-DIAMONDS", "NINE-DIAMONDS", "TEN-DIAMONDS", "QUEEN-DIAMONDS", "KING-DIAMONDS",
             "ONE-HEARTS", "TWO-HEARTS", "THREE-HEARTS", "FOUR-HEARTS", "FIVE-HEARTS", "SIX-HEARTS", "SEVEN-HEARTS",
             "EIGHT-HEARTS", "NINE-HEARTS", "TEN-HEARTS", "QUEEN-HEARTS", "KING-HEARTS"]

values = {
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "TEN": 10,
    "QUEEN": 10,
    "KING": 10,
}

computer_value = 0
user_value = 0


def computerTurn():
    global computer_value
    # Get the first value from the random computer deck and split it into an array.
    computer_card = computer_deck[0]
    computer_card = computer_card.split("-")
    # Get the value of the card from a dict and add to the value of computer
    computer_card_value = values.get(computer_card[0])
    computer_value += computer_card_value

    # Remove card from deck
    del computer_deck[0]

    print(
        f"The computer drew the {computer_card[0].lower().capitalize()} of {computer_card[1].lower().capitalize()}! - (Worth {computer_card_value} Points)")
    print(f"Computer Value Total: {computer_value}")


def userTurn():
    global user_value

    # Establish connection to droidcam server (camera) and then init the QRCodeDetector
    cap = cv2.VideoCapture('http://192.168.X.XXX:4747/video')
    detector = cv2.QRCodeDetector()

    # Fetch camera frames from droidcam while camera instance is connected.
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        # Detect all qr codes in frame and retrieve the data from within
        data, bbox, _ = detector.detectAndDecode(frame)
        # Check if  there is data (data is true and thus not None)
        if data:
            tmp_card = data
            user_card = data.split("-")

            # Get the value of the card from a dict and add to the value of user
            user_card_value = values.get(user_card[0])
            user_value += user_card_value

            del user_deck[user_deck.index(tmp_card)]

            print(
                f"The user drew the {user_card[0].lower().capitalize()} of {user_card[1].lower().capitalize()}! - (Worth {user_card_value} Points)")
            print(f"Computer Value Total: {user_value}")
            cap.release()
            # End connection to droidcam server to prevent further scoring from one turn


computerTurn()
userTurn()
