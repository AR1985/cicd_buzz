#Python3
#https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjY5ZWQ1N2Y0MjQ0OTEyODJhMTgwMjBmZDU4NTk1NGI3MGJiNDVhZTAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2MjA2NTgwMTgsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNTkzOTYyNjU4MDU4MDkxOTE5OSIsImVtYWlsIjoiYWxleC5yYW5raW4xQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJuYW1lIjoiQSBSIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBVFhBSnk1Rm9ZVUZkLWpYNzd5YjJsS1VLZkljM2RSWUQ3a0FRQnJtOUE5PXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkEiLCJmYW1pbHlfbmFtZSI6IlIiLCJpYXQiOjE2MjA2NTgzMTgsImV4cCI6MTYyMDY2MTkxOCwianRpIjoiZTI3ZjM4OGFhYTNmNWY5MDUyMmM5YTdlMzNmMzEzN2ZhOWFhYWFkYSJ9.apirjOAQu_pdpsBGPWjTB6JExv0rUnz8FHj84fCbneLtSzhDHuuriy7NyxHbn7jFJIY8AAsCm5HYCg141fa-6qiUAWz6MCdBSA4qqJEQeNCOoeFGgs9h80k0Lqockj72IbcHSpgXsUwkunmFyBRh0ZMTDLb5ks9H1gb9nJO5s3eWOitSY3lcV8-z80YYn61uKeJjV6cI_OtzatXMW4os9YD2kB6b_WxHT4WEOIRXHJPrsafP9A_zjgE3UP-E0JgUvd0S3fhk27lqAYza2U6srDXaUdKFAKZ3o3ahpFr8z7bIu5bxbTvgAwh8WVeXaQ-DTg8ns8TA5AZQMHMbUwoJfA
"""Generate a statement of buzzwords to practice CI_CD"""

from __future__ import print_function
import random

buzzwords = ('continuous testing', 'continuous integration',
    'continuous deployment', 'continuous improvement', 'devops')

adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')

adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
    'seriously')

verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')

def sample(l, n = 1):
    result = random.sample(l, n)

    if n == 1:
        return result[0]
    return result


def generate_buzz():
    buzz_terms = sample(buzzwords, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()


if __name__ == "__main__":
    print(generate_buzz())
