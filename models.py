from datetime import datetime
from config import config
from sqlmodel import Field, Session, SQLModel, create_engine, select

DATABASE_URL = f"postgresql://{config['DATA_BASE']['USER']}:{config['DATA_BASE']['PASSWORD']}@{config['DATA_BASE']['IP']}:{config['DATA_BASE']['PORT']}/{config['DATA_BASE']['NAME']}"
engine = create_engine(DATABASE_URL)


class UserCommandLog(SQLModel, table=True):
    __tablename__ = "user_command_log"
    id: int = Field(primary_key=True)
    userid: int
    command: str
    bot_response: str
    date: datetime

    def toJson(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "command": self.command,
            "bot_response": self.bot_response,
            "date": self.date,
        }


def find(user_id):
    with Session(engine) as session:
        statement = select(UserCommandLog).where(UserCommandLog.userid == user_id)
        records: list[UserCommandLog] = session.exec(statement)

        return list(map(lambda x: x.toJson(), records))


def findAll():
    with Session(engine) as session:
        statement = select(UserCommandLog)
        records: list[UserCommandLog] = session.exec(statement)

        return list(map(lambda x: x.toJson(), records))
