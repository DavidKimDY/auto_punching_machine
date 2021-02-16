import requests
import sys
import getopt
from datetime import datetime

# Send Slack Message Using Slack API

def send_slack_message(message):
    payload = '{"text": "%s"}' % message.encode('utf-8').decode('latin-1')
    response = requests.post('https://hooks.slack.com/services/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',
                             data = payload)
    print(response.text)

def main(argv):

    date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')

    message = ' '
    try:
        opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('auto_in_out.py -m <message>')
        print('message: in or out')
        sys.exit(2)

    if len(opts) == 0:
        print('auto_in_out.py -m <message>')
        print('message: in or out')

    for opt, arg in opts:
        if opt == '-h':
            print('SlackMessage.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            if arg == 'in':
                message = date + ' ' + '출근'
            elif arg == 'out':
                message = date + ' ' + '퇴근'
            else :
                print("input in or out")

    send_slack_message(message)

if __name__ == "__main__":
    main(sys.argv[1:])