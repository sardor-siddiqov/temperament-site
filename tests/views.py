from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, AnswerOption, TestResult
from .serializers import QuestionSerializer, SubmitTestSerializer, TestResultSerializer


TEMPERAMENT_ORDER = ['Sangvinik', 'Xolerik', 'Flegmatik', 'Melanxolik']
ANSWER_SCORE = {
    'Ha': 2,
    'Ba’zan': 1,
    "Ba'zan": 1,
    'Yo‘q': 0,
    "Yo'q": 0,
}

DESCRIPTIONS = {
    'Sangvinik': 'Siz ochiqko‘ngil, faol va odamlar bilan tez chiqishib ketasiz.',
    'Xolerik': 'Siz qat’iyatli, jasur va tez qaror qabul qiladigan insonsiz.',
    'Flegmatik': 'Siz barqaror, sabrli va tinchlikni afzal ko‘radigan odamnisiz.',
    'Melanxolik': 'Siz chuqur o‘ylovchi, nozik hissiyotli va tafakkurli shaxsnisiz.',
}


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SubmitTestAPIView(APIView):
    def post(self, request):
        serializer = SubmitTestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        questions = Question.objects.in_bulk([item['question_id'] for item in data['answers']])
        if len(questions) != 20:
            return Response(
                {'error': 'Savollar ro‘yxati noto‘g‘ri yoki barcha savollar topilmadi.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        scores = {key: 0 for key in TEMPERAMENT_ORDER}
        for answer_item in data['answers']:
            question = questions.get(answer_item['question_id'])
            if question is None:
                return Response(
                    {'error': f"Savol {answer_item['question_id']} topilmadi."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            answer_text = answer_item['answer']
            if answer_text not in ANSWER_SCORE:
                return Response(
                    {'error': f"Noto‘g‘ri javob varianti: {answer_text}."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            score = ANSWER_SCORE[answer_text]
            scores[question.temperament] += score

        dominant = max(TEMPERAMENT_ORDER, key=lambda key: (scores[key], -TEMPERAMENT_ORDER.index(key)))
        result = TestResult.objects.create(
            name=data.get('name', '').strip() or None,
            sangvinik_score=scores['Sangvinik'],
            xolerik_score=scores['Xolerik'],
            flegmatik_score=scores['Flegmatik'],
            melanxolik_score=scores['Melanxolik'],
            dominant_temperament=dominant,
        )

        response_data = {
            'dominant_temperament': dominant,
            'scores': {
                'Sangvinik': scores['Sangvinik'],
                'Xolerik': scores['Xolerik'],
                'Flegmatik': scores['Flegmatik'],
                'Melanxolik': scores['Melanxolik'],
            },
            'description': DESCRIPTIONS.get(dominant, ''),
            'result_id': result.id,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class TestResultListAPIView(generics.ListAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
