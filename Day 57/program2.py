from ast import keyword
#rule based text xclassification

def classify_request(text):
    text = text.lower()
    
    if  any(keyword in text for keyword in ["billing", "invoice", "charge"]):
        return "Billing Issue"
    elif any(keyword in text for keyword in ["password","access","login","account"]):
        return "Technical support"
    elif any(keyword in text for keyword in ["hour","time","location","general"]):
        return "general support"
    else:
        return "other support"
    
    #test sample
requestes=[
        "my account is  blocked",
        "I need my last billing details",
        "I need to know the timing of my order"
    ]
for request in requestes:
        category = classify_request(request)
        print(f"request: {request}\n category: {category}\n")