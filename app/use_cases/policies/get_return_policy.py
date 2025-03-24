from app.domain.policies import RETURN_POLICIES

class GetReturnPolicyUseCase:

    """
    Use case for retrieving store return policy information based on a user's query.

    This use case interprets the query and returns the most relevant section 
    of the store's return policy (general rules, exceptions, or refund info).
    """

    def execute(self, query: str) -> str:

        """
        Process the query to determine and return the appropriate return policy information.

        Args:
            query (str): A string containing the user's question or keywords about returns.

        Returns:
            str: A detailed policy statement relevant to the query.
        
        Example:
            >>> use_case = GetReturnPolicyUseCase()
            >>> use_case.execute("What items are non-returnable?")
            "Certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable..."
        """

        query = query.lower()
        if "non-returnable" in query or "exceptions" in query:
            return RETURN_POLICIES["exceptions"]
        elif "refund" in query:
            return RETURN_POLICIES["refunds"]
        return RETURN_POLICIES["general"]
