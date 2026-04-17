INSPECTION_PROMPT = """
Extract structured observations from this inspection report.

{text}

Return STRICT JSON ONLY:
[
  {
    "area": "",
    "issue": "",
    "description": ""
  }
]
"""

THERMAL_PROMPT = """
Extract thermal findings.

{text}

Return STRICT JSON ONLY:
[
  {
    "area": "",
    "temperature": "",
    "issue": ""
  }
]
"""

REPORT_PROMPT = """
Generate a professional DDR report.

RULES:
- Do NOT invent data
- Use simple language
- Write "Not Available" if missing
- Clearly mention conflicts

DATA:
{data}

FORMAT:
1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information
"""