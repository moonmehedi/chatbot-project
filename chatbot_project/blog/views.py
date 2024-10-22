from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import spacy

# Create your views here
# Load the spaCy model


bot=ChatBot('chatbot',read_only=False,logic_adapters=[{
    'import_path':'chatterbot.logic.BestMatch',
    'default_response':'I am sorry, but I do not understand.',
   
    }])

list_to_train=[
    "hi",
    "hi,there",
    "what's your name?",
    "I'm a chatbot",
    "what is your fav food?",
    "i like cheese",
    'Hi how are you?',
    'I am doing well.',
]



ChatterBotCorpusTrainer=ChatterBotCorpusTrainer(bot)
ChatterBotCorpusTrainer.train('chatterbot.corpus.english')


list_trainer=ListTrainer(bot)
list_trainer.train(list_to_train)




def index(req):
    return render(req,'index.html')

    

@csrf_exempt  # Temporarily exempt from CSRF for testing purposes (not recommended for production)
def getResponse(request):
        
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            message=data.get('message','')
            print('Received message:',message)
            
            botres=str(bot.get_response(message))
            return JsonResponse({'message':botres})
        except json.JSONDecodeError:
            return JsonResponse({'error':'Invalid JSON'},status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
