import json
import os
import mercadopago

def lambda_handler(event, context):

    # Profe me confundi con el link del api mandandolo a silabuz, es este para que pueda probarlo:
    # https://p7rehb0xq7.execute-api.us-east-2.amazonaws.com/default/new

    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    products = json.loads(event["body"])
    
    data = {
        
        "transaction_amount": products["transaction_amount"],
        "token": products["token"],
        "installments": products["installments"],
            
        "payment_method_id": products["payment_method_id"],
        "payer": {
            "email": products["payer"]["email"],
            "identification": {
                "type": products["payer"]["identification"]["type"],
                "number": products["payer"]["identification"]["number"]
                }
            }
    }

    response = sdk.payment().create(data)
    
    return {
        "statusCode":200,
        "body": json.dumps(response)
    }