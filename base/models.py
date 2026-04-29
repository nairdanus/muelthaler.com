from django.db import models
from dataclasses import dataclass, field
from django.conf import settings


@dataclass
class Project:
    title: str
    abstract: str
    subtitle: Optional[str] = None
    image: Optional[str] = None
    link: Optional[str] = None
 
 

PROJECTS = [
    Project(
        title="Quantum Computing vs. Firewalls: When Complexity Saves the Horizon",
        subtitle="Seminar Paper",
        abstract="The black hole firewall paradox, proposed by Almheiri, Marolf, Polchinski, and Sully, exposes a fundamental tension between the principles of quantum mechanics and the classical description of black hole event horizons. In response, Harlow and Hayden argued that limitations arising from quantum computational complexity render the firewall paradox thought experiment operationally unrealizable, thereby offering a potential resolution of the paradox. This seminar paper is a pedagogical review and synthesis of these ideas rather than a presentation of new results, providing a clear and accessible introduction to the firewall paradox and the Harlow–Hayden complexity argument. The paper is aimed at readers with a background in quantum computing but limited familiarity with black hole physics.",
        image="QCvsFire.png",
        link="https://bib.nm.ifi.lmu.de/pdf/semQC25proceedings.pdf#chapter.1",
    ),
    Project(
        title="Using LLMs and Preference Optimization for Agreement-Aware HateWiC Classification",
        subtitle="WOAH, ACL 2025",
        abstract="Annotator disagreement poses a significant challenge in subjective tasks like hate speech detection. In this paper, we introduce a novel variant of the HateWiC task that explicitly models annotator agreement by estimating the proportion of annotators who classify the meaning of a term as hateful. To tackle this challenge, we explore the use of Llama 3 models fine-tuned through Direct Preference Optimization (DPO). Our experiments show that while LLMs perform well for majority-based hate classification, they struggle with the more complex agreement-aware task. DPO fine-tuning offers improvements, particularly when applied to instruction-tuned models.",
        image="hateWIC.png",
        link="https://aclanthology.org/2025.woah-1.47/",
    ),
    Project(
        title="Simulating Circuits in Quantum Natural Language Processing using Tensor Networks",
        subtitle="Bachelor's Thesis",
        abstract="Quantum natural language processing deals with the implementation of natural language models on quantum hardware. It remains uncertain whether these models benefit from a quantum advantage or can be efficiently simulated on classical hardware. Tensor networks emerge as a promising tool in the efficient approximation of quantum states. This thesis explores the feasibility and potential advantages of employing tensor network simulation for quantum natural language processing. Using a matrix product state architecture, we investigate the complexity of simulating circuits obtained from the Categorical Compositional Distributional framework.",
        image="BA.png",
        link="https://bib.nm.ifi.lmu.de/pdf/muel24.pdf",
    ),
    Project(
        title="A Recurrent Depth Approach to Latent Reasoning",
        subtitle="Seminar Paper",
        abstract="This seminar paper examines how LLMs can be improved in their reasoning abilities by comparing two paradigms: explicit reasoning through Chain-of-Thought (CoT) and latent reasoning. CoT enables interpretability by making intermediate steps explicit, but it is computationally costly and limited to reasoning that can be verbalized. Latent reasoning, in contrast, operates entirely within hidden states, offering greater efficiency and flexibility but less transparency. A particular focus is placed on the recurrent depth approach, which introduces recurrence into transformer architectures. This method allows iterative refinement of internal representations and shows promising results in domains such as mathematics and coding, achieving competitive performance with fewer parameters.",
        image="fmf_seminar.png",
        link="/static/fmf_seminar.pdf",
    ),

]
 


class Personal:
    description = """
    Hey! I'm Adrian.
    I am a student of Computational Linguistics and Computer Science in Munich.
    Welcome to my personal website!
    """.strip()

    interest_title = """
    These are my main fields of interest:
    """.strip()

    interests = {"Quantum Computing": "oil_quantum.png",
                 "Natural Language Processing": "oil_ai.png",
                 "Free and Open-Source Software": "oil_foss.png"}

    contact_text = "Contact me if you like!"
