import { SDRAnalysis }
from "../types/analysis";

const API_BASE_URL =
  "http://localhost:8000";

export async function analyzeLead(
  url: string
): Promise<SDRAnalysis> {

  const response = await fetch(
    `${API_BASE_URL}/analyze-lead?url=${encodeURIComponent(url)}`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to analyze lead"
    );
  }

  return response.json();
}

export async function rewriteTone(
  tone: string,
  companyAnalysis: any,
  painPoints: any,
  leadScore: any
) {
  const response = await fetch(
    "http://localhost:8000/rewrite-tone",
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        tone,
        company_analysis:
          companyAnalysis,
        pain_points:
          painPoints,
        lead_score:
          leadScore,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to rewrite tone"
    );
  }

  return response.json();
}