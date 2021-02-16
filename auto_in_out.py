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
        print('SlackMessage.py -m <message>')
        sys.exit(2)

    if len(opts) == 0:
        message = "HELLO, WORLD!"

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
                print("input 'in' or 'out'")

    send_slack_message(message)

if __name__ == "__main__":
    main(sys.argv[1:])