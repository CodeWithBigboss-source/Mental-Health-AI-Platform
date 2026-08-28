CRISIS_RESPONSE = """I'm really glad you told me this, and I want you to be safe right now.

I'm not able to provide emergency help myself, but please reach out immediately to:
- A crisis helpline in your country
- Emergency services (e.g. 15 in Pakistan for police/rescue, or your local emergency number)
- A trusted person near you right now

You don't have to go through this alone. Would you like me to stay here with you while you reach out to someone?"""

def get_safety_action(risk_level: int) -> dict:
    if risk_level == 4:
        return {"action": "crisis_response", "override_response": CRISIS_RESPONSE, "continue_normal_flow": False}
    if risk_level == 3:
        return {"action": "recommend_professional", "override_response": None, "continue_normal_flow": True}
    return {"action": "none", "override_response": None, "continue_normal_flow": True}
