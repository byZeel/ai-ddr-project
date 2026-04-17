from extractor import extract_pdf
from llm import call_llm
from merger import merge_data
from prompts import INSPECTION_PROMPT, THERMAL_PROMPT, REPORT_PROMPT

def run_pipeline(inspection_pdf, thermal_pdf):
    print("Extracting PDFs...")
    insp_text, insp_images = extract_pdf(inspection_pdf)
    therm_text, therm_images = extract_pdf(thermal_pdf)

    print("Structuring data with LLM...")
    insp_prompt = INSPECTION_PROMPT.replace("{text}", insp_text)
    therm_prompt = THERMAL_PROMPT.replace("{text}", therm_text)

    insp_struct = call_llm(insp_prompt)
    therm_struct = call_llm(therm_prompt)

    print("Merging data...")
    merged = merge_data(insp_struct, therm_struct)

    print("Generating report...")
    report_prompt = REPORT_PROMPT.replace("{data}", str(merged))
    report = call_llm(report_prompt)

    with open("final_report.txt", "w") as f:
        f.write(report)

    print("\n===== FINAL REPORT =====\n")
    print(report)


if __name__ == "__main__":
    run_pipeline("inspection.pdf", "thermal.pdf")