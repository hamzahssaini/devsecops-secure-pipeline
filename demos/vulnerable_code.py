# def execute_user_command(user_input):
#     """
#     DANGEROUS EVAL USAGE DEMO
#     This function uses python's eval/exec which is highly insecure
#     if user input is passed directly to it.
    
#     Bandit will flag this with CWE-94 (Improper Control of Generation of Code).
#     """
#     print(f"Executing: {user_input}")
    
#     # Intentional vulnerability
    eval(user_input)  # nosec B307

# if __name__ == "__main__":
#     execute_user_command('print("Hello DevSecOps!")')
