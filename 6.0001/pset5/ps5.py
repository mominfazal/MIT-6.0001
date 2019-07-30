# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
from time import mktime
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

def remove_punctuation(phrase):
    """ Accepts string and returns list of words in order"""
    phrase = phrase.lower()
    # remove all punctuation first
    for punctuation in string.punctuation:
        if punctuation in phrase:
            phrase = phrase.replace(punctuation, " ")
    # check if after removing punctuation
    # words are available in actual phrase in sequence
    return [each for each in phrase.split(" ") if len(each) > 0]
#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory


class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        """ get guid """
        return self.guid

    def get_title(self):
        """ get title """
        return self.title

    def get_description(self):
        """ get description """
        return self.description

    def get_link(self):
        """ get link """
        return self.link

    def get_pubdate(self):
        """ get pubdate """
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    """ PhraseTrigger class inherited from Trigger abstract class """

    def __init__(self, phrase):
        """
        Constructor
        """
        Trigger.__init__(self)
        self.phrase = phrase.lower() # Its specified in document

    def is_phrase_in(self, text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')
        word_list = text.split(' ')
        while '' in word_list:
            word_list.remove('')
        phrase_split = self.phrase.split()
        test = []
        for ph in phrase_split:
            for i, word in enumerate(word_list):
                if ph == word:
                    test.append(i)
        found = True
        if len(test) < len(phrase_split):
            return False
        for i in range(len(test) - 1):
            if test[i + 1] - test[i] != 1:
                found = False
        return found
    # def is_phrase_in(self, check_phrase):
    #     """ Takes in one string argument text.
    #         It returns ​True​
    #         if the whole phrase is present in text,
    #         False​ otherwise
    #     """
        # check_phrase = remove_punctuation(check_phrase)
        # phrase = remove_punctuation(self.phrase)

        # # maintaing indexes so that we can check if words exists together
        # indexes_list = []
        # for i, word in enumerate(check_phrase):
        #     for each_word in phrase:
        #         if each_word == word:
        #             indexes_list.append(i)

        # count_consequtive = 1
        # for i in range(0, len(indexes_list)):
        #     # If phrase length is 3 then
        #     # there should be 3 consequitive numbers in
        #     # indexes_list
        #     if i <= len(indexes_list)-2:
        #         if indexes_list[i]+1 == indexes_list[i+1]:
        #             count_consequtive += 1

        # if count_consequtive >= len(phrase) or count_consequtive == len(phrase):
        #     return True
        # else:
        #     return False


    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# Problem 3
class TitleTrigger(PhraseTrigger):
    """ TitleTrigger class implements PhraseTrigger """
    def __init__(self, phrase):
        """
        Constructor
        """
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    """ DescriptionTrigger class implements PhraseTrigger """
    def __init__(self, phrase):
        """
        Constructor
        """
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS


# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, string_time):
        Trigger.__init__(self)
        try:
            self.pubtime = datetime.fromtimestamp(mktime(time.strptime(
                string_time, "%d %b %Y %H:%M:%S"))).replace(tzinfo=pytz.timezone("EST"))
        except:
            raise Exception("Time to string conversion failed")

# Problem 6

class BeforeTrigger(TimeTrigger):
    def __init__(self, string_time):
        TimeTrigger.__init__(self, string_time)

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.pubtime > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    def __init__(self, string_time):
        TimeTrigger.__init__(self, string_time)

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.pubtime <= story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    """ NotTrigger """
    def __init__(self, trigger):
        Trigger.__init__(self)
        self.trigger = trigger

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return not self.trigger.evaluate(story)
# Problem 8
class AndTrigger(Trigger):
    """ AndTrigger """
    def __init__(self, trigger1, trigger2):
        Trigger.__init__(self)
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9

class OrTrigger(Trigger):
    """ OrTrigger """

    def __init__(self, trigger1, trigger2):
        Trigger.__init__(self)
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    trigger_stories = []
    for eachstory in stories:  # stories is a list of NewsStory class instances
        for trigger in triggerlist:
            # triggerlist is a list of trigger
            # class instances, it can be title,
            # description etc type of triggers
            print("-------")
            print(trigger)
            print("evaluate" in dir(trigger))
            print(type(trigger))
            if trigger.evaluate(eachstory):
                trigger_stories.append(eachstory)

    return trigger_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    final = []
    final_dict={}
    for line in lines:
        splitted_line = line.split(',')
        if splitted_line[1] == 'TITLE':
            final.append(TitleTrigger(splitted_line[2]))
            final_dict[splitted_line[0]] = TitleTrigger(splitted_line[2])

        elif splitted_line[1] == 'DESCRIPTION':
            final.append(DescriptionTrigger(splitted_line[2]))
            final_dict[splitted_line[0]] = DescriptionTrigger(splitted_line[2])

        elif splitted_line[1] == 'AFTER':
            final.append(AfterTrigger(splitted_line[2]))
            final_dict[splitted_line[0]] = AfterTrigger(splitted_line[2])

        elif splitted_line[1] == 'BEFORE':
            final.append(BeforeTrigger(splitted_line[2]))
            final_dict[splitted_line[0]] = BeforeTrigger(splitted_line[2])

        elif splitted_line[1] == 'AND':
            final.append(AndTrigger(final_dict[splitted_line[2]], final_dict[splitted_line[3]]))
            final_dict[splitted_line[0]] = AndTrigger(
                final_dict[splitted_line[2]], final_dict[splitted_line[3]])

        elif splitted_line[1] == 'OR':
            final.append(OrTrigger(final_dict[splitted_line[2]], final_dict[splitted_line[3]]))
            final_dict[splitted_line[0]] = OrTrigger(
                final_dict[splitted_line[2]], final_dict[splitted_line[3]])

        elif splitted_line[1] == 'NOT':
            final.append(NotTrigger(splitted_line[2]))
            final_dict[splitted_line[0]] = NotTrigger(splitted_line[2])

    return final



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
