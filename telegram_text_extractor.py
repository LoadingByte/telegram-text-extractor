import json



def input_choice(choices, prompt, allow_blank=False):
    print('Available chocies: ' + ', '.join(choices))
    choice = input(prompt)
    if choice in choices or (allow_blank and choice == ''):
        return choice
    else:
        raise ValueError('This choice is not available: ' + choice)


def extract_text(node):
    if isinstance(node, str):
        return node
    elif isinstance(node, dict):
        if 'text' in node:
            return extract_text(node['text'])
        else:
            raise ValueError('Encountered dict without text field while extracting text: ' + str(node))
    elif isinstance(node, list):
        return ''.join(map(extract_text, node))
    else:
        raise ValueError('Encountered unexpected node extracting text: ' + str(node))



with open('result.json', encoding='utf8') as input_file:
    telegram_export = json.load(input_file)

available_chat_names = [chat['name'] for chat in telegram_export['chats']['list'] if ('name' in chat) and chat['name'] != None]
requested_chat_name = input_choice(available_chat_names, 'Enter requested chat name: ')

requested_chat = next(chat for chat in telegram_export['chats']['list'] if ('name' in chat) and chat['name'] == requested_chat_name)

print()
available_author_names = set([message['from'] for message in requested_chat['messages'] if ('from' in message)])
requested_author_name = input_choice(available_author_names, 'Only export this person\'s messages (leave blank to export everything): ', allow_blank=True)

extracted_text = '\n\n'.join([extract_text(message) for message in requested_chat['messages']
    if ('from' in message) and (requested_author_name == '' or message['from'] == requested_author_name)])

with open('output.txt', 'w', encoding='utf8') as output_file:
    output_file.write(extracted_text)
