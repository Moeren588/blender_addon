

def log_console_message(log_type:str, message:str) -> None:

    match log_type.upper():
        case 'INFO': print(f'\033[34m[INFO]:\033[0m {message}')
        case 'WARNING': print(f'\033[33m[WARNING]:\033[0m {message}')
        case 'ERROR': print(f'\033[31m[ERROR]:\033[0m {message}')
        case 'FINISH': print(f'\033[32m[FINISHED]:\033[0m {message}')
        case 'SYS': print(f'\033[36m[SYSTEM]:\033[0m {message}')
        case 'DEBUG': print(f'\033[35m[DEBUG]:\033[0m {message}')
        case _: print(f'[{log_type.upper()}] : {message}')