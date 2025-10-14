"""
tts handler: part of pyagt library
"""

from accessible_output2 import outputs

class TTS:
    """tts handler"""
    def __init__(self) -> None:
        """
        initialize tts object
        """
        self.reader = outputs.auto.Auto()
        self.interruptible = True

    def set_screen_reader(self, reader) -> None:
        """
select screen reader for tts output, default is auto detect    
args:
reader()
returns:
None
"""
        self.reader = reader

    def speak(self, text: str) -> None:
        """
        args:
        text(str)
        """
        if not self.reader:
            raise RuntimeError("screen reader not initialized")
        self.reader.speak(text, interrupt=self.interruptible)
        return

    def interrupt(self):
        """manualy interrupt the tts speech"""
        if not self.reader:
            raise RuntimeError("screen reader not initialized")
        self.reader.speak("", interrupt=True)
