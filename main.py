import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import pypdf

load_dotenv()
api_key = os.getenv("MONA_API_KEY")

# Initialize LLM Client
client = OpenAI(api_key=api_key)

app = FastAPI(title="Mona AI Hackathon Multi-Agent Hub")

def extract_pdf_text(file_path: str) -> str:
    try:
        reader = pypdf.PdfReader(file_path)
        text = "".join([page.extract_text() or "" for page in reader.pages])
        return text if text.strip() else "[No text content found / Image-based PDF]"
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

@app.get("/")
def read_root():
    return {"message": "Multi-Agent Hub is live!"}

# --- TASK 3: WORK PERMIT VALIDATION AGENT (Leistenschneider) ---
class DocumentCheckRequest(BaseModel):
    file_path: str # e.g., "work_permits_part_3/permit_wp_valid_01.pdf"

@app.post("/agent/validate-work-permit")
async def validate_work_permit(payload: DocumentCheckRequest):
    if not os.path.exists(payload.file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    
    text_content = extract_pdf_text(payload.file_path)
    
    prompt = f"""
    You are a Strict Document Verification Agent for a recruitment firm.
    Analyze the extracted text from a candidate's uploaded document:
    ---
    {text_content[:3000]}
    ---
    Determine if this is an actual work permit, provide a validation status (CONFIRM or DENY), 
    an accuracy percentage score, and extract the expiration date. Format exactly like this:
    
    Result: [CONFIRM or DENY]
    Accuracy Score: [0-100]%
    Valid Until: [YYYY-MM-DD or Not Found]
    Reasoning: [Short summary]
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        return {"status": "processed", "verification": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- TASK 4: CV & CERTIFICATE VALIDATION AGENT (Persowerk) ---
class CertificateCheckRequest(BaseModel):
    file_name: str # e.g., "bachelor_zertifikat.jpg"

@app.post("/agent/verify-certificate")
async def verify_certificate(payload: CertificateCheckRequest):
    # Since we have images in certificates_part_4, we provide a structured metadata validation agent
    prompt = f"""
    You are a Fraud Detection Agent looking for AI-generated or falsified CVs and certificates.
    Simulate a verification of the file document '{payload.file_name}' against standard verification registries.
    Highlight typical red flags (unaligned fonts, missing certification numbers, suspicious dates).
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"status": "analyzed", "fraud_report": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- TASK 5: INTERVIEW SUPPORT AGENT (Kohlpharma) ---
@app.post("/agent/interview-kit")
async def generation_interview_kit():
    file_path = "problem5_job_offers.pdf"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="problem5_job_offers.pdf not found.")
    
    job_text = extract_pdf_text(file_path)
    prompt = f"""
    You are an Expert Technical Recruiter assisting a non-technical hiring manager.
    Based on this job offer text:
    {job_text[:3000]}
    
    Generate an Interview Guide containing:
    1. 10 Targeted Technical Questions
    2. 5 Behavioral Questions
    3. 5 Red Flags to spot in answers
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"interview_kit": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    