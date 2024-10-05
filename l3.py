from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class SMSNotification(Notification):
    def send(self, message):
        print(f'отправка sms: {message}')


class EmailNotification(Notification):
    def send(self, message):
        print(f'отправка email: {message}')


class PushNotification(Notification):
    def send(self, message):
        print(f'отправка push уведомления: {message}')


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == 'sms':
            return SMSNotification()

        elif notification_type == 'email':
            return EmailNotification()

        elif notification_type == 'push':
            return PushNotification()

        else:
            raise ValueError(f'неизвестный тип уведомления: {notification_type}')


factory = NotificationFactory()

sms_notification = factory.create_notification('sms')
sms_notification.send('ваш код подтверждения: 123456')

email_notification = factory.create_notification('email')
email_notification.send('вы получили новое письмо!')

push_notification = factory.create_notification('push')
push_notification.send('ваш заказ доставлен!')
