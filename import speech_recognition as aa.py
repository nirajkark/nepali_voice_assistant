import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import pyaudio
import datetime
import wikipedia
import webbrowser
import pywhatkit

listener = sr.Recognizer()
machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()










def open_app():
    apps = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Snapchat', 'Pinterest', 'WhatsApp', 'YouTube', 'Tumblr', 'Reddit', 'Flickr', 'Vimeo', 'Periscope', 'TikTok', 'WeChat', 'Viber', 'Telegram', 'LINE', 'KakaoTalk', 'Skype', 'Google Maps', 'Waze', 'Uber', 'Lyft', 'Google Chrome', 'Safari', 'Netflix', 'Hulu', 'Disney+', 'Amazon Prime Video', 'Spotify', 'Apple Music', 'Tinder', 'Bumble', 'Grindr', 'WhatsApp', 'Telegram', 'Signal', 'Zoom', 'Microsoft Teams', 'Google Meet', 'Snapseed', 'Adobe Photoshop Express', 'Evernote', 'Microsoft Word', 'Microsoft Excel', 'Microsoft PowerPoint', 'Dropbox', 'Google Drive', 'OneDrive', 'Shazam', 'Trello', 'Wunderlist', 'Todoist', 'Weather', 'Google Photos', 'Adobe Acrobat Reader', 'Duolingo', 'Khan Academy', 'Google Translate', 'Pocket', 'Flipboard', 'Feedly', 'Kindle', 'Audible', 'WhatsApp Business', 'LinkedIn Learning', 'Twitch', 'Discord', 'Clubhouse', 'Signal', 'Cash App', 'Venmo', 'PayPal', 'Google Pay', 'Apple Pay', 'Zelle', 'Robinhood', 'Coinbase', 'DoorDash', 'Postmates', 'Instacart', 'Uber Eats', 'Grubhub', 'Waze', 'Google Earth', 'Snapchat', 'Bitmoji', 'Facebook Messenger', 'WhatsApp Messenger', 'Skype', 'Hangouts', 'Viber', 'Signal', 'Telegram', 'LINE', 'KakaoTalk', 'WeChat', 'Instagram', 'Snapseed', 'Adobe Lightroom', 'Google Photos', 'VSCO', 'TikTok', 'Snapchat', 'Instagram', 'Facebook', 'Twitter', 'Pinterest', 'LinkedIn', 'Tinder', 'Bumble', 'Grindr', 'OkCupid', 'Hinge', 'Zoosk', 'Match.com', 'eHarmony', 'Netflix', 'Hulu', 'Disney+', 'Amazon Prime Video', 'HBO Max', 'Apple TV+', 'Spotify', 'Apple Music', 'Tidal', 'YouTube Music', 'Pandora', 'SoundCloud', 'Audible', 'Kindle', 'Google Books', 'Wattpad', 'Goodreads', 'Duolingo', 'Babbel', 'Rosetta Stone', 'Google Translate', 'Microsoft Translator', 'Pocket', 'Flipboard', 'Feedly', 'BBC News', 'CNN', 'The New York Times', 'BBC iPlayer', 'TED', 'Khan Academy', 'Coursera', 'Udemy', 'LinkedIn Learning', 'Google Classroom', 'Microsoft Teams', 'Zoom', 'Skype', 'Slack', 'Microsoft Outlook', 'Gmail', 'Yahoo Mail', 'Outlook', 'Google Drive', 'Dropbox', 'OneDrive', 'Evernote', 'Microsoft OneNote', 'Notion', 'Trello', 'Wunderlist', 'Todoist', 'Asana', 'Weather', 'AccuWeather', 'The Weather Channel', 'Dark Sky', 'Google Maps', 'Waze', 'Uber', 'Lyft', 'Google Earth', 'Snapseed', 'Adobe Lightroom', 'Google Photos', 'VSCO', 'TikTok', 'Snapchat', 'Bitmoji', 'Facebook Messenger', 'WhatsApp Messenger', 'Skype', 'Hangouts', 'Viber', 'Signal', 'Telegram', 'LINE', 'Kakao']
    lowercase_apps = [app.lower() for app in apps]
    for app in lowercase_apps:
        return app
   







def open_website(url):
    try:
        webbrowser.open(url)
    except webbrowser.Error as e:
        print(f"Error opening website: {e}")
        talk("Sorry, I couldn't open the website.")


def play_Jarvis(translated_input):
    instruction = translated_input

    import spacy
    nlp = spacy.load("en_core_web_sm")
    text = instruction
    doc = nlp(text)
   
    apps = ['Facebook', 'Twitter', 'Instagram', 'LinkedIn', 'Snapchat', 'Pinterest', 'WhatsApp', 'YouTube', 'Tumblr', 'Reddit', 'Flickr', 'Vimeo', 'Periscope', 'TikTok', 'WeChat', 'Viber', 'Telegram', 'LINE', 'KakaoTalk', 'Skype', 'Google Maps', 'Waze', 'Uber', 'Lyft', 'Google Chrome', 'Safari', 'Netflix', 'Hulu', 'Disney+', 'Amazon Prime Video', 'Spotify', 'Apple Music', 'Tinder', 'Bumble', 'Grindr', 'WhatsApp', 'Telegram', 'Signal', 'Zoom', 'Microsoft Teams', 'Google Meet', 'Snapseed', 'Adobe Photoshop Express', 'Evernote', 'Microsoft Word', 'Microsoft Excel', 'Microsoft PowerPoint', 'Dropbox', 'Google Drive', 'OneDrive', 'Shazam', 'Trello', 'Wunderlist', 'Todoist', 'Weather', 'Google Photos', 'Adobe Acrobat Reader', 'Duolingo', 'Khan Academy', 'Google Translate', 'Pocket', 'Flipboard', 'Feedly', 'Kindle', 'Audible', 'WhatsApp Business', 'LinkedIn Learning', 'Twitch', 'Discord', 'Clubhouse', 'Signal', 'Cash App', 'Venmo', 'PayPal', 'Google Pay', 'Apple Pay', 'Zelle', 'Robinhood', 'Coinbase', 'DoorDash', 'Postmates', 'Instacart', 'Uber Eats', 'Grubhub', 'Waze', 'Google Earth', 'Snapchat', 'Bitmoji', 'Facebook Messenger', 'WhatsApp Messenger', 'Skype', 'Hangouts', 'Viber', 'Signal', 'Telegram', 'LINE', 'KakaoTalk', 'WeChat', 'Instagram', 'Snapseed', 'Adobe Lightroom', 'Google Photos', 'VSCO', 'TikTok', 'Snapchat', 'Instagram', 'Facebook', 'Twitter', 'Pinterest', 'LinkedIn', 'Tinder', 'Bumble', 'Grindr', 'OkCupid', 'Hinge', 'Zoosk', 'Match.com', 'eHarmony', 'Netflix', 'Hulu', 'Disney+', 'Amazon Prime Video', 'HBO Max', 'Apple TV+', 'Spotify', 'Apple Music', 'Tidal', 'YouTube Music', 'Pandora', 'SoundCloud', 'Audible', 'Kindle', 'Google Books', 'Wattpad', 'Goodreads', 'Duolingo', 'Babbel', 'Rosetta Stone', 'Google Translate', 'Microsoft Translator', 'Pocket', 'Flipboard', 'Feedly', 'BBC News', 'CNN', 'The New York Times', 'BBC iPlayer', 'TED', 'Khan Academy', 'Coursera', 'Udemy', 'LinkedIn Learning', 'Google Classroom', 'Microsoft Teams', 'Zoom', 'Skype', 'Slack', 'Microsoft Outlook', 'Gmail', 'Yahoo Mail', 'Outlook', 'Google Drive', 'Dropbox', 'OneDrive', 'Evernote', 'Microsoft OneNote', 'Notion', 'Trello', 'Wunderlist', 'Todoist', 'Asana', 'Weather', 'AccuWeather', 'The Weather Channel', 'Dark Sky', 'Google Maps', 'Waze', 'Uber', 'Lyft', 'Google Earth', 'Snapseed', 'Adobe Lightroom', 'Google Photos', 'VSCO', 'TikTok', 'Snapchat', 'Bitmoji', 'Facebook Messenger', 'WhatsApp Messenger', 'Skype', 'Hangouts', 'Viber', 'Signal', 'Telegram', 'LINE', 'Kakao']
    lowercase_apps = [app.lower() for app in apps]
    
    for token in doc:
        token=token.text.lower()
        if token in lowercase_apps:
            talk("Opening " + token)
            website_url = f"https://www.{token}.com"
           
            open_website(website_url)
       
        
        
        elif token == "play" :
        
             song = instruction.replace('Play', "")
             talk("playing" + song)
             pywhatkit.playonyt(song)

        elif token == "time" :
        
            time = datetime.datetime.now().strftime('%I:%M%p')
            talk('Current time ' + time)

        elif token=='date' :
            date = datetime.datetime.now().strftime('%d %m %Y ')
            talk("Today's date " + date)



    if token=='what is your name' :
       talk('I am Jarvis, what can I do for you?')
    elif token == 'who':
        query_start_index = instruction.find('who is') + len('who is')
        human = instruction[query_start_index:].strip()
        print("After replacement:", human)
        try:
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.PageError as e:
            print(f"PageError: {e}")
            talk("Sorry, I couldn't find information on that.")



      


           

            
   

   

    
def nepali_voice_assistant():
    talk("नमस्ते! कसरी सहायक गर्न सक्छु?")  # Translation: Hello! How can I assist you?

    while True:
        user_input = recognize_speech()

        if user_input:
            if "stop" in user_input.lower():
                talk("फेरी भेटौं!")  # Translation: Goodbye!
                break
            else:
                translated_input = translate_text(user_input, target_language='en')
                play_Jarvis(translated_input)

# ...

from gtts import gTTS
import pygame

def speak_nepali_male(text):
    # Specify the language (Hindi for a male voice)
    language = 'ne'

    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the audio file
    tts.save("output.mp3")

    # Initialize the Pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load("output.mp3")

    # Play the audio
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up (optional)
    pygame.mixer.quit()




def activation_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ne-NP')  # Recognize speech in Nepali
        if text=='हे बाबु' :
            speak_nepali_male("नमस्ते! कसरी सहायक गर्न सक्छु?")
            nepali_voice_assistant()

        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        m=translate_text("Sorry, could not understand audio.")
        speak_nepali_male(m)

        return None
       


   

  





def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ne-NP')  # Recognize speech in Nepali
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None


def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    print("Translation:",translated_text.text)
    
   
    return translated_text.text


if __name__ == "__main__":
    nepali_voice_assistant()
