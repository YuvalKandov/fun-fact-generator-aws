import boto3, random, json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudFacts")

bedrock = boto3.client("bedrock-runtime", region_name="eu-central-1")

MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

def lambda_handler(event, context):
    # Get a fact (fallback text if table is empty)
    items = table.scan().get("Items", [])
    fact = random.choice(items)["FactText"] if items else "Cloud computing helps you scale without buying hardware."

    user_text = (
        "Take this cloud computing fact and make it fun and engaging in 1–2 sentences max. "
        "Keep it short and witty:\n\n" + fact
    )
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {"role": "user", "content": [{"type": "text", "text": user_text}]}
        ],
        "max_tokens": 120,
        "temperature": 0.7
    }

    try:
        resp = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json",
        )
        result = json.loads(resp["body"].read())
        witty = "".join(
            block.get("text", "")
            for block in result.get("content", [])
            if block.get("type") == "text"
        ).strip()
        witty_fact = witty if 0 < len(witty) <= 300 else fact

    except Exception as e:
        print(f"Bedrock error: {e}")
        witty_fact = fact

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
        "body": json.dumps({"fact": witty_fact}),
    }
