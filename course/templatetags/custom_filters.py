from django import template

register = template.Library()

@register.filter
def is_course_paid_for(course_pk, paid_course_ids):
    return course_pk in paid_course_ids
