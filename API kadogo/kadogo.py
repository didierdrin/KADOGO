# Kadogo KINYA reply bot application
import re
import requests

class Kadogo:
    _dict_file = "data.txt"
    dictionary = {}
    json_return = {}
    question = ""
    answer = ""
    #audio = ""
    is_command = False

    def __init__(self):
        self.json_return.clear()
        self.question = ""
        self.answer = ""
        #self.audio = ""
        self.is_command = False
        self.dictionary = {}
        self.dictionary = self.load_dictionary()

    def api(self, query):
        self.question = str(query).strip()
        ans = self.answering()
        #self.audio = re.sub("", "_", self.question)
        #self.json_return['audio'] = self.audio
        self.json_return['answer'] = ans
        self.json_return['is_command'] = self.is_command

        return self.json_return

    def answering(self):
        # command should be used for specific task request
        command = str(self.question.strip().split(" ")[0])
        if self.question in self.dictionary.keys():
            res = self.dictionary.get(self.question)
        
        else:
            # self.audio = "Ntago mbyumvise"
            res = "Ntago mbyumvise"
        return res

    def load_dictionary(self):
        res = {}
        infile = open(self._dict_file, 'r')
        contents = infile.readlines()
        for item in contents:
            separate = item.strip().split("-")
            question = separate[:1]
            answer = separate[1:]
            # Lists for question and answer formed 
            for question_item, answer_item in zip(question, answer):
                res[question_item.strip()] = answer_item.strip()
        
        return res




