import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'baizhi_book.settings'
if __name__ == '__main__':
    send_mail('这是邮件的标题',
              '这是邮件的内容！',
              'yintiannong@sina.com',
              ['1532295578@qq.com'])