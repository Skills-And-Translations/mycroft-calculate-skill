# mycroft-calculate-skill
This skill is very in a beginn! Joining welcomed.

The sense of this skill is the following: At the moment, when you ask "whats 1 + 1", the wolfram alpha-search-engine will give you kind of fallback-response.

Calculating math's is no problem for python, so why not doing this stuff on mycroft's cpu itself?

Should

- save response-time
- allow offline query (due to speech to text, for the only real offline-scenario you have to chat)

#### Installation of skill:
* Download or Clone Git
* Create /opt/mycroft/skills folder if it does not exist
* Copy the mycroft-calculate-skill folder to /opt/mycroft/skills/ folder


##### How To Use: 
###### Plus and minus
- "Hey Mycroft, calc 1 + 1"
- "Hey Mycroft, calculate 3 - 5"

###### divide
- "Hey Mycroft, divide 3 with 3"
- "Hey Mycroft, divide 9 through 2"

###### constants
- "Hey Mycroft, what is pi"
- "Hey Mycroft, whats pi"

###### functions
- "Hey Mycroft, square of 3"
- "Hey Mycroft, square of 9"

## Current state

Working features:
* Plus and minus
* divide
* constants
* functions

Known issues:
* None

TODO:
* add more constants than pi and make more accurate (atm, lot is testing)
* add more functions, not only "square of"
* add multiplie-command
* a very cool thing would be to make infinite calculations like "hey mycroft, calculate 3 + 2 divided by 7 - 99 .... " (and so on) - no idea about this yet.
* etc
