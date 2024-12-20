from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):

    number_of_lessons_in_the_course = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_number_of_lessons_in_the_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'number_of_lessons_in_the_course', 'lessons')


