import sys
# configurations for application
from cfg.application import *

def sys_exit(msg: str ="" ) -> str:
    if msg=="":
        print(f"\n ... Sorry, you pressed key \"X\" ... bye, bye")
    else:
        print(f"\n ... {msg}")
    sys.exit(0)

# prints standard header
def workshop_task_header() -> str:
    header_string=60 * "-" + "\n" + f"{CFG_APP_CODE}" + "\n" + 60 * "-"
    print(header_string)
    return header_string

# prints standard footer
def workshop_task_footer() -> str:
    #footer_string="--- end "+52*"-"
    footer_string=""
    print(footer_string)
    return footer_string
