import webbrowser
import time

#initialize counter
count = 0
frequency = 3
#Loop through the frequency of breaks and open the browser to play a song every hour
while(count < frequency):
    time.sleep(60*60)
    count = count+1
    webbrowser.open("https://www.youtube.com/watch?v=ElWN4B4Wvxw")
    
    



