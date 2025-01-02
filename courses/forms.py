from django.forms.models import inlineformset_factory
from .models import Course, Lecture


LectureFormSet = inlineformset_factory(
    Course,
    Lecture,
    fields=['title', 'description'],
    extra=2,
    can_delete=True
)