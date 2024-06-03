from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Salary
from salaryanalytics.utils import send_telegram_message


@receiver(post_save, sender=Salary)
def check_salary_change(sender, instance, **kwargs):
    if kwargs.get('created', False):
        return

    try:
        old_instance = Salary.objects.get(pk=instance.pk)
        if old_instance.amount != instance.amount:
            percentage_change = instance.get_percentage_change(old_instance.amount)
            if abs(percentage_change) > 10:
                message = f"Зарплата за {instance.year} изменилась на {percentage_change:.2f}%."
                send_telegram_message(message)
    except Salary.DoesNotExist:
        pass
