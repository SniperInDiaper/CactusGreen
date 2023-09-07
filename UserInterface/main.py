import os
import gradio as gr
import openai

css = """
.feedback textarea {font-size: 24px !important;}
.centered {
  display: flex;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        height: 10vh !important;
}
.label {
  font-size: 24px !important;
  font-weight: bold !important;
  transform: translate(0px, 0px) !important;
}
"""
html = """
<div>
<span><img src='https://cdn.discordapp.com/attachments/1146469444902715392/1146900078129332407/logo2.png' alt='Centered Image'></span>
</div>
"""
markdown = """
## AI Business Decision Analysis Module

The **AI Business Decision Analysis Module** is an advanced artificial intelligence tool designed to assist businesses in making informed decisions by analyzing various factors and providing actionable insights. This module employs state-of-the-art machine learning algorithms and data analysis techniques to evaluate business decisions and offer detailed reports on strategies to enhance success rates.

### Features

1. **Decision Assessment:** The AI module starts by assessing the parameters of the business decision, including market trends, financial projections, risk factors, and potential outcomes.

2. **Data Integration:** It integrates both internal and external data sources, such as historical company data, market research, and industry benchmarks, to ensure a comprehensive analysis.

3. **Risk Evaluation:** The AI assesses potential risks associated with the decision and quantifies their potential impact on the business. It identifies vulnerabilities and suggests mitigation strategies.

4. **Success Factors:** The module identifies key success factors related to the decision. It considers factors like market demand, competitive landscape, financial feasibility, and operational efficiency.

5. **Scenario Simulation:** Using historical data and predictive modeling, the AI can simulate different scenarios based on different decision outcomes. This helps in understanding potential results and adjusting strategies accordingly.

6. **Recommendations:** The AI generates a detailed report outlining recommendations for improving the success chances of the decision. These recommendations are data-driven and tailored to the specific business context.

7. **Avoidance Strategies:** In addition to suggesting what to do, the AI module highlights potential pitfalls and provides insights into what to avoid. This helps in steering clear of common mistakes that could hinder success.

8. **Visualizations:** The module presents its findings through interactive visualizations, charts, and graphs. This helps stakeholders understand complex data and insights more easily.

### Benefits

- **Informed Decision-Making:** Businesses can make decisions with higher confidence, backed by data-driven insights and comprehensive analysis.

- **Risk Mitigation:** By identifying and quantifying potential risks, the AI module enables businesses to take proactive measures to mitigate these risks.

- **Strategy Adjustment:** The scenario simulation feature allows businesses to refine their strategies based on various outcomes, optimizing decision-making.

- **Reduced Errors:** The AI's avoidance strategies help businesses steer clear of common mistakes and pitfalls, reducing the chances of failure.

- **Time and Cost Savings:** By automating the analysis process, businesses can save time and resources that would otherwise be spent on manual research and analysis.

In conclusion, the AI Business Decision Analysis Module empowers businesses to make well-informed decisions by analyzing critical factors and providing actionable recommendations. By harnessing the power of AI, businesses can increase their success chances and achieve their goals more effectively.
"""

# if you have OpenAI API key as an environment variable, enable the below
openai.api_key = os.getenv("OPENAI_API_KEY")


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


blocks = gr.Blocks(css=css, theme=gr.themes.Soft())


def PrintAnalysisReport(Type, Startup_Costs, Marketing_Budget):
    return openai_create(
        f"""
i want to build a {Type} branch in Saudi Arabia - Riyadh city

Startup Costs: {Startup_Costs} SR

Marketing Budget: {Marketing_Budget} SR

Given the following data I would like you to give me a marketing plan and a Staffing plan and if this is a good dec or not in the following format:

* Revenue Projections and Operating Costs for the first 5 years note that if there is no data for the first 5 years you can simulate the data.

* Break-even point analysis and the inflation effect on the analysis.

* Staffing plan for the first 5 years and the cost of each employee and the total cost of the employees depending on the revenue projections and the business type.

* Marketing Plan for the first 5 years and the cost of each marketing campaign and the total cost of the marketing campaigns depending on the revenue projections and the business type.

and make it concise and professional and numbers-wise.

after that i want you to give me a table in markdown format with the following:
summary of the analysis
the key success factors
the key risks
the key recommendations
the key avoidance strategies
a table with the following:
the revenue projections for the first 5 years
the operating costs for the first 5 years
the staffing plan for the first 5 years
the marketing plan for the first 5 years
the net profit for the first 5 years

for each of the above points be sure to list the assumptions and the data sources used in the analysis. and line-break after each point using "=" seperator.
"""
    )


def openai_create(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}"}],
        temperature=0.7,
    )

    return response["choices"][0]["message"]["content"]


with blocks as demo:
    gr.HTML(value=html, elem_classes="centered")
    gr.Label("Welcome to Consultant Business Model.!", elem_classes="label centered")
    gr.Markdown(markdown)
    box0 = gr.Textbox(
        info="Whether it's a coffee shop or a restaurant etc..",
        label="Business Type",
        placeholder="",
        value="",
        elem_id="warning",
        elem_classes="feedback",
    )
    box1 = gr.Textbox(
        info="The total estimated startup costs, including expenses such as rent, interior design, equipment purchase, licenses and permits, staff salaries, marketing expenses, and any other relevant costs. Please provide a breakdown if possible.",
        label="Startup Budget",
        placeholder="",
        value="",
        elem_id="warning",
        elem_classes="feedback",
    )
    box4 = gr.Textbox(
        info="Costs of your marketing plan, including how you plan to attract customers to your new coffee shop. This may include social media promotion, local partnerships, and customer loyalty programs.",
        label="Marketing Budget",
        placeholder="",
        value="",
        elem_id="warning",
        elem_classes="feedback",
    )
    # output
    output1 = gr.Textbox(
        label="Analysis Report",
        placeholder="Analysis Report",
        value="",
        elem_id="warning",
        elem_classes="feedback",
        lines=10,
        show_copy_button=True,
    )
    btn = gr.Button(value="analyse", elem_id="submit", elem_classes="feedback")
    btn.click(PrintAnalysisReport, [box0, box1, box4], output1)
    demo.launch(share=True)
