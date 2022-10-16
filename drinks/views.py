from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3

@api_view(["GET"])
def home(request):
    db = boto3.resource("dynamodb")
    table = db.Table("drinks")
    drinks = table.scan() # get all of the table and store in variable drinks
    # return Response(drinks) # this will show table info and more useless info of the table and dynamoDB AWS
    return Response({"drinks": drinks.get("Items")}) # this will only show the "Items" 