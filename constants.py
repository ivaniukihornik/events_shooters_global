import os
from dotenv import load_dotenv


# browser screen size
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# time rates
DEFAULT_POLL_INTERVAL_S = 0.1
DEFAULT_POLL_ACTION_TIMEOUT_S = 5
DEFAULT_WAITING_TIMEOUT_MS = 5000
BUILDER_LOADING_TIMEOUT_MS = 300000

# system path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = ROOT_DIR + '/test_results/screenshots'

# site path
MAIN_PAGE_URL = 'https://events.shooters.global'
LOGIN_PAGE_URL = MAIN_PAGE_URL + '/sign-in'
LOGIN_PAGE_URL_GET_STARTED = LOGIN_PAGE_URL + '#get-started'
STAGE_BUILDER_PAGE = MAIN_PAGE_URL + '/stage-builder'


# env
load_dotenv()
USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')
