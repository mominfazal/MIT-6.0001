import string

class Trigger():
    """ Trigger Interface """
    def __init__(self):
        pass

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

class PhraseTrigger(Trigger):
    """ PhraseTrigger class inherited from Trigger abstract class """

    def __init__(self, phrase):
        """
        Constructor
        """
        Trigger.__init__(self)
        self.phrase = phrase

    def is_phrase_in(self, phrase):
        """ Takes in one string argument text.
            It returns ​True​
            if the whole phrasephrase​ is present in text,
            False​ otherwise
        """
        return True
