import gradio as gr

css = """
.feedback textarea {font-size: 24px !important; background-color: #000000 !important}
.centered {
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
}
.label {
  font-size: 24px !important;
  font-weight: bold !important;
  color: #000000 !important;
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

blocks = gr.Blocks(css=css)
def PrintAnalysisReport(name, age):
  return f"Hello {name}! You are {age} years old."
  
with blocks as demo:
    gr.HTML(value=html,elem_classes="centered")
    gr.Label("Welcome to Consultant Business Model.!", elem_classes="label centered")
    gr.Markdown(markdown)
    box1 = gr.Textbox(label="Name", placeholder="Enter your name", value="", elem_id="warning", elem_classes="feedback")
    box2 = gr.Textbox(label="age", placeholder="Enter your age", value="", elem_id="warning", elem_classes="feedback")
    output1 = gr.Textbox(label="Analysis Report", placeholder="Analysis Report", value="", elem_id="warning", elem_classes="feedback",lines=10)
    btn = gr.Button(value="analyse", elem_id="submit", elem_classes="feedback")
    btn.click(PrintAnalysisReport,[box1, box2],output1)
    demo.launch()
    