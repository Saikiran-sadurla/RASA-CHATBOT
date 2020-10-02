## happy path
* greet
  - utter_greet

* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help

* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye


## bot challenge
* bot_challenge
  - utter_iamabot

## best colleges
* top_colleges
  - action_colleges
## top news
* top_news
  - utter_news
##prediction
* greet
    - utter_greet
* predict_college
    - predict_form
    - form{"name":"predict_form"}
    - form{"name": null}
    - utter_slots_values
    - action_output

* goodbye
    - utter_goodbye
    
 ##predict
 * predict_college
    - predict_form
    - form{"name":"predict_form"}
    - form{"name": null}
    - utter_slots_values
    - action_output
