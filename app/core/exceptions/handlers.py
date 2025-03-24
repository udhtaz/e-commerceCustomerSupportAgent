# app/core/exceptions/handlers.py

from fastapi import Request
from fastapi.responses import JSONResponse
from langchain.schema import OutputParserException

from app.core.logging import logger

async def output_parser_exception_handler(request: Request, exc: OutputParserException):

    """
    Handles OutputParserException from the LangChain agent.

    Logs the error and returns a 422 Unprocessable Entity response with
    relevant details for debugging.

    Args:
        request (Request): The incoming HTTP request.
        exc (OutputParserException): The exception raised during output parsing.

    Returns:
        JSONResponse: A response containing the error message and 422 status code.
    """

    logger.error(f"Output parsing failed: {str(exc)}")
    return JSONResponse(
        status_code=422,
        content={"detail": "Agent output could not be parsed.", "error": str(exc)},
    )
