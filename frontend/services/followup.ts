import { SDRAnalysis }
from "@/types/analysis";

const API_BASE_URL =
  "http://localhost:8000";

export async function generateFollowup(
  followupType: string,
  analysis: SDRAnalysis
) {

  const response = await fetch(
    `${API_BASE_URL}/followup`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify({
        followup_type:
          followupType,

        company_analysis:
          analysis.company_analysis,

        pain_points:
          analysis.pain_points,

        lead_score:
          analysis.lead_score,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to generate follow-up"
    );
  }

  return response.json();
}