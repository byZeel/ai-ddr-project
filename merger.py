import json

def safe_json_load(data):
    try:
        return json.loads(data)
    except:
        return []

def merge_data(insp_json, therm_json):
    inspection = safe_json_load(insp_json)
    thermal = safe_json_load(therm_json)

    merged = []

    for insp in inspection:
        area = insp.get("area", "Unknown")
        issue = insp.get("issue", "Not Available")

        match = None
        for t in thermal:
            if area.lower() in t.get("area", "").lower():
                match = t
                break

        if match:
            thermal_issue = match.get("issue", "Not Available")
            temp = match.get("temperature", "Not Available")

            # Simple conflict detection
            if "no issue" in issue.lower() and thermal_issue != "Not Available":
                conflict = "Conflict detected between inspection and thermal data"
            else:
                conflict = "No conflict"

        else:
            thermal_issue = "Not Available"
            temp = "Not Available"
            conflict = "Thermal data missing"

        merged.append({
            "area": area,
            "inspection_issue": issue,
            "thermal_issue": thermal_issue,
            "temperature": temp,
            "conflict": conflict
        })

    return merged