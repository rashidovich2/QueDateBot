from better_profanity import profanity


def censored_message(message):
    return profanity.censor(message)
