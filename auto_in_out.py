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

# def main(argv):
# 
#     try: opts, args = getopt.getopt(argv, "hm:", ["message="])
# 
#     except getopt.GetoptError:
#         print('SlackMessage.py -m <message>')
#         sys.exit(2)
#     if len(opts) == 0:
#         message = "HELLO, WORLD!"
#     for opt, arg in opts:
#         if opt == '-h':
#             print('SlackMessage.py -m <message>')
#             sys.exit()
#         elif opt in ("-m", "--message"):
#             message = arg
# 
#     send_slack_message(message)

if __name__ == "__main__":
    date = datetime.now()
    send_slack_message(f"{datetime.strftime(date, '%Y-%m-%d %H:%M')} 출근")