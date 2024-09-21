import logging

from codealchemy import log_group

# Ensure the logger level is set to INFO
# logging.getLogger(__name__).setLevel(logging.INFO)

@log_group("MainGroup",include_prints=True)
def main_function():
    print("====1Inside main function===")
    print("*"*20)
    logging.info("Inside main function")
    inner_function()

@log_group("InnerGroup",include_prints=True)
def inner_function():
    print("====2Inside inner function====")
    print("*"*20)
    logging.info("Inside inner function")
    innermost_function()

@log_group("InnermostGroup",include_prints=False)
def innermost_function():
    print("====3Inside innermost function====")
    print("*"*40)
    logging.info("Inside innermost function")
    print("Innermost function executed")


# @log_group("2MainGroup")
# def new_main_function():
#     print("====New 1Inside main function===")
#     print("*"*20)
#     logging.info("New Inside main function")
#     new_inner_function()

# @log_group("2InnerGroup")
# def new_inner_function():
#     print("====2Inside inner function====")
#     print("*"*20)
#     logging.info("New Inside inner function")


main_function()
# new_main_function()