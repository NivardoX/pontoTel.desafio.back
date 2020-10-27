from dotenv import load_dotenv
import os

load_dotenv()

default = "postgresql://postgres:123@localhost:5432/guerreirinhos"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", default)
# --------------------------------------------------------------------------------------------------#

DEBUG = True

# --------------------------------------------------------------------------------------------------#

ROWS_PER_PAGE = int(os.environ.get("ROWS_PER_PAGE", 10))

# --------------------------------------------------------------------------------------------------#

JWT_SECRET_KEY = "XyeFq2YSfEf95vQZ6SfnhZlJHHxjjp1D"

# --------------------------------------------------------------------------------------------------#

SQLALCHEMY_TRACK_MODIFICATIONS = True

# --------------------------------------------------------------------------------------------------#
