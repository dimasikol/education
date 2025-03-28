class Task7():
    def __init__(self):
        self.data = DATA['seven']
        self.text = self.data['address']
        self.protokol = random.choice(self.text['protokol'])
        self.address = [random.choice(self.text['domain']), random.choice(self.text['second_level_domain']),
                        random.choice(self.text['top_level_domain'])]
        self.path = random.choice(self.text['path'])
        self.file_type = random.choice(self.text['file_type'][random.choice(['photo', 'media', 'text', 'video'])])
        self.file_name = random.choice(self.text['file_name'])
        self.decision = f'{self.protokol}://{self.address[0]}.{self.address[1]}.{self.address[2]}/{self.path}/{self.file_name}.{self.file_type}'
        self.randomize_answer = (
        self.protokol, "://", "/", '.', self.address[0], self.address[1], self.address[2], self.path, self.file_name,
        self.file_type,"@")
        self.alf = list('АБВГДЕЁЖЗИКЛМНОПРСТ')[:13]
        random.shuffle(self.alf)
        self.answer_tuple = sorted(list(zip(self.alf, self.randomize_answer)))
        self.answer_dict = {v: k for k, v in dict(self.answer_tuple).items()}| {k: v for k, v in dict(self.answer_tuple).items()}

        self.answer = self.answer_dict[self.protokol] + self.answer_dict['://'] + self.answer_dict[self.address[0]] + \
                      self.answer_dict["."] + self.answer_dict[self.address[1]] + self.answer_dict["."] + \
                      self.answer_dict[self.address[2]] + self.answer_dict["/"] + self.answer_dict[self.path] + \
                      self.answer_dict["/"] + self.answer_dict[self.file_name] + self.answer_dict["."] + \
                      self.answer_dict[self.file_type]
        self.answer_quiz = '<br>' + ''.join(list(map(lambda x: f'{x[0]}) {x[1]}<br>', self.answer_tuple)))
        self._write()

    def _write(self):
        type =4
        if type==1:
            self.quiz = f"{self.data['text1']} {self.file_name}.{self.file_type} {self.data['text2']} {self.address[1]}.{self.address[2]} в директории {self.path} поддомена {self.address[0]} {self.data['text3']} {self.protokol} {self.data['text4']} {self.answer_quiz}"
        elif type == 2:
            self.quiz = f"{self.data['text1']} {self.file_name}.{self.file_type} {self.data['text2']} {self.address[1]}.{self.address[2]} в директории {self.path} поддиректории {self.address[0]} {self.data['text3']} {self.protokol} {self.data['text4']} {self.answer_quiz}"
            self.answer = self.answer_dict[self.protokol] + self.answer_dict['://'] + self.answer_dict[self.address[0]] + self.answer_dict["."] + \
                          self.answer_dict[self.address[2]] + self.answer_dict["/"]+self.answer_dict[self.address[1]] +self.answer_dict["/"]+ self.answer_dict[self.path] + \
                          self.answer_dict["/"] + self.answer_dict[self.file_name] + self.answer_dict["."] + \
                          self.answer_dict[self.file_type]
            self.decision = f'{self.protokol}://{self.address[1]}.{self.address[2]}/{self.address[0]}/{self.path}/{self.file_name}.{self.file_type}'
        elif type==3:
            self.quiz = f"{self.data['text1']} {self.data['text2']} {self.address[1]}.{self.address[2]} в директории {self.path} поддиректории {self.address[0]} {self.data['text3']} {self.protokol} Определите наименование файла и запишите последовательность этих букв, кодирующую адрес фала в сети Интернет. {self.answer_quiz}"
            self.answer = self.answer_dict[self.protokol] + self.answer_dict['://'] + self.answer_dict[self.address[0]] + self.answer_dict["."] + \
                          self.answer_dict[self.address[2]] + self.answer_dict["/"]+self.answer_dict[self.address[1]] +self.answer_dict["/"]+ self.answer_dict[self.path] + \
                          self.answer_dict["/"] + self.answer_dict[self.file_name] + self.answer_dict["."] + \
                          self.answer_dict[self.file_type]
            self.decision = f'{self.protokol}://{self.address[1]}.{self.address[2]}/{self.address[0]}/{self.path}/{self.file_name}.{self.file_type}'
        elif type == 4:
            self.login = random.choice(DATA['logins'])
            self.answer_dict[self.login] = 'Т'
            self.quiz = f'На сервере {self.address[1]} находится почтовый ящик {self.login}. Восстановите адрес электронной почты если доменн вернего уровня {self.address[2]}.'
            self.decision = f"{self.login}@{self.address[1]}.{self.address[2]}"
            self.answer = self.answer_dict[self.login]+self.answer_dict['@']+self.answer_dict[self.address[0]]+self.answer_dict["."]+self.answer_dict[self.address[2]]
            self.answer_quiz = '<br>' + ''.join(list(map(lambda x: f'{x[0]}) {x[1]}<br>', self.answer_tuple)))

            print()
    def _write3(self):
        self.quiz = 'составьте ip адресс из предложенных цифр'
