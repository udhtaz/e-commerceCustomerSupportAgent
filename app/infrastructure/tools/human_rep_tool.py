import csv
from langchain.tools import BaseTool

class HumanRepTool(BaseTool):

    """
    Tool to handle user requests to speak with a human representative.

    Attributes:
        name (str): Identifier for the tool used by the agent.
        description (str): Explanation of the tool's purpose and expected input format.
    """

    name: str = "human_rep_tool"
    description: str = (
        "Use this tool when a user requests to speak to a human representative. "
        "Input must be a string formatted as 'Full Name, Email, Phone Number'. "
        "It saves the contact info to a CSV file."
    )

    def _run(self, contact_info: str) -> str:

        """
        Process the contact information and save it to a CSV file.

        Args:
            contact_info (str): A comma-separated string in the format 'Full Name, Email, Phone Number'.

        Returns:
            str: Acknowledgment message or an error message if input format is invalid or saving fails.
        """

        try:
            parts = [x.strip() for x in contact_info.split(",")]
            if len(parts) != 3:
                return "Invalid input format. Please use: Full Name, Email, Phone Number"

            with open("data/contact_info.csv", "a", newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(parts)

            return "Your request has been noted. A human representative will contact you soon."
        except Exception as e:
            return f"Error saving contact info: {str(e)}"

    async def _arun(self, contact_info: str) -> str:

        """
        Asynchronous version of the run method (not implemented).

        Args:
            contact_info (str): Contact string.

        Raises:
            NotImplementedError: This tool does not support asynchronous execution.
        """

        raise NotImplementedError("This tool does not support async.")
