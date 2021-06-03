from typing import Any, Text, Dict, List, Union, Optional ## Datatypes
from rasa_sdk import Action, Tracker, FormValidationAction ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted, ConversationPaused, EventType

class ValidateComplaint(FormValidationAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "validate_form_complaint"
        
    def validate_complaint(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate exper value."""

        complaint = tracker.get_slot('complaint')
        
        if complaint:
            if len(complaint)>=10:
                return {'complaint':complaint}
            else:
                dispatcher.utter_message(text="Please enter a description more than 10 characters.")
                return {"complaint":None}
        else:
            dispatcher.utter_message(text="Please enter a description.")
            return {"complaint":None}

    def validate_submit_complaint(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]: 
        """Validate related work."""

        intent= tracker.latest_message["intent"].get("name")
            
        if intent=="affirm" or value == "/affirm":
            return {"submit_complaint":"OK"}

        elif intent=="deny" or value == "/deny":
            new_feature_value_list = []
            return {"complaint":None, "submit_complaint":None}
            
        else:
            dispatcher.utter_message(text="I couldn't get a valid option!.")
            return {"submit_complaint": None}


class ActionCreateComplaint(Action):

    def name(self) -> Text:
        return "action_create_complaint"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:    

        dispatcher.utter_message(text="Your complaint have been forwarded to the concerning department.")
        dispatcher.utter_message(response="utter_anything_else")

        return [SlotSet('complaint',None), SlotSet('submit_complaint', None)]

class ActionSlotReset(Action):

    def name(self) -> Text:
        return "action_slot_reset"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:    

        dispatcher.utter_message(response="utter_anything_else") 
        return [AllSlotsReset()]


                