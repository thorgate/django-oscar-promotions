from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PromotionsDashboardConfig(AppConfig):
    label = 'oscar_promotions.dashboard'
    name = 'oscar_promotions.dashboard'
    verbose_name = _('Promotions dashboard')
