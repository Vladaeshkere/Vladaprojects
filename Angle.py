angle = None
ErrorTypeAngle = True
if ErrorTypeAngle:
    while ErrorTypeAngle:
        try:
            angle = int(input('Напишіть градусну міру кута'))
            ErrorTypeAngle = False
        except ValueError:
            print('Будь ласка напишіть нормально')

ErrorNumberAngle = None
if angle < 0 or angle > 180:
    ErrorNumberAngle = True
    while ErrorNumberAngle:
        print('Будь ласка напишіть число не менше за 0 і не більше за 180')
        ErrorTypeAngle = True
        while ErrorTypeAngle:
            try:
                angle = int(input('Напишіть градусну міру кута'))
                ErrorTypeAngle = False
            except ValueError:
                print('Будь ласка напишіть нормально')
        if 0 < angle < 180:
            ErrorNumberAngle = False

if 0 < angle < 90:
    print('Кут гострий')
elif angle == 90:
    print('Кут прямий')
elif 90 < angle < 180:
    print('Кут тупий')
elif angle == 180:
    print('Кут розгорнутий')
elif angle == 0:
    print('Кут нульовий')
