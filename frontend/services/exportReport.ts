import { SDRAnalysis } from "@/types/analysis";

export async function exportReport(
  payload: any
) {

  const response =
    await fetch(
      "http://localhost:8000/export-report",
      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json",
        },

        body: JSON.stringify(
          payload
        ),
      }
    );

  if (!response.ok) {

    throw new Error(
      "Failed to export report"
    );

  }

  return response.blob();
}