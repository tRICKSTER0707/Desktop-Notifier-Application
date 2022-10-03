from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
           title = "Amit!!..Your Organs Need Water",
           message = '''The National Academics of Sciences, Engineering and Medicine determined that an adequate daily fluid intake is: About 15.5 cups(3.7 litres) of fluids for men. About 11.5 cups(2.7 litres) of fluids a day for women.''',
           app_icon = 'C:/Users/yadav/OneDrive/Desktop/PROJECT 03/iicon.ico',
           timeout=10
        )
        time.sleep(3600)