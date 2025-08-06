from config import DB_User, DB_Password, DB_Host, DB_Name
from sqlalchemy import create_engine,text
from demotradingclass import demotrading
import pandas as pd

engine = create_engine(f"mysql+pymysql://{DB_User}:{DB_Password}@{DB_Host}/{DB_Name}")

def instruction_input():
    return(
        "'id' : 'int'\n"
        "'Asset' : 'str'\n"
        "'position_type' : 'bool'\n"
        "'entryprice' : 'float'\n"
        "'stoploss' : 'float'\n"
        "'takeprofit' : 'float'\n"
        "'Risk_in_percent' : 'float'\n"
        "'RR_ratio' : 'float'\n"
        "'size_in_asset' : 'float'\n"
        "'strategy_used' : 'str'\n"
        "'strategy_compliance' : 'bool'\n"
        "'thoughts_before' : 'str'\n"
        "'thoughts_during' : 'str'\n"
        "'thoughts_after' : 'str'\n"
        "'exit_price' : 'float'\n"
        "'PNL' : 'float'\n")






trade26 =  demotrading(
    id=,
    Asset="",
    position_type=,
    entryprice=,
    stoploss=,
    takeprofit=,
    Risk_in_percent=,
    RR_ratio=,
    size_in_asset=,
    strategy_used="",
    strategy_compliance=,
    thoughts_before="",
    thoughts_during="",
    thoughts_after="",
    exit_price=,
    PNL=,
)
df=pd.DataFrame([trade26.to_sql_dict()])
df.to_sql("demotrading1",con=engine,if_exists="append",index=False)












