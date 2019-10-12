import pprint

from googleapiclient.discovery import build

def main():
    service = build("customsearch", "v1", developerKey="AIzaSyCbANyRJ7Bj18DiQ8B4WKDDbN-nS-ujVjc")
    res = service.cse().list(
        q='plants',
        cx='013125366642420418874:8iebi6x9bd6',
    ).execute()
    pprint.pprint(res)

if __name__ == '__main__':
    main()