from django.db import models

# Create your models here.

class Personal:
    description = """
    Hey! I'm Adrian.
    I am a student of Computational Linguistics and Computer Science in Munich.
    This is my personal website. I created it just for fun.
    """.strip()

    interest_title = """
    These are my main fields of interest:
    """.strip()

    interests = {"Quantum Computing": "oil_quantum.png",
                 "Natural Language Processing": "oil_ai.png",
                 "Free and Open-Source Software": "oil_foss.png"}

    contact_text = "Contact me if you like!"
