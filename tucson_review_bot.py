import argparse

def generate_response(business_name, review_text, rating):
    """Generates a professional, personalized response to a customer review."""
    sentiment = "positive" if rating >= 4 else "constructive"

    if sentiment == "positive":
        return f"Hi there! Thank you so much for the {rating}-star review of {business_name}. We're thrilled to hear you had a great experience. We appreciate you taking the time to share your feedback and can't wait to serve you again soon!"
    else:
        return f"Hi there, thank you for your honest {rating}-star feedback about {business_name}. We're sorry to hear your experience didn't meet expectations. We take this seriously and would love to make it right. Please reach out to us directly so we can resolve this for you."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tucson Local Business Review Responder")
    parser.add_argument("--business", required=True, help="Name of the local business")
    parser.add_argument("--review", required=True, help="The customer's review text")
    parser.add_argument("--rating", type=int, required=True, help="Star rating (1-5)")

    args = parser.parse_args()
    response = generate_response(args.business, args.review, args.rating)

    print(f"\n🏢 BUSINESS: {args.business} ({args.rating}/5 Stars)")
    print(f"💬 CUSTOMER REVIEW: \"{args.review}\"")
    print(f"\n✅ AI GENERATED RESPONSE:\n{response}\n")
