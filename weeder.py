__author__ = "Nolan Jimenez"
import pprint
from googleapiclient.discovery import build

def main():
    service = build("customsearch", "v1", developerKey="")
    res = service.cse().list(
        q='',
        cx='',
    ).execute()
    pprint.pprint(res)

if __name__ == '__main__':
    main()
