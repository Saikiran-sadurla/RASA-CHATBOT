# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import json


class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "predict_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("required_slots(tracker:Tracker)")
        return ["name", "caste", "rank", "course"]

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any],
               ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return []

    # validation for caste

    @staticmethod
    def caste_db() -> List[Text]:
        return [
            "OC_BOYS",
            "OC_GIRLS",
            "BC_A_BOYS",
            "BC_A_GIRLS",
            "BC_B_BOYS",
            "BC_B_GIRLS",
            "BC_C_BOYS",
            "BC_C_GIRLS",
            "BC_D_BOYS",
            "BC_D_GIRLS",
            "BC_E_BOYS",
            "BC_E_GIRLS",
            "SC_BOYS",
            "SC_GIRLS",
            "ST_BOYS",
            "ST_GIRLS",
        ]

    def validate_caste(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value.upper() in self.caste_db():
            return {"caste": value}

        else:
            dispatcher.utter_message(template="utter_wrong_caste")
            return {"caste": None}

    @staticmethod
    def validate_rank(
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if len(value) <= 6:
            return {"rank": value}

        else:
            dispatcher.utter_message(template="utter_wrong_rank")
            return {"rank": None}


# accessing data from json file

class ActionFinalWorld(Action):

    def name(self) -> Text:
        return "action_output"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
        new_c = tracker.get_slot("caste")
        new_r = tracker.get_slot("rank")
        new_co = tracker.get_slot("course")

        f = open('csvjson.json', )
        data = json.load(f)
        for i in data['college_prediction']:
            if i[new_c] == 'NA':
                pass
            else:
                x = i[new_c]
                if (int(x) - 5000 < int(new_r)) and (int(x) + 10000 > int(new_r)) and (i["Branch_Code"] == new_co):
                    dispatcher.utter_message("college name\t" + i['Inst_Name'] + "\nfee\t" + str(i['Tuition_Fee'])+ "\nLast Rank\t" + str(i[new_c]))

                else:
                    pass

        f.close()
        return []


class TopCollege(Action):
    def name(self) -> Text:
        return "action_colleges"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
            ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("1:JNTU HYDERABAD - JNTU ")
        dispatcher.utter_message("2:Osmania University - OU")
        dispatcher.utter_message("3:CBIT(Chaitanya Bharat Institute of technology) - OU(its autonomous college)")
        dispatcher.utter_message("4:Vasavi - OU""5:VNR Vignan Jyothi - JNTU")
        dispatcher.utter_message("6:SriNidhi College - JNTU")
        dispatcher.utter_message("7:Naraynamma college - JNTU")
        dispatcher.utter_message("8:Vardhaman college - Autonomus")
        dispatcher.utter_message("9:CVR College - JNTU")
        dispatcher.utter_message("10:Gokaraju Rangaraju - JNTU")
        dispatcher.utter_message("11:MVSR College - OU")
        dispatcher.utter_message("12:JNTU Kareemnagar - JNTU")
        dispatcher.utter_message("13:MGIT College - JNTU (Beside CBIT College)")
        dispatcher.utter_message("14:Muffakham Jah College of Engineering (MJ college best for minority - OU students)")
        dispatcher.utter_message("15:JNTU: Sultanpur - JNTU")
        dispatcher.utter_message("16:BVRIT College - JNTU")
        dispatcher.utter_message("17:Matrusri College - OU")
        dispatcher.utter_message("18:CVSR College - JNTU")
        dispatcher.utter_message("19:IARE College(best for aeronautical branch also other branches - JNTUare there)")
        dispatcher.utter_message("20:JNTU Manthani - JNTU")
        return []
