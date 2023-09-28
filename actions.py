

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted, SlotSet
#
#
class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        number = tracker.get_slot("number")
        city = tracker.get_slot("city")
        ass_id = tracker.get_slot("ass_id")

        dispatcher.utter_message(text=f"Hey {name}! Glad to have you here.\nMobile No.:{number} \nAssociate ID: {ass_id} \n{city} branch is really amazing \n Do you need any help?")

        return []

class ValidateSimpleForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_simple_form"

    def validate_number(self, slot_value: Any, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number = tracker.get_slot("number")

        if(int(len(number))>10):
            dispatcher.utter_message(text="Invalid phone number")
            return{"number":None}
        if (int(len(number)) < 10):
            dispatcher.utter_message(text="Invalid phone number")
            return {"number": None}
        else:
            return{"number":number}


class CustomRestartAction(Action):
    def name(self) -> Text:
        return "action_custom_restart"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        return [Restarted(), SlotSet("requested_slot", None)]