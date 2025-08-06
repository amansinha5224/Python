import time
from plyer import notification

interval = float(input("Enter Interval for Notification (in min.): "))

count = 1
while True:
    notification.notify(
        title='Reminder!',
        message='Take a break or stretch a bit and drink some water.',
        app_name='FocusApp',
        timeout=10  # seconds the notification stays on screen
    )
    print(f"Reminder {count}")
    count += 1
    time.sleep(interval*60)
