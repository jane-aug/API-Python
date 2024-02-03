import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

obj = json.loads(json_text)

second_message = obj['messages'][1]['message']
print(json.dumps(second_message, indent=4, sort_keys=True))

'''
#печать в цикле всех сообщений
for messages in obj['messages']:
    print(messages['message'])
'''