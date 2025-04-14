from django.contrib import admin
from .models import lessonplanBatch,courseoutcomes,textbooks,referencebooks,targetproficiency,lectureplan,co_pso_Matrix,course_end_survey,details_of_instructors,teachers
# Register your models here.
# from dynamic_models.models import ModelSchema, FieldSchema
admin.site.register(lessonplanBatch)
admin.site.register(courseoutcomes)
admin.site.register(textbooks)
admin.site.register(referencebooks)
admin.site.register(targetproficiency)
admin.site.register(lectureplan)
admin.site.register(co_pso_Matrix)
admin.site.register(course_end_survey)
admin.site.register(details_of_instructors)
admin.site.register(teachers)
# admin.site.register(ModelSchema)
# admin.site.register(FieldSchema)