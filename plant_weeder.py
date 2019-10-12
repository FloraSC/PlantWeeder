from googleapiclient.discovery import build
import pprint

__author__ = 'micah_benjamin_steinberg'

my_api_key = "AIzaSyCbANyRJ7Bj18DiQ8B4WKDDbN-nS-ujVjc"
my_cse_id = "013757675577679800349:n8wq5iaw6ag"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'plant',
    my_api_key,
    my_cse_id,
    searchType="image"
)

for result in results:
    pprint.pprint(result)
