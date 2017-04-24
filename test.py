from ubidots import ApiClient

api = ApiClient(token='9DKg2IZOfbshkldF62l0SNvghxbCls')

temp = api.get_variable('58fdc0357625420d815053e1')


while True:
    print("temp:", end=" ")
    t = input()
    if t == 'q':
        break
    try:
        temp.save_value({'value': int(t)})
    except ValueError:
        print("invalid temp")
