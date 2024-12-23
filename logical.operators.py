#These are the logical operators (Or, and)

temp = 25
is_sunny = False

if temp > 30 or is_sunny:
    print('it is hot and sunny')

elif 25 > temp > 0 and is_sunny:
    print('it is warm and sunny')

elif temp < 0 and not is_sunny:
    print('dang, it is cold')

else :
    print('its low-key cool')
