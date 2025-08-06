from scipy.stats import skew,kurtosis
from config import DB_User,DB_Password,DB_Host,DB_Name
from sqlalchemy import create_engine,text
import pandas as pd
import math
from scipy.stats import shapiro,ttest_1samp,chi2_contingency,pearsonr
import numpy as numpy
import matplotlib as pyplot
import matplotlib.pyplot as plt


engine=create_engine(f"mysql+pymysql://{DB_User}:{DB_Password}@{DB_Host}/{DB_Name}")

with engine.connect() as connection:
    result=connection.execute(text("SELECT * from demotrading1"))
    rows=result.fetchall()
    df=pd.DataFrame(rows,columns=result.keys())

PNL_list=df["PNL"].tolist()
compliance_rate=df["strategy_compliance"].tolist()
RR_ratio=df["RR_ratio"].tolist()
id_list=df["id"].tolist()


def PNL_descriptive_analysis(PNL_list):
    sum_win=0
    count_win=0
    sum_loss=0
    count_loss=0
    for result in PNL_list:
        if result >=0:
            sum_win+=result
            count_win+=1

        else:
            sum_loss+=result
            count_loss+=1



    winrate=count_win/(count_win+count_loss)*100
    mean_win=sum_win/count_win
    mean_loss=sum_loss/count_loss
    total_trades=count_win+count_loss
    EV=(winrate*mean_win)+((1-winrate)*mean_loss)

    diff_from_meanL=0
    diff_from_meanW = 0
    for element in PNL_list:
        if element >=0:
            diff_from_meanW+=(element-mean_win)**2

        else:
            diff_from_meanL+=(element-mean_loss)**2

    SD_W=math.sqrt(diff_from_meanW/count_win) if count_win else 0
    SD_L=math.sqrt(diff_from_meanL/count_loss) if count_loss else 0

    CV_W=(SD_W/mean_win)*100
    CV_L=(SD_L/(abs(mean_loss)))*100

    CV_W_Classification=None
    CV_L_Classification =None

    if CV_W <=20:
        CV_W_Classification="Weak variation"
    elif 20<CV_W<=40:
        CV_W_Classification="Moderate variation"
    elif 40<CV_W<=60:
        CV_W_Classification="Strong Variation"
    else:
        CV_W_Classification="Very strong variation"

    if CV_L <=20:
        CV_L_Classification="Weak variation"
    elif 20<CV_L<=40:
        CV_L_Classification="Moderate variation"
    elif 40<CV_L<=60:
        CV_L_Classification="Strong Variation"
    else:
        CV_L_Classification="Very strong variation"
    wins_list=[]
    losses_list=[]

    for result in PNL_list:
        if result <=0:
            wins_list.append(result)
        else:
            losses_list.append(result)
    Skewness_of_wins=skew(wins_list)
    Skewness_of_losses = skew(losses_list)



    skewnessW_inter=None


    if Skewness_of_wins > 0:
        skewnessW_inter="Distribition of data to the left"
    elif Skewness_of_wins < 0:
        skewnessW_inter = "Distribition of data to the right"
    else:
        skewnessW_inter = "Symetrical distribution"

    if Skewness_of_losses > 0:
        skewnessL_inter="Distribition of data to the left"
    elif Skewness_of_losses < 0:
        skewnessL_inter = "Distribition of data to the right"
    else:
        skewnessL_inter = "Symetrical distribution"

    kurtW=kurtosis(wins_list)
    kurtL = kurtosis(losses_list)

    KurtW_inter=None
    KurtL_inter=None

    if kurtW > 0:
        KurtW_inter="Leptokurtosis"
    elif kurtW < 0:
        KurtW_inter="Platykurtosis"
    else:
        KurtW_inter="Normal distribution"


    if kurtL > 0:
        KurtL_inter="Leptokurtosis"
    elif kurtL < 0:
        KurtL_inter="Platykurtosis"
    else:
        KurtL_inter="Normal distribution"





    return {
        "winrate": winrate,
        "mean of win": mean_win,
        "mean of losses": mean_loss,
        "total number of trades": total_trades,
        "SD of Wins": SD_W,
        "SD of Losses": SD_L,
        "Expected Value": EV,
        "Coefficient of Variation - Wins":f"{CV_W},{CV_W_Classification}",
        "Coefficient of Variation - Losses": f"{CV_L}: {CV_L_Classification}",
        "Skewness of Wins": f"{Skewness_of_wins}:{skewnessW_inter}",
        "Skewness of Losses": f"{Skewness_of_losses}:{skewnessL_inter}",
        "Kurtosis of Wins":f"{kurtW}:{KurtW_inter}",
        "Kurtosis of Losses":f"{kurtL}:{KurtL_inter}"

    }

def shapiro_Wilk(PNL_list):
    stat,p=shapiro(PNL_list)

    if p>0.05:
        interpretation="Distribution closer to gaussian - acceptance of H0"
    else:
        interpretation="Distribution not normal - rejection of H0 "

    return {
        "value":stat,
        "p value": p,
        "interpretation":interpretation,

    }

def pp_corelation(RR_ratio,PNL_list):
    r,p=pearsonr(RR_ratio,PNL_list)

    if r>0 and r<=0.3:
        interpretation="Weak positive correlation."

    elif r>0.3 and r<=0.6:
        interpretation="moderate positive correlation."

    elif r>0.6 and r<=0.99:
        interpretation="strong positive correlation."

    elif r==1:
        interpretation="perfect positive relationship."

    elif r==-1:
        interpretation="perfect negative relationship."

    if r < 0 and r >= -0.3:
        interpretation = "Weak negative correlation."

    elif r < -0.3 and r >= -0.6:
        interpretation = "moderate negative correlation."

    else:
        interpretation = "strong negative correlation."

    return {
        "Pearson correlation coefficient":r,
        "Interpretation:":interpretation
    }



def t_test(PNL_list):
    stat,p=ttest_1samp(PNL_list,0)

    if p > 0.05:
        interpretation="Results are statistically insignificant"

    else:
        if stat>0:
            interpretation="statisticaly significant - positive PNL"

        else:
            interpretation="Statistically significant-negative PNL"

    return {
        "t-stat":stat,
        "p-value":p,
        "mean":(sum(PNL_list)/len(PNL_list)),
        "intepretation": interpretation

    }


def chi2(PNL_list,compliance_rate):
    df["result"]=df["PNL"].apply(lambda x: "WIN" if x>=0 else "Loss")
    contigency_table=pd.crosstab(df["strategy_compliance"],df["result"])
    print(contigency_table)

    chi2,p,dof,expected = chi2_contingency(contigency_table)

    if p<0.05:
        interpretation="H0 rejection-compliance  is related to winrate"
    else:
        interpretation="Not enough evidence to reject H0-complaince likely doesnt influence winrate "

    return {
        "Chi2 Value":chi2,
        "degrees of freedom":dof,
        "p -value": p,
        "intepretation":interpretation,
    }



def barchart(PNL_list,id_list):
    colors=["green" if pnl>=0 else "red" for pnl in PNL_list]

    fig,ax= plt.subplots(figsize=(8,5))
    ax.bar(id_list,PNL_list,color=colors)
    ax.axhline(0,color="black",linewidth=1)
    ax.set_xlabel("Trade ID")
    ax.set_ylabel("PNL (%)")
    return fig


def wins_chart(PNL_list,id_list):
    wins=[(trade_id,pnl) for trade_id,pnl in zip(id_list,PNL_list) if pnl>0]
    x_wins=[trade_id for trade_id, _ in wins]
    y_wins=[pnl for _ , pnl in wins]

    fig,ax = plt.subplots(figsize=(8,5))

    ax.plot(x_wins,y_wins,marker="o", color="green", label= "Winning Trades")
    ax.axhline(0,color="black", linewidth=1)


    ax.set_xlabel("Trade number")
    ax.legend()

    return fig


def loss_chart(PNL_list,id_list):
    losses = [(trade_id, pnl) for trade_id, pnl in zip(id_list, PNL_list) if pnl < 0]
    x_losses = [trade_id for trade_id, _ in losses]
    y_losses = [pnl for _, pnl in losses]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(x_losses, y_losses, marker="o", color="red", label="losing trades")
    ax.axhline(0, color="black", linewidth=1)


    ax.set_xlabel("Trade number")
    ax.legend()

    return fig

def table():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * from demotrading1"))
        rows = result.fetchall()
        df = pd.DataFrame(rows, columns=result.keys())

        return df











