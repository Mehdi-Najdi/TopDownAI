import random
import spacy

nlp = spacy.load("en_core_web_sm")

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "Outlook not so good.",
    "My sources say no.",
    "Very doubtful."
]

evaluation_questions = {
    "Will I get a raise this year?": "Better not tell you now.",
    "Should I invest in Bitcoin?": "Cannot predict now.",
    "Will I win the lottery?": "Very doubtful.",
    "Will it rain tomorrow?": "Reply hazy, try again.",
    "Will I pass my exam?": "Yes, definitely.",
    "Is it a good day to ask my boss for a promotion?": "Outlook good."
}


def magic_eight_ball():
    """
    Function to simulate a magic eight ball that returns a response based on the user's question.
    """
    print("Welcome to the Magic 8 Ball! Ask me a question.")
    question = input("Ask me a question: ")

    # Perform part-of-speech tagging and dependency parsing on the question
    doc = nlp(question)

    # Identify the subject of the question
    subject = None
    for token in doc:
        if token.dep_ == "nsubj":
            subject = token.text

    # Identify the verb of the question
    verb = None
    for token in doc:
        if token.pos_ == "VERB":
            verb = token.lemma_

    # Generate a response based on the subject and verb of the question
    response = None
    for r in responses:
        r_doc = nlp(r)
        for token in r_doc:
            if token.text == subject and token.dep_ == "nsubj":
                if verb is not None and verb in [t.lemma_ for t in r_doc if t.pos_ == "VERB"]:
                    response = r
                    break
        if response is not None:
            break

    # If no appropriate response is found, select a random response
    if response is None:
        response = random.choice(responses)

    print(response)

    # Check if the question is in the evaluation set
    if question in evaluation_questions:
        expected_response = evaluation_questions[question]
        if response == expected_response:
            print("Correct!")
        else:
            print(f"Incorrect. Expected: {expected_response}")