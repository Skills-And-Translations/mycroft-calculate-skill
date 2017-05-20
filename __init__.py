from __future__ import division
import sys
import dbus
import glib
import os
import math
import psutil
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import subprocess


__author__ = 'hersche'


LOGGER = getLogger(__name__)

class CalculateSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor 
    def __init__(self):
        super(CalculateSkill, self).__init__(name="CalculateSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        
        internals_plus_intent = IntentBuilder("CalculatePlusIntent").\
            require("CalculateKeyword").require("firstNr").require("PlusKeyword").require("secondNr").build()
        self.register_intent(internals_plus_intent, self.handle_internals_plus_intent)

        
        internals_minus_intent = IntentBuilder("CalculateMinusIntent").\
            require("CalculateKeyword").require("firstNr").require("MinusKeyword").require("secondNr").build()
        self.register_intent(internals_minus_intent, self.handle_internals_minus_intent)
        
        internals_divide_intent = IntentBuilder("DivideMinusIntent").\
            require("DivideKeyword").require("firstNr").require("WithKeyword").require("secondNr").build()
        self.register_intent(internals_divide_intent, self.handle_internals_divide_intent)
        
        internals_squareof_intent = IntentBuilder("SquareOfMinusIntent").\
            require("SquareOfKeyword").require("firstNr").build()
        self.register_intent(internals_squareof_intent, self.handle_internals_squareof_intent)
        
        internals_pi_intent = IntentBuilder("PiIntent").\
            require("PiKeyword").build()
        self.register_intent(internals_pi_intent, self.handle_internals_pi_intent)


    def handle_internals_pi_intent(self, message):
        self.speak("Pi is 3.1415")

    def handle_internals_squareof_intent(self, message):
        firstNr = message.data.get("firstNr")
        try:
            pFirstNr = int(firstNr)
            self.speak("square of "+firstNr+" is "+str(math.sqrt(pFirstNr)))
        except ValueError:
            self.speak("sorry, was not able to resolve the task. please use your calculator")

    def handle_internals_divide_intent(self, message):
        firstNr = message.data.get("firstNr")
        secondNr = message.data.get("secondNr")
        
        try:
            pFirstNr = float(firstNr)
            pSecondNr = float(secondNr)
            self.speak(firstNr+ " divided with "+secondNr+" is "+str(pFirstNr/pSecondNr))
        except ValueError:
            self.speak("sorry, was not able to resolve the task. please use your calculator")
        
    def handle_internals_plus_intent(self, message):
        firstNr = message.data.get("firstNr")
        secondNr = message.data.get("secondNr")
        try:
            pFirstNr = int(firstNr)
            pSecondNr = int(secondNr)
            self.speak(firstNr+ " plus "+secondNr+" is "+str(pFirstNr+pSecondNr))
        except ValueError:
            self.speak("sorry, was not able to resolve the task. please use your calculator")
 
 
    def handle_internals_minus_intent(self, message):
        firstNr = message.data.get("firstNr")
        secondNr = message.data.get("secondNr")
        try:
            pFirstNr = int(firstNr)
            pSecondNr = int(secondNr)
            self.speak(firstNr+ " minus "+secondNr+" is "+str(pFirstNr-pSecondNr))
        except ValueError:
            self.speak("sorry, was not able to resolve the task. please use your calculator")
            

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return CalculateSkill()
