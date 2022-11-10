import requests
import json

ACCESS_TOKEN = 'tVpF0s5Ofnk4z1PIq-vrX4SuwQxAtr0AeO4-Pe34.HpzjzzdhpJfK6tMNO0cyfSTuEMGwOZZc6YLV8OJ1NBuBaM860P4VAKWto28fz0YN5cfT-3aWVxP-VGT1D6EdiyI'

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

#perhpas here is the problem
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


                        
                                
                    
                            
        