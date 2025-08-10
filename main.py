import time
import random

class SimpleCRM:
    def __init__(self):
        self.customers = {
            "cust001": {"name": "Alice", "last_purchase": "2025-07-15", "issues": ["invoice delay"]},
            "cust002": {"name": "Bob", "last_purchase": "2025-08-01", "issues": []},
        }
        self.feedback_log = []

    def query_customer(self, customer_id, question):
        # Mocked LLM response generation with CRM context
        start = time.time()
        customer = self.customers.get(customer_id)
        if not customer:
            response = "Customer not found."
        else:
            # Simulate LLM generating response based on CRM data + question
            if "last purchase" in question.lower():
                response = f"{customer['name']}'s last purchase was on {customer['last_purchase']}."
            elif "issue" in question.lower() and customer["issues"]:
                response = f"{customer['name']} reported issues: {', '.join(customer['issues'])}."
            else:
                response = "I'm here to help with your CRM queries!"

        response_time = time.time() - start
        # Log feedback as random satisfaction score for demo
        satisfaction = random.choice([1, 2, 3, 4, 5])
        self.feedback_log.append({"customer_id": customer_id, "question": question, "response": response,
                                  "response_time": response_time, "satisfaction": satisfaction})
        return response, response_time, satisfaction

def main():
    crm = SimpleCRM()
    # Demo queries
    queries = [
        ("cust001", "What was the last purchase date?"),
        ("cust002", "Any reported issues?"),
        ("cust003", "Who is this customer?")
    ]
    for cid, question in queries:
        response, rt, sat = crm.query_customer(cid, question)
        print(f"Query for {cid}: {question}")
        print(f"Response: {response}")
        print(f"Response Time: {rt:.4f}s, Satisfaction: {sat}/5")
        print("-" * 30)

if __name__ == '__main__':
    main()
