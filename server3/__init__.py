import random 
import string 
import azure.functions as func

letters =string.ascii_lowercase 

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("".join(random.choice(letters) for i in range(5)))
