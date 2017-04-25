from ubidots import ApiClient

raise Exception("Configuration needed")

api_token = ''

api = ApiClient(token=api_token)

temp = api.get_variable('')

is_charging = api.get_variable('')
