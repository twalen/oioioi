from django.db import models
from django.utils.translation import ugettext_lazy as _

from oioioi.base.utils.deps import check_django_app_dependencies
from oioioi.contests.models import ProblemInstance
from oioioi.submitsqueue.models import submission_states


check_django_app_dependencies(__name__, ['oioioi.submitsqueue'], strict=True)

submission_states.register('SUSPENDED', _("Suspended"))


class SuspendedProblem(models.Model):
    problem_instance = models.OneToOneField(ProblemInstance,
                                            related_name='suspended')
    suspend_init_tests = models.BooleanField(default=True)