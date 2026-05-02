from rest_framework import serializers
from .models import Question, TestResult


class AnswerItemSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer = serializers.CharField(max_length=20)


class SubmitTestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, allow_blank=True, required=False)
    answers = AnswerItemSerializer(many=True)

    def validate_answers(self, value):
        if len(value) != 20:
            raise serializers.ValidationError('Iltimos, 20 ta savolga ham javob bering.')
        return value


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_number', 'text', 'temperament']


class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = [
            'id',
            'name',
            'sangvinik_score',
            'xolerik_score',
            'flegmatik_score',
            'melanxolik_score',
            'dominant_temperament',
            'created_at',
        ]
