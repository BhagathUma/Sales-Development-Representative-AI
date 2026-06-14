export async function
generateCompetitorAnalysis(
  companyAnalysis: any
) {

  const response =
    await fetch(
      "http://localhost:8000/competitor-analysis",
      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json"
        },

        body: JSON.stringify({
          company_analysis:
            companyAnalysis
        })
      }
    );

  return response.json();
}