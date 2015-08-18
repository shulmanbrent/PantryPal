import os
import sys
sys.path.insert(0, '..')
from collections import defaultdict, Counter
from PantryPal_app.models import Query
from gensim.models import Word2Vec
import requests
from bs4 import BeautifulSoup
from django.core.mail import send_mail


def send_emails():

    queries = Query.objects.all()[16:18]

    def get_syn(*args):
        BASE = "http://irsrv2.cs.biu.ac.il:9998/?word="
        synonyms = list()
        for word in args[0]:
            rq = requests.get(BASE + word)
            soup = BeautifulSoup(rq.text)
            synonyms += [s.text for s in soup.findAll('a')[:3]]
        return synonyms

    ## How do I get the 3 most recent queries?? ##
    by_user = defaultdict(Counter)
    for q in queries:
        for word in q.query.split():
            by_user[q.user_email].update([word])

    synonyms = dict()
    for user_email, words in by_user.items():
        synonyms[user_email] = get_syn([w for w, count in words.most_common(3)])

        send_mail('Your synonyms', str(synonyms[user_email]), 'shulmanbrent@gmail.com', [
                  user_email], fail_silently=False)

    return synonyms
