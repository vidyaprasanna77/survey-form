# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from urllib import response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("my_name")
        mobile=tracker.get_slot("mobile_number")
        email=tracker.get_slot("email_id")
        sport=tracker.get_slot("fav_sport")
        info=f"{name},{mobile},{email},{sport}"
        with open("information.txt","w") as file:
            file.write(info)
        dispatcher.utter_message(response="utter_thanks")

        return []
