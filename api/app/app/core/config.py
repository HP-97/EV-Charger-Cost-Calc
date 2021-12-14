from pydantic import BaseSettings
from pydantic.networks import AnyHttpUrl

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    PROJECT_NAME: str
    TEST_EV_LOG_PATH: str = "app/tests/ev_logs"
    
settings = Settings()