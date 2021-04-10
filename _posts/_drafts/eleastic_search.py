import boto3
import time
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from korean_convert import korean_to_englished_string
ACCESS_KEY = 'AKIAJGOUCFHQEEDMFIGA'
SECRET_KEY = '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'
# session = boto3.Session(
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY,
# )
#
# dynamodb = session.resource('dynamodb', region_name='us-east-2')
# table = dynamodb.Table('subscriptions')
host = 'https://search-taehyuntest-htanxvuwtmn5jdisq5h5b7xa6q.us-east-2.es.amazonaws.com'
region = 'us-east-2'
service = 'es'
auth = AWS4Auth(ACCESS_KEY, SECRET_KEY, region, service)
es = Elasticsearch(
    hosts=[host],
    http_auth=auth,
    user_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    port=443
)
index = 'subscriptions'
# body = {
#     "settings": {
#         "index": {
#             "number_of_shards": 1,
#             "number_of_replicas": 0,
#             "max_ngram_diff": 30
#         },
#         "analysis": {
#             "analyzer": {
#                 "name_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "ngram_tokenizer"
#                 },
#                 "converted_name_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "edge_ngram_tokenizer"
#                 }
#             },
#             "tokenizer": {
#                 "ngram_tokenizer": {
#                     "type": "nGram",
#                     "min_gram": 1,
#                     "max_gram": 10,
#                     "token_chars": [
#                         "letter"
#                     ]
#                 },
#                 "edge_ngram_tokenizer": {
#                     "type": "edgeNGram",
#                     "min_gram": 1,
#                     "max_gram": 25,
#                     "token_chars": [
#                         "letter"
#                     ]
#                 }
#             }
#         }
#     },
#     "mappings": {
#         "properties": {
#             "name": {
#                 "type": "text",
#                 "analyzer": "name_analyzer",
#                 "search_analyzer": "name_analyzer",
#                 "boost": 0.2
#             },
#             "converted_name": {
#                 "type": "text",
#                 "analyzer": "converted_name_analyzer",
#                 "search_analyzer": "converted_name_analyzer",
#                 "boost": 1.5
#             }
#         }
#     }
# }
#
# es.indices.delete(index=index, ignore=[400, 401])
# es.indices.create(index=index, body=body)
#
# response = table.scan()
# subscriptions = response['Items']
#
# for idx, data in enumerate(subscriptions):
#     subscription = korean_to_englished_string(data['name'])
#     # data['name'] = ' '.join(data['name'])
#     # subscription = ' '.join(subscription)
#     data['converted_name'] = subscription
#
# for idx, data in enumerate(subscriptions):
#     res = es.index(index=index, body=data, id=idx)
#
# time.sleep(2)
client_request = "ㅇㅇ스탠"
client_word = korean_to_englished_string(client_request)
query = {
    "query": {
        "bool": {
            "should": [
                {
                    "match": {
                        "converted_name": client_word
                    }
                },
                {
                    "match": {
                        "name": client_request
                    }
                }
            ],
            "minimum_should_match": 1
        }
    }
}
res = es.search(index=index, body=query)
print(res)
results = res['hits']['hits']
names = []
for result in results:
    if result['_score'] > 0:
        names.append(result['_source']['name'])
print(names)