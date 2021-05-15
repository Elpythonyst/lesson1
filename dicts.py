data = {'city':'Москва', 'temperature':'20'}
print(data['city'])
data['temperature'] = int(data['temperature']) - 5
data

print(data.get('country', 'Russia'))
data['date'] = '27.05.2019'
data
print(len(data))    