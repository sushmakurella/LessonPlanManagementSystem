import fitz
import re

def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text

def extract_course_outcomes(text):
    """Extracts course outcomes and their knowledge levels."""
    co_pattern = re.findall(r"(CO\d+):\s*(.*?)(\(?K\d\)?)", text, re.DOTALL)
    co_dict = {}

    for co in co_pattern:
        co_number = co[0]
        co_text = co[1].strip().replace("\n", " ")
        knowledge_level = co[2].strip() if co[2] else "N/A"
        co_dict[co_number] = [co_text, knowledge_level]

    return co_dict

def extract_units(text):
    """Extracts units and their syllabus."""
    unit_pattern = re.findall(r"(UNIT-\w+):\s*(.*?)(?=UNIT-\w+:|\Z)", text, re.DOTALL)
    unit_dict = {}

    for unit in unit_pattern:
        unit_number = unit[0].strip()
        unit_content = unit[1].strip()

        lines = unit_content.split("\n")
        unit_name = lines[0].strip()

        syllabus = []
        for line in lines[1:]:
            topics = re.split(r"[,;]", line)
            syllabus.extend([topic.strip() for topic in topics if topic.strip()])

        unit_dict[unit_number] = {"name": unit_name, "Syllabus": syllabus}

    return unit_dict
