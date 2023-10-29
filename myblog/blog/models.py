from django.db import models

class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок поста', max_length=100)
    description = models.TextField('Текст поста')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comments(models.Model):
    '''Комментарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
