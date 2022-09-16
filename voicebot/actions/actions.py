
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction,Action

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_registration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Hello World!")
        #print(dispatcher.utter_message(text="Hello how can I help you?"))
        # dispatcher.utter_template('utter_your_num', tracker, number=details[str(tracker.get_slot('NAME')).lower()])
        return []


class ActionFormInfo(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name",'phone',"registration",'email']

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(   response="utter_submit", 
                                    name = tracker.get_slot('name'),
                                    phone = tracker.get_slot('phone'),
                                    registration = tracker.get_slot('registration'),
                                    email = tracker.get_slot('email'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": [self.from_text()],
            "phone": [self.from_text()],
            "registration": [self.from_text()],
            "email": [self.from_text()]
        }

def validate_name(
    self,
    value: Text,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
) -> Dict[Text, Any]:
    
    
    requested_slot = tracker.get_slot("requested_slot")
    name = tracker.get_slot("name")

    if requested_slot == "name":
        return {"name": value}
    elif name:
        return {"name": name}
    else:
        return {"name": None}

def validate_phone(
    self,
    value: Text,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
) -> Dict[Text, Any]:
    
    
    requested_slot = tracker.get_slot("requested_slot")
    phone = tracker.get_slot("phone")

    if requested_slot == "phone":
        return {"phone": value}
    elif phone:
        return {"phone": phone}
    else:
        return {"phone": None}

def validate_email(
    self,
    value: Text,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
) -> Dict[Text, Any]:
    
    
    requested_slot = tracker.get_slot("requested_slot")
    email = tracker.get_slot("email")

    if requested_slot == "email":
        return {"email": value}
    elif email:
        return {"email": email}
    else:
        return {"email": None}

def validate_registration(
    self,
    value: Text,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
) -> Dict[Text, Any]:
    
    
    requested_slot = tracker.get_slot("requested_slot")
    registration = tracker.get_slot("registration")

    if requested_slot == "registration":
        return {"registration": value}
    elif registration:
        return {"registration": registration}
    else:
        return {"registration": None}
