from langchain.tools import BaseTool

POLICIES = {
    "general": (
        "You can return most items within 30 days of purchase for a full refund or exchange. "
        "Items must be in their original condition, with all tags and packaging intact. "
        "Please bring your receipt or proof of purchase when returning items."
    ),
    "exceptions": (
        "Certain items such as clearance merchandise, perishable goods, and personal care items are "
        "non-returnable. Please check the product description or ask a store associate for more details."
    ),
    "refunds": (
        "Refunds will be issued to the original form of payment. "
        "If you paid by credit card, the refund will be credited to your card. "
        "If you paid by cash or check, you will receive a cash refund."
    )
}

class ReturnPolicyTool(BaseTool):
    name: str = "return_policy_tool"
    description: str = (
        "Use this tool to answer questions about the store's return policies. "
        "Input should be a question about returns. Output is a policy statement."
    )

    def _run(self, query: str) -> str:
        query = query.lower()
        if "non-returnable" in query or "cannot be returned" in query or "exceptions" in query:
            return POLICIES["exceptions"]
        elif "refund" in query:
            return POLICIES["refunds"]
        else:
            return POLICIES["general"]

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("This tool does not support async.")
