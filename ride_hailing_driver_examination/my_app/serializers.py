from django.core.serializers import serialize

def serialize_questions(questions):
    return serialize('json', questions)
