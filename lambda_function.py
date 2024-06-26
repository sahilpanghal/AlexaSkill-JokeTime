# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
#Created by Sahil Panghal
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

jokes = [
        "Did you hear about the semi-colon that broke the law? He was given two consecutive sentences.",
        "I ate a clock yesterday, it was very time-consuming.",
        "I've just written a song about tortillas; actually, it's more of a rap.",
        "I woke up this morning and forgot which side the sun rises from, then it dawned on me.",
        "I recently decided to sell my vacuum cleaner as all it was doing was gathering dust.",
        "If you shouldn't eat at night, why do they put a light in the fridge?",
        "I can’t believe I got fired from the calendar factory: all I did was take a day off!",
        "Money talks: mine always says is goodbye.",
        "I went to see the doctor about my short-term memory problems — the first thing he did was make me pay in advance.",
        "You have two parts of the brain, “left” and “right” — in the left side, there’s nothing right and in the right side, there’s nothing left.",
        "Why do bees hum? They don’t remember the lyrics!",
        "I have a dog to provide me with unconditional love but I also have a cat to remind me that I don’t deserve it: it’s all about balance.",
        "Don’t spell part backwards. It’s a trap.",
        "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.",
        "Most people are shocked when they find out how bad I am as an electrician.",
        "I find it ironic that the colors red, white, and blue stand for freedom until they are flashing behind you.",
        "Moses had the first tablet that could connect to the cloud.",
        "Don’t trust atoms, they make up everything.",
        "Thanks for explaining the word “many” to me, it means a lot.",
        "I hope when I inevitably choke to death on gummy bears people just say I was killed by bears and leave it at that.",
        "I accidentally handed my wife a glue stick instead of a chapstick. She still isn’t talking to me.",
        "I’m reading a book about anti-gravity. It’s impossible to put down.",
        "I wasn’t originally going to get a brain transplant, but then I changed my mind.",
        "R.I.P boiled water. You will be mist.",
        "Alcohol is a perfect solvent: It dissolves marriages, families and careers.",
        "I got a new pair of gloves today, but they’re both ‘lefts’ which, on the one hand, is great, but on the other, it’s just not right.",
        "My wife just found out I replaced our bed with a trampoline; she hit the roof.",
        "What is the best thing about living in Switzerland? Well, the flag is a big plus.",
        "Atheism is a non-prophet organization.",
        "Did you hear about the guy who got hit in the head with a can of soda? He didn’t get hurt because it was a soft drink.",
        "The future, the present and the past walked into a bar. Things got a little tense.",
        "At what age is it appropriate to tell my dog that he’s adopted?",
        "|I just found out I’m colorblind. The diagnosis came completely out of the purple.",
        "I bought some shoes from a drug dealer. I don’t know what he laced them with, but I’ve been tripping all day.",
        "My boss is going to fire the employee with the worst posture. I have a hunch, it might be me.",
        "I started out with nothing, and I still have most of it.",
        "Smoking will kill you… Bacon will kill you… And yet, smoking bacon will cure it.",
        "I was addicted to the hokey pokey… but thankfully, I turned myself around.",
        "Did Noah include termites on the ark?",
        "The Man Who Created Autocorrect Has Died. Restaurant In Peace.",
        "I used to think I was indecisive, but now I’m not too sure.",
        "My wife likes it when I blow air on her when she’s hot, but honestly… I’m not a fan.",
        "I really hate Russian dolls, they’re so full of themselves.",
        "The first time I got a universal remote control I thought to myself, “This changes everything”.",
        "I refused to believe father, the road worker, was stealing from his job, but when I got home all the signs were there.",
        "Where there’s a will, there’s a relative.",
        "It’s hard to explain puns to kleptomaniacs — they’re always taking things literally.",
        "I like to hold hands at the movies… which always seems to startle strangers.",
        "Women should not have children after 35 — 35 children are enough!",
        "There are three kinds of people: those who can count and those who can’t",
        "Whenever I lose my TV controller, I always find it at a remote location.",
        "My first job was working in an orange juice factory, but I got canned: I just couldn’t concentrate.",
        "My math teacher called me average — it’s so mean!",
        "“The easiest time to add insult to injury is when you’re signing somebody’s cast.” – Demetri Martin",
        "I don’t have an attitude problem. You have a perception problem.",
        "I’m skeptical of anyone who tells me they do yoga every day — that’s a bit of a stretch.",
        "Light travels faster than sound, which is why some people appear bright before they open their mouth.",
        "“It’s sad that a family can be torn apart by something as simple as wild dogs.” – Jack Handey",
        "I don’t have a boyfriend, but I do know a guy who would be really mad to hear that.",
        "“The worst time to have a heart attack is during a game of charades.” – Demetri Martin",
        "When life gives you melons, you might be dyslexic.",
        "“I don’t want to be part of a club that would have me as a member.” – Groucho Marx",
        "“Does my wife think I’m a control freak? I haven’t decided yet.” – Stewart Francis",
        "“The New England Journal of Medicine reports that 9 out of 10 doctors agree that 1 out of 10 doctors is an idiot.” – Jay Leno",
        "“I have a lot of growing up to do. I realized that the other day inside my fort.” – Zach Galifianakis",
        "“Honesty may be the best policy, but it’s important to remember that apparently, by elimination, dishonesty is the second-best policy.” – George Carlin",
        "“I looked up my family tree and found out I was the sap.” – Rodney Dangerfield",
        "Keep the dream alive — hit your snooze button.",
        "It sure takes a lot of balls to golf the way I do.",
        "“My therapist says I have a preoccupation with vengeance. We’ll see about that.” – Stewart Francis",
        "I was wondering why the ball kept getting bigger and bigger, and then it hit me.",
        "The person who invented knock knock jokes should get a no bell prize.",
        "The other day I asked the banker to check my balance, so she pushed me.",
        "For a while, Houdini would use a trap door in every single one of his show – I guess you could say it was a stage he was going through.",
        "I hope there’s no pop quiz at the class trip to the Coca Cola factory.",
        "If money doesn’t grow on trees, how come banks have branches?",
        "I didn’t like my beard at first, but it grew on me.",
        "Give me the calculator, friends don’t let friends derive drunk.",
        "A baseball walks into a bar —  the bartender throws it out.",
        "I doubt, therefore I might be.",
        "I used to have a handle on life, but then it broke.",
        "I had an “hour glass” figure, but then the sand shifted.",
        "When everything is coming your way — you’re in the wrong lane.",
        "Animal testing is a terrible idea — they get all nervous and give the wrong answers",
        "“I was playing chess with my friend and he said, ‘Let’s make this interesting’. So we stopped playing chess.” — Matt Kirshen",
        "“Crime in multi-story car parks. That is wrong on so many different levels.” — Tim Vine",
        "“I was raised as an only child, which really annoyed my sister.” —Will Marsh",
        "“People who use selfie sticks really need to have a good, long look at themselves.” — Abi Roberts",
        "“A thesaurus is great. There’s no other word for it” —Ross Smith", 
        "“I failed math so many times at school I can’t even count.” — Stewart Francis",
        "“Two fish in a tank. One says: ‘How do you drive this thing?'” — Peter Kay",
        "“I saw a documentary on how ships are kept together. Riveting!” — Stewart Francis",
        "“People who like trance music are very persistent. They don’t techno for an answer.” — Joel Dommett",
        "“Do Transformers get car, or life insurance?” – Russell Howard",
        "“My father drank so heavily, when he blew on the birthday cake he lit the candles.” – Les Dawson",
        "I once saw two people wrapped in a barcode and had to ask — “are you an item?”",
        "I went to buy camouflage trousers but I couldn’t find any.",
        "“Alright lads, a giant fly is attacking the police station. I’ve called the SWAT team!” — Greg Davies",
        "“I usually meet my girlfriend at 12:59 because I like that one-to-one time.” — Tom Ward",
        "“I like a woman with a head on her shoulders. I hate necks.” — Steve Martin",
        "My husband and I were happy for 20 years. And then we met.",
        "I, for one, like Roman numerals.",
        "When my boss asked me who was stupid, me or him, I told him he doesn’t hire stupid people.",
        "Any married person should forget their mistakes. No use two people remembering the same thing.",
        "My wife told me to stop impersonating a flamingo. I had to put my foot down.",
        "I, for one, like Roman numerals.",
        "I have an inferiority complex, but it’s not a very good one.",
        "“People tell me I’m condescending…” (Leans in real close) “That means I talk down to people. ",
        "“By the time a man is wise enough to watch his step he is too old to go anywhere.” — Billy Crystal",
        "“Proof that we don’t understand death is that we give dead people a pillow.” — Jerry Seinfeld",
        "“Don’t talk to me about Valentine’s Day. At my age, an affair of the heart is a bypass.” — Joan Rivers",
        "“Learning to dislike children at an early age saves a lot of expense and aggravation later in life.” — Ed Byrne",
        "“I failed math so many times in school I lost count.” — Stewart Francis",
        "“Oh, when I was a kid in show business I was poor. I used to go to orgies to eat the grapes.” — Rodney Dangerfield",
        "“In the school I went to, they asked a kid to prove the law of gravity and he threw the teacher out of the window.”— Rodney Dangerfield",
        "“I looked up my family tree and found three dogs using it.”— Rodney Dangerfield",
        "“One time my whole family played hide and seek. They found my mother in Pittsburgh!” — Rodney Dangerfield",
        "“I met the surgeon general – he offered me a cigarette.”— Rodney Dangerfield",
        ]

class JokeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("JokeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = random.choice(jokes)
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hey there! I am a Joke Time. You can ask me to tell you a random Joke that might just make your day better!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(JokeIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
