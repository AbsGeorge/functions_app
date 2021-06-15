import requests  
import random 
import azure.functions as func

from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = ""
key = ''

client = CosmosClient(endpoint, key)

database_name = 'RandUsernameDatabase'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'RandomUsernameContainer'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/username"),
    offer_throughput=400
)



def main(req: func.HttpRequest) -> func.HttpResponse:

    alpha = requests.get('https://gennum1234s1.azurewebsites.net/api/server3?code=jq5LBb5dHLNQTf8G9wkSuXICewy3/uvzvwR/a6orwrSWx9/frvyRQg==').text
    number = requests.get('https://gennum1234s1.azurewebsites.net/api/server2?code=ldSkjVqv1Lz2sLsPOGydcniTdsPL7n4Yu1VpF0mdMFYIlxpkrBtr1g==').text

    Username = number + alpha 

    # mix it up = random.sample(Username, len(Username))
    # return mix it up 

    container.create_item(body={"id": str(random.randint(1, 1000)), "Username": Username})

    return func.HttpResponse(Username)

    