#The script should accept a JSON file with questions for the survey and a text file with a list of email addresses.
#The structure of a JSON file with questions: "Survey_Name" "Page_Name": "Question1_Name" "Description" : "Description of question","Answers" : "Answer1" "Answer2","Answer3"
#ACCESS_TOKEN which is needed to do API requests from your script.
#There should be at least 3 questions and 2 recipients.

import requests
import json

ACCESS_TOKEN = 'tVpF0s5Ofnk4z1PIq-vrX4SuwQxAtr0AeO4-Pe34.HpzjzzdhpJfK6tMNO0cyfSTuEMGwOZZc6YLV8OJ1NBuBaM860P4VAKWto28fz0YN5cfT-3aWVxP-VGT1D6EdiyI'
SURVEY_NAME = 'Survey'
PAGE_NAME = 'Page'
QUESTION_NAME = 'Question'
DESCRIPTION = 'Description of question'
ANSWERS = 'Answer1', 'Answer2', 'Answer3'
RECIPIENTS = 'leczek.weronika@gmail.com'

def create_survey():
        
    url = 'https://api.surveymonkey.net/v3/surveys'
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {
    "title": "p_task6_survey",
    "language": "en",
    "folder_id": "0",
    "footer": True,
    "custom_variables": {},
    "pages": [
        {
            "title": "",
            "position": 1,
            "questions": [
                {
                    "visible": True,
                    "family": "single_choice",
                    "subtype": "vertical",
                    "headings": [
                        {
                            "heading": "Question1_Name"
                        }
                    ],
                    "answers": {
                        "choices": [
                            {
                                "position": 1,
                                "visible": True,
                                "text": "Answer1",
                                "quiz_options": {
                                    "score": 0
                                }
                            },
                            {
                                "position": 2,
                                "visible": True,
                                "text": "Answer2",
                                "quiz_options": {
                                    "score": 0
                                }
                            },
                            {
                                "position": 3,
                                "visible": True,
                                "text": "Answer3",
                                "quiz_options": {
                                    "score": 1
                                }
                            }
                        ]
                    },
                },
                {
                    "visible": True,
                    "family": "single_choice",
                    "subtype": "vertical",
                    "headings": [
                        {
                            "heading": "Question2_Name"
                        }
                    ],
                    "answers": {
                        "choices": [
                            {
                                "position": 1,
                                "visible": True,
                                "text": "Answer1",
                                "quiz_options": {
                                    "score": 0
                                }
                            },
                            {
                                "position": 2,
                                "visible": True,
                                "text": "Answer2",
                                "quiz_options": {
                                    "score": 0
                                }
                            },
                            {
                                "position": 3,
                                "visible": True,
                                "text": "Answer3",
                                "quiz_options": {
                                    "score": 1
                                }
                            }
                        ]
                    },
                },
                {
                    "visible": True,
                    "family": "single_choice",
                    "subtype": "vertical",
                    "headings": [
                        {
                            "heading": "Question3_Name"
                        }
                    ],
                    "answers": {
                        "choices": [
                            {
                                "position": 1,
                                "visible": True,
                                "text": "Answer1",
                                "quiz_options": {
                                    "score": 0
                                }
                            },
                            {
                                "position": 2,
                                "visible": True,
                                "text": "Answer2",
                                "quiz_options": {
                                    "score": 0
                                }
                            },
                            {
                                "position": 3,
                                "visible": True,
                                "text": "Answer3",
                                "quiz_options": {
                                    "score": 1
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ]
}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    return response.json()

    
def send_survey():

    url = 'https://api.surveymonkey.net/v3/surveys/123456789/collectors'
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {
        "type": "email",
        "name": "Test",
        "recipients": {
          "list_id": "123456789",
            "custom_emails": [
                "leczek.weronika@gmail.com"
            ]
        },
        "subject": "Test",
        "from_email": "leczek.weronika@gmail.com",
        "from_name": "Test",
        "message": "Test",
        "is_shareable": True,
        "is_test": True,
        "logic_jump": {
            "default": {
                "type": "next_page"
            }
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    
def add_recipients(survey_id):
    url = 'https://api.surveymonkey.net/v3/surveys/%s/collectors//recipients' % survey_id
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {
        "recipients": [
            {
                "address": "leczek.weronika@gmail.com"
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)

def create_collector(survey_id):
    url = 'https://api.surveymonkey.net/v3/surveys/%s/collectors' % survey_id
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {
        "type": "weblink",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    return response.json()
    
def add_message(survey_id):
    url = 'https://api.surveymonkey.net/v3/collectors/%s/messages' % survey_id
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {
             "type": "invite",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    return response.json()

def add_recipients_to_collector(collector_id, message_id):
    url = 'https://api.surveymonkey.net/collectors/%s/messages/%s/recipients' % (collector_id, message_id)
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {
    "email": "leczek.weronika@gmail.com",
    "first_name": "Weronika",
    "last_name": "Łęczek",
    "custom_fields": {
        "1": "First Value",
        "2": "Second Value",
        "3": "Third Value"
    },
    "extra_fields": {
        "field_name1": "field_value1",
        "field_name2": "field_value2"
    }
}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
    
def send_email(collector_id, message_id):
    url = 'https://api.surveymonkey.net/v3/collectors/%s/messages/%s/send' % (collector_id, message_id)
    headers = {'Authorization': 'bearer %s' % ACCESS_TOKEN, 'Content-Type': 'application/json'}
    data = {}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.text)
      
    
def main():
    survey_id = create_survey().get('id')
    collector_id = create_collector(survey_id).get('id')
    message_id = add_message(collector_id).get('id') 
    add_recipients_to_collector(collector_id, message_id)
    send_email(collector_id, message_id)
    
if __name__ == '__main__':
    main()


                        
                                
                    
                            
        