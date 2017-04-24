from ubidots import ApiClient
from api_token import api_token

api = ApiClient(token=api_token)

temp = api.get_variable('58fdc0357625420d815053e1')

is_charging = api.get_variable('58fe6d5d7625424b9c5368f0')