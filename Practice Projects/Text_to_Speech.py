import win32com.client as wincl

spk = wincl.Dispatch("SAPI.SpVoice")

def convertToSpeech(speaker, text):
    speaker_number = speaker - 1

    print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
    spk.Voice
    spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)

    spk.Speak(f"Hello, {text}. Nice to see you!")


if __name__ == "__main__":
    print("text to speech".upper().center(100))

    # Get List of All available voices
    print("Select Voice Type:-")
    vcs = spk.GetVoices()

    for i in range(vcs.Count):
        print(f"{i+1}: {vcs.Item(i).GetAttribute('Name')}")
    
    speaker = int(input("\nEnter Choice of Speaker: "))

    # name = input("Enter Your Name: ")

    names = ["Aman", "John", "Tom", "Tony", "Chris", "Juilee", "Katherine"]

    for name in names:
        convertToSpeech(speaker, name)
