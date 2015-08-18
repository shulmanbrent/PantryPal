import os
import sys
sys.path.insert(0, '..')
from collections import defaultdict, Counter
from PantryPal_app.models import Query
from PantryPal_app.run_query import run_query
# from gensim.models import Word2Vec
import requests
from bs4 import BeautifulSoup
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def send_emails():

    queries = Query.objects.all()

    def get_syn(*args):
        BASE = "http://irsrv2.cs.biu.ac.il:9998/?word="
        synonyms = list()
        for word in args[0]:
            rq = requests.get(BASE + word)
            soup = BeautifulSoup(rq.text)
            synonyms += [s.text for s in soup.findAll('a')[:1] if s.text != "CherryPy 3.2.4"]
        return synonyms

    ## How do I get the 3 most recent queries?? ##
    by_user = defaultdict(Counter)
    for q in queries:
        for word in q.query.split():
            by_user[q.user_email].update([word])

    synonyms = dict()
    for user_email, words in by_user.items():
        synonyms[user_email] = get_syn([w for w, count in words.most_common(3)])
        similar_recipes = run_query(' '.join(synonyms[user_email]), '', 1)
        template = get_template('mail/email_message.html')
        context = Context({'result_list': similar_recipes})
        content = template.render(context)
        msg = EmailMessage('PantryPal!', content, 'shulmanbrent@gmail.com', [user_email])
        msg.content_subtype = 'html'
        msg.send()

    return synonyms
