import json

def handle_get_meetings(event):
    return {
        'meetings': [1,2,3] 
    }
    
def handle_get_meeting_summary(meeting_id):
    return {
        'summary': 'Este aqui é o sumário de uma reunião. Isso poderia estar em um bucket do Amazon S3, em um banco de dados, etc... Ficamos de conversar com o Bob até o dia 15/02 e verificar com os fornecedores até o final do mês de março.'
    }

def lambda_handler(event, context):
    print(event)  
    response_code = 200
    action_group = event['actionGroup']
    api_path = event['apiPath']

    if api_path == '/meetings':
        result = handle_get_meetings(event)
    elif api_path == '/meetings/{meetingId}/summary':
        result = handle_get_meeting_summary(event)
    else:
        response_code = 404
        result = f'Unrecognized api path: {action_group}::{api_path}'

    response_body = {
        'application/json': {
            'body': result  
        }
    }

    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMethod': event['httpMethod'],
        'httpStatusCode': response_code,
        'responseBody': response_body
    }

    api_response = {'messageVersion': '1.0', 'response': action_response}
    return api_response