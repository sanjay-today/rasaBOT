## welcome path 
* welcome
  - utter_welcome

## greet path 
* greet
  - form_info
  - form{"registration": "form_info"}
  - slot{"requested_slot": "registration"}

## registration path
* registration{"registration":"MH12RN1289"}
  - form_info
  - form{"name": "form_info"}
  - slot{"requested_slot": "name"}
  

## name path
* name
  - form_info
  - form{"phone": "form_info"}
  - slot{"requested_slot": "phone"}
  

## phone path  
* phone{"phone":"9005839050"}
  - form_info
  - form{"email": "form_info"}
  - slot{"requested_slot": "email"}

## email path
* email{"email":"sanjayyadav@gmail.com"}
  - utter_anything_else

## bye path 
* deny
  - utter_bye

## bot challenge
* bot_challenge
  - utter_iamabot
