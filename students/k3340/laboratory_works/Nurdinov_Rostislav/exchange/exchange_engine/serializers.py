from rest_framework import serializers
from .models import JobSeeker, Vacancy, Resume, Experience, Profession, Employer


class ResumeDetailSerializer(serializers.ModelSerializer):
    """Резюме"""

    class Meta:
        model = Resume
        fields = "__all__"


class JobSeekerListSerializer(serializers.ModelSerializer):
    """Список соискателей"""

    class Meta:
        model = JobSeeker
        fields = '__all__'


class JobSeekerDetailSerializer(serializers.ModelSerializer):
    """Соискатель"""
    # resume = ResumeDetailSerializer()

    class Meta:
        model = JobSeeker
        fields = "__all__"


class JobSeekerCreateSerializer(serializers.ModelSerializer):
    """Добавление соискателя"""

    class Meta:
        model = JobSeeker
        fields = '__all__'


class VacancyListSerializer(serializers.ModelSerializer):
    """Списов активных вакансий"""

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)

    class Meta:
        model = Vacancy
        fields = ("id", "profession", "date_start", "salary", "min_exp", "status")


class VacancyCreateSerializer(serializers.ModelSerializer):
    """Создание вакансии"""

    RANK_TYPES = [
        ('1', '1 разряд'),
        ('2', '2 разряд'),
        ('3', '3 разряд'),
    ]

    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)
    # education = serializers.SlugRelatedField(slug_field='education', read_only=True)
    employer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    rank = serializers.ChoiceField(choices=RANK_TYPES, source='get_rank_display')
    education = serializers.ChoiceField(choices=EDUCATION_TYPES, source='get_education_display')

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyDetailSerializer(serializers.ModelSerializer):
    """Вакансия"""
    RANK_TYPES = [
        ('1', '1 разряд'),
        ('2', '2 разряд'),
        ('3', '3 разряд'),
    ]

    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)
    # education = serializers.SlugRelatedField(slug_field='education', read_only=True)
    employer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    rank = serializers.ChoiceField(choices=RANK_TYPES, source='get_rank_display')
    education = serializers.ChoiceField(choices=EDUCATION_TYPES, source='get_education_display')

    class Meta:
        model = Vacancy
        fields = "__all__"


class ProfessionListSerializer(serializers.ModelSerializer):
    """Список профессий"""

    class Meta:
        model = Profession
        fields = '__all__'


class ProfessionCreateSerializer(serializers.ModelSerializer):
    """Добавление профессии"""

    class Meta:
        model = Profession
        fields = '__all__'


class ProfessionDetailSerializer(serializers.ModelSerializer):
    """Профессия"""

    class Meta:
        model = Profession
        fields = '__all__'


class EmployerListSerializer(serializers.ModelSerializer):
    """Список работодателей"""

    class Meta:
        model = Employer
        fields = ("id", "name", "surname", "second_name", "firm")


class EmployerCreateSerializer(serializers.ModelSerializer):
    """Добавление работодателей"""

    class Meta:
        model = Employer
        fields = "__all__"


class EmployerDetailSerializer(serializers.ModelSerializer):
    """Работодатель"""

    class Meta:
        model = Employer
        fields = "__all__"


class ExperienceListSerializer(serializers.ModelSerializer):
    """Список опытов работы"""
    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class ExperienceCreateSerializer(serializers.ModelSerializer):
    """Добавление опыта работы"""
    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class ExperienceDetailSerializer(serializers.ModelSerializer):
    """Опыт работы"""
    EDUCATION_TYPES = [
        ('1', 'Среднее общее'),
        ('2', 'Профессиональное'),
        ('3', 'Высшее (бакалавриат)'),
        ('4', 'Высшее (магистратура)'),
    ]

    profession = serializers.SlugRelatedField(slug_field='prof', read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


