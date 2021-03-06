from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_first_last_name(self):
    return self.first_name + ' ' + self.last_name


User.add_to_class("__str__", get_first_last_name)


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание вопроса")
    additional_information = models.TextField(
        verbose_name="Дополнительная информация для пользователя после отправки ответа.")
    is_input_question = models.BooleanField(
        verbose_name="Отметьте, если ответ на этот вопрос пользователь вводит сам, а не выбирает из «ответов». Потом вам придётся самому выбрать, правильно ли ответил пользователь на вопрос или нет.")
    image_url = models.CharField(blank=False, max_length=200, verbose_name="Ссылка на фото",
                                 help_text="Загрузите на imgur.com и правым кликом по фото нажмите 'Копировать ссылку на изображение'. Вставьте ссылку. Пример: https://i.imgur.com/sRjy27f.jpg")
    video_yt_url = models.CharField(blank=True, max_length=200, verbose_name="Ссылка на видео",
                                    help_text="Вставьте идентификатор видео с YouTube. Пример: vX3fXef2F4M")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Вопрос создан")

    class Meta:
        ordering = ['-created']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.CharField(max_length=1000, verbose_name="Текст ответа")
    correct = models.BooleanField(default=False, verbose_name="Правильный?",
                                  help_text="Выберите 1 правильный ответ для 1 вопроса")
    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.text


class Result(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    is_correct = models.BooleanField(null=True, default=None, verbose_name="Правильно ответил?")
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name="Ответ пользователя", blank=True,
                               null=True)
    time_result_done = models.DateTimeField(verbose_name="Когда прошёл тест? (UTC+5)", auto_now_add=True, blank=True,
                                            null=True)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
        unique_together = (
            'question',
            'user',
        )

    def __str__(self):
        return f"{self.question}"


class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.CharField(max_length=600, verbose_name="Описание квеста")
    image_url = models.CharField(blank=False, max_length=200, verbose_name="Ссылка на фото",
                                 help_text="Загрузите на imgur.com и правым кликом по фото нажмите 'Копировать ссылку на изображение'. Вставьте ссылку. Пример: https://i.imgur.com/sRjy27f.jpg")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Квест создан")
    question = models.ManyToManyField(Question, verbose_name="Вопрос")

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'

    def __str__(self):
        return self.title
