from fpdf import FPDF
from demotrading1_analysis import(
PNL_descriptive_analysis,
table,
wins_chart,
loss_chart,
shapiro_Wilk,
pp_corelation,
t_test,
chi2,
barchart,
PNL_list,
id_list,
compliance_rate,
RR_ratio,
)
def clean_text(text):
    if isinstance(text, str):
        return text.encode('latin-1', 'replace').decode('latin-1')
    return str(text)
def generate_report(output_path="analysis_report.pdf"):

    pdf=FPDF()
    pdf.add_page()

    pdf.set_font("Arial","B",16)
    pdf.cell(200,10,clean_text("Trading Data Analysis Report"),ln=True, align = "C")

    pdf.ln(10)
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,clean_text("1. SQL:"),ln=True)
    table_df= table()
    pdf.set_font("Courier",size=8)
    for _ , row in table_df.iterrows():
        pdf.cell(0,8,clean_text(str(list(row.values))),ln=True)

    pdf.ln(10)
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,clean_text("2. PNL Descriptive Analysis:"),ln=True)
    stats=PNL_descriptive_analysis(PNL_list)
    for key,value in stats.items():
        pdf.cell(0,8,clean_text(f"{key}:{value}"), ln= True)

    wins_fig=wins_chart(PNL_list,id_list)
    wins_fig.savefig("wins_chart.png")
    pdf.image("wins_chart.png", x=10, w=180)

    losses_fig=loss_chart(PNL_list,id_list)
    losses_fig.savefig("Loss_chart.png")
    pdf.image("Loss_chart.png",x=10,w=180)

    pdf.ln(10)
    pdf.set_font("Arial",size=10)
    pdf.cell(200,10,clean_text("5.Shapro-Wilk Test:"),ln=True)
    shapiro_result=shapiro_Wilk(PNL_list)
    for key,value in shapiro_result.items():
        pdf.cell(0,8,clean_text(f"{key} {value}"),ln=True)
    corr_results=pp_corelation(RR_ratio,PNL_list)
    for key,value in corr_results.items():
        pdf.cell(0,8,clean_text(f"{key} {value}"),ln=True)

    pdf.ln(5)
    pdf.cell(200,10,clean_text("7. T-Test:"), ln=True)
    ttest_results=t_test(PNL_list)
    for key,value in ttest_results.items():
        pdf.cell(0,8,clean_text(f"{key} {value}"), ln=True)

    pdf.ln(5)
    pdf.cell(200,10,clean_text("8. Chi2 Test (Compliance vs Winrate):"),ln=True)
    chi2_results=chi2(PNL_list,compliance_rate)
    for key,value in chi2_results.items():
        pdf.cell(0,8,clean_text(f"{key} {value}"),ln=True)

    barchart_fig=barchart(PNL_list,id_list)
    barchart_fig.savefig("barchart.png")
    pdf.image("barchart.png", x=10 , w=180)

    pdf.output(output_path)

if __name__== "__main__":
    generate_report("analysis_report.pdf")
