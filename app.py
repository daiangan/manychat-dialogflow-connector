from flask import Flask, request

from utils import manychat_helpers, dialogflow_helpers

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def connector():
    if request.method == 'POST':
        request_data = request.get_json()
        psid = request_data['user_id']
        manychat_api_key = request_data['manychat_api_key']
        dialogflow_project_id = request_data['dialogflow_project_id']
        dialogflow_agent_id = request_data['dialogflow_agent_id']
        df_text_input = request_data['df_text_input']
        language = request_data['language']
        context = request_data['context']
        input_text = ''

        response = {
            'status': 'success',
        }

        df = dialogflow_helpers.DialogFlowAPI(
            project_id=dialogflow_project_id,
            agent_id=dialogflow_agent_id,
        )

        mc = manychat_helpers.ManyChatAPI(
            api_key=manychat_api_key,
            psid=psid,
        )

        if df_text_input == '':
            mc_user_info = mc.get_user_info()
            if mc_user_info['status'] == 'success':
                input_text = mc_user_info['data']['last_input_text']
        else:
            input_text = df_text_input

        if input_text == '':
            response['status'] = 'error'
            return response

        dialogflow_response = df.detect_intent(
            session_id=psid,
            text=input_text,
            language_code=language,
            context=context if context != '' else None
        )

        if dialogflow_response.parameters:
            for param in dialogflow_response.parameters:
                for key, value in param.items():
                    if value and value != '':
                        mc.set_custom_field_by_name(
                            field_name=key,
                            field_value=value[0] if isinstance(value, list) else value,
                        )

        for message in dialogflow_response.messages:
            if message['type'] == 'text':
                mc.send_content(
                    messages=[
                        message['message']
                    ]
                )
            else:
                mc.send_flow(
                    flow_ns=message['flow']
                )

        return response

    else:
        return 'I am alive!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
