from aims.router.router import route_message
from aims.language_en.aim import respond as respond_en
from aims.language_es.aim import respond as respond_es
from aims.issue_classifier.aim import classify_issue



def handle_message(message: str) -> dict:
    route = route_message(message)
    issue = classify_issue(message)

    if route == "language_es":
        reply = respond_es(message)
    else:
        reply =respond_en(message)

    # Escalation rule (Fast path)
    escalate = (issue == "billing")

    if escalate:
        if route == "language_es":
            reply += "\n\nVoy a escalar esto a un agente humano de facturacion."
        else:
            reply += "\n\nI'm escalating this to a human billing agent."

    return {
        "route": route,
        "issue": issue,
        "reply": reply,
        "escalate": escalate,
    }
