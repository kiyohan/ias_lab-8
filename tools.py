from langchain_core.tools import tool

@tool
def classify_issue(message: str) -> str:
    """Classify issue into: delivery, refund, technical, other."""

    message = message.lower()

    if any(word in message for word in ["delivery", "late", "order", "where is my order", "tracking"]):
        return "delivery"

    if any(word in message for word in ["refund", "return", "money back"]):
        return "refund"

    if any(word in message for word in ["not working", "error", "bug", "issue"]):
        return "technical"

    return "other"


@tool
def delivery_handler() -> str:
    """Handle delivery issues."""
    return "Your order is in transit and will arrive within 2 days."


@tool
def refund_handler() -> str:
    """Handle refund issues."""
    return "Your refund request is approved. Amount will be credited in 5-7 business days."


@tool
def technical_handler() -> str:
    """Handle technical issues."""
    return "Please try clearing cache and reinstalling the app. Contact support if issue persists."


@tool
def escalate_to_human() -> str:
    """Escalate issue to human agent."""
    return "Your issue has been escalated to a human support executive."