"use client";

import { useRef, useState } from "react";

import { Search, Copy } from "lucide-react";

import { motion } from "framer-motion";

import { cn } from "@/lib/utils";

import toast from "react-hot-toast";
import React from "react";
import UrlInput from "@/components/UrlInput";
import CompanyCard from "@/components/CompanyCard";
import PainPointCard from "@/components/PainPointCard";
import LeadScoreCard from "@/components/LeadScoreCard";
import OutreachCard from "@/components/OutreachCard";
import FollowupCard from "@/components/FollowupCard";
import AgentTimeline from "@/components/AgentTimeline";
import { rewriteTone } from "@/services/api";
import { analyzeLead,  } from "@/services/api";
import {CompetitorAnalysis} from "@/types/competitor";
import { Outreach, SDRAnalysis } from "@/types/analysis";

import { FollowupResponse } from "@/types/followup";
import { generateFollowup } from "@/services/followup";
import { generateCompetitorAnalysis } from "@/services/competitor";
import CompetitorCard from "@/components/CompetitorCard";
import {exportReport} from "@/services/exportReport";












type ToneResponse = Outreach;

export default function Home() {
  const [selectedTone, setSelectedTone] =
    useState("professional");
  const [
  exportLoading,
  setExportLoading
] = useState(false);
  const [toneLoading, setToneLoading] =
    useState(false);

  const [toneCache, setToneCache] =
    useState<Record<string, ToneResponse>>(
      {}
    );

    const [
  competitorAnalysis,
  setCompetitorAnalysis
] =
useState<
  CompetitorAnalysis | null
>(null);

const [
  competitorLoading,
  setCompetitorLoading
] =
useState(false);
  
  const [followupCache,setFollowupCache] = useState<Record<string,FollowupResponse>>({});
  const [followupLoading,setFollowupLoading] =useState(false);

  const [url, setUrl] = useState("");

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const [currentStep, setCurrentStep] =
    useState(-1);

  const [analysis, setAnalysis] =
    useState<SDRAnalysis | null>(null);

  const dashboardRef =
    useRef<HTMLDivElement>(null);

  const [selectedFollowup,setSelectedFollowup] =useState("");

  function isValidUrl(value: string) {
    try {
      new URL(value);
      return true;
    } catch {
      return false;
    }
  }



  async function handleAnalyze() {
    if (!url.trim()) {
      toast.error(
        "Please enter a company URL"
      );
      return;
    }

    if (!isValidUrl(url)) {
      toast.error(
        "Please enter a valid URL"
      );
      return;
    }

    try {
      setLoading(true);

      setError("");

      setAnalysis(null);

      setCurrentStep(0);

      setTimeout(
        () => setCurrentStep(1),
        1000
      );

      setTimeout(
        () => setCurrentStep(2),
        3000
      );

      setTimeout(
        () => setCurrentStep(3),
        7000
      );

      const result =
        await analyzeLead(url);

      setAnalysis(result);

      toast.success(
        "Lead Analysis Complete"
      );

      setTimeout(() => {
        dashboardRef.current?.scrollIntoView({
          behavior: "smooth",
        });
      }, 300);

    } catch (err) {
      console.error(err);

      setError(
        "Failed to analyze company"
      );

      toast.error(
        "Analysis failed"
      );

    } finally {
      setLoading(false);
    }
  }

  async function
handleExportReport() {

  if (!analysis) return;

  try {

    setExportLoading(true);

    const payload = {

      company_analysis:
        company,

      pain_points:
        painPoints,

      lead_score:
        leadScore,

      outreach:
        outreach,

      competitor_analysis:
        competitorAnalysis,

      followups:
        followupCache,
    };

    const blob =
      await exportReport(
        payload
      );

    const url =
      window.URL.createObjectURL(
        blob
      );

    const link =
      document.createElement(
        "a"
      );

    link.href = url;

    link.download =
      "Sales_Intelligence_Report.pdf";

    document.body.appendChild(
      link
    );

    link.click();

    link.remove();

    window.URL.revokeObjectURL(
      url
    );

  } catch (error) {

    console.error(error);

  } finally {

    setExportLoading(false);

  }
}

  async function handleToneChange(
  tone: string
) {
  setSelectedTone(tone);

  if (toneCache[tone]) {
    return;
  }

  try {
    setToneLoading(true);

    const result =
      await rewriteTone(
        tone,
        company,
        painPoints,
        leadScore
      );

    setToneCache((prev) => ({
      ...prev,
      [tone]: result,
    }));
  } catch (error) {
    console.error(error);

    toast.error(
      "Failed to generate tone"
    );
  } finally {
    setToneLoading(false);
  }
}

  async function handleFollowupClick(
  type: string
) {
  setSelectedFollowup(type);

  if (followupCache[type]) {
    return;
  }

  try {
    setFollowupLoading(true);

    const result =
      await generateFollowup(
        type,
        analysis!
      );

    setFollowupCache((prev) => ({
      ...prev,
      [type]: result,
    }));

    setAnalysis(prev => {

  if (!prev) return prev;

  return {
    ...prev,

    followups: {
      ...prev.followups,

      [type]: result
    }
  };

});

  } catch (error) {

    console.error(error);

    toast.error(
      "Failed to generate follow-up"
    );

  } finally {

    setFollowupLoading(false);

  }
}


async function
handleCompetitorAnalysis() {

  if (
    competitorAnalysis
  ) {
    return;
  }

  try {

    setCompetitorLoading(
      true
    );

    const result =
      await generateCompetitorAnalysis(
        company!
      );

    setCompetitorAnalysis(
      result
    );

  } finally {

    setCompetitorLoading(
      false
    );

  }
}

  const company =
    analysis?.company_analysis;

  const painPoints =
    analysis?.pain_points;

  const leadScore =
    analysis?.lead_score;

  const outreach =
    analysis?.outreach;
  const currentOutreach =
  toneCache[selectedTone] ||
  outreach;

  function copyEmail() {
    if (!outreach) return;

    navigator.clipboard.writeText(
      outreach.email_body
    );

    toast.success(
      "Email copied"
    );
  }

  function copyLinkedIn() {
    if (!outreach) return;

    navigator.clipboard.writeText(
      outreach.linkedin_message
    );

    toast.success(
      "LinkedIn message copied"
    );
  }

  

  return (
    <main className={cn(
  "relative min-h-screen bg-black text-white px-16 py-16",
  "w-full", // Ensures it takes full width
  "[background-size:40px_40px]",
  "[background-image:radial-gradient(#d4d4d4_1px,transparent_1px)]",
  "dark:[background-image:radial-gradient(#50C878_2px,transparent_1px)]"
)}>
      <div className="mx-auto max-w-6xl"
      >

        {/* HERO */}

        <div className="text-center">
          <h1 className="text-6xl font-bold py-10">
            ScaleSDR
          </h1>

          <p className="mt-6 text-lg text-slate-400 max-w-3xl mx-auto">
            Human-grade outreach at machine-scale.
          </p>
        </div>

        {/* INPUT */}

        <div className="mt-12 rounded-2xl border border-neutral-800 bg-neutral-900/40 backdrop-blur-md p-6 shadow-xl">
          <UrlInput
            url={url}
            setUrl={setUrl}
          />

          <button
            onClick={handleAnalyze}
            disabled={loading}
            className="
              mt-4
              w-full
              flex
              items-center
              justify-center
              gap-2
              rounded-lg
              bg-neutral-900
              px-4
              py-3
              font-medium
              hover:bg-neutral-800
            "
          >
            <Search size={18} />

            {loading
              ? "Analyzing..."
              : "Analyze Lead"}
          </button>
        </div>

        {/* ERROR */}

        {error && (
          <div className="mt-6 rounded-xl border border-red-500 p-4 text-red-400">
            {error}
          </div>
        )}

        {/* AGENT TIMELINE */}

        {loading && (
          <div className="mt-8">
            <AgentTimeline
              currentStep={currentStep}
            />
          </div>
        )}

        {/* DASHBOARD */}

        {analysis && (
          <div
            ref={dashboardRef}
            className="mt-10 space-y-6"
          >
            {/* KPI BANNER */}

            <motion.div
              initial={{
                opacity: 0,
                y: 20,
              }}
              animate={{
                opacity: 1,
                y: 0,
              }}
              className="
                rounded-2xl
                border
                border-slate-800
                bg-neutral-900/40 backdrop-blur-xl border border-white/10
                p-6
              "
            >
              <h2 className="text-xl font-bold">
                SDR Summary
              </h2>

              <div className="mt-4 grid md:grid-cols-3 gap-4">

                <div>
                  <p className="text-slate-400">
                    Agents Executed
                  </p>

                  <p className="text-3xl font-bold">
                    4
                  </p>
                </div>

                <div>
                  <p className="text-slate-400">
                    Lead Score
                  </p>

                  <p className="text-3xl font-bold">
                    {leadScore?.score}
                  </p>
                </div>

                <div>
                  <p className="text-slate-400">
                    Qualification
                  </p>

                  <p className="text-3xl font-bold">
                    {
                      leadScore?.qualification
                    }
                  </p>
                </div>

              </div>
            </motion.div>

            {/* COMPANY */}

            <motion.div
              initial={{
                opacity: 0,
                y: 20,
              }}
              animate={{
                opacity: 1,
                y: 0,
              }}
              transition={{
                delay: 0.2,
              }}
            >
              <CompanyCard
                data={company!}
              />
            </motion.div>

            {/* PAIN POINTS + SCORE */}

            <div className="grid md:grid-cols-2 gap-6">

              <motion.div
                initial={{
                  opacity: 0,
                  y: 20,
                }}
                animate={{
                  opacity: 1,
                  y: 0,
                }}
                transition={{
                  delay: 0.4,
                }}
              >
                <PainPointCard
                  data={painPoints!}
                />
              </motion.div>

              <motion.div
                initial={{
                  opacity: 0,
                  y: 20,
                }}
                animate={{
                  opacity: 1,
                  y: 0,
                }}
                transition={{
                  delay: 0.6,
                }}
              >
                <LeadScoreCard
                  data={leadScore!}
                />
              </motion.div>

            </div>

            {/* OUTREACH */}

            <motion.div
              initial={{
                opacity: 0,
                y: 20,
              }}
              animate={{
                opacity: 1,
                y: 0,
              }}
              transition={{
                delay: 0.8,
              }}
            >
              <OutreachCard
              data={currentOutreach}
              selectedTone={selectedTone}
              onToneChange={
                handleToneChange
              }
              toneCache={toneCache}
              toneLoading={toneLoading}
            />
            </motion.div>
            

            {/* COPY ACTIONS */}

            <div className="flex flex-wrap gap-4">

              <button
                onClick={copyEmail}
                className="
                  flex
                  items-center
                  gap-2
                  rounded-lg
                  bg-neutral-800 border border-white/50
                  px-4
                  py-2
                "
              >
                <Copy size={16} />
                Copy Email
              </button>

              <button
                onClick={copyLinkedIn}
                className="
                  flex
                  items-center
                  gap-2
                  rounded-lg
                  bg-neutral-800 border border-white/50
                  px-4
                  py-2
                "
              >
                <Copy size={16} />
                Copy LinkedIn Message
              </button>

            </div>




              <FollowupCard
  selectedFollowup={
    selectedFollowup
  }
  followupLoading={
    followupLoading
  }
  followupCache={
    followupCache
  }
  onSelect={
    handleFollowupClick
  }
/>



            

            <CompetitorCard
  data={
    competitorAnalysis
  }
  loading={
    competitorLoading
  }
  onGenerate={
    handleCompetitorAnalysis
  }
/>

            {/* AGENT STATS */}

            <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

              <h2 className="text-xl font-bold">
                Agent Statistics
              </h2>

              <div className="mt-4 space-y-3">

                <p>
                  ⏳ Research Agent:
                  Company Intelligence Generated
                </p>

                <p>
                  ⏳ Pain Point Agent:
                  {
                    painPoints?.pain_points
                      ?.length
                  }{" "}
                  Pain Points Found
                </p>

                <p>
                  ⏳ Lead Scoring Agent:
                  {
                    leadScore?.score
                  }
                  /100
                </p>

                <p>
                  ⏳ Outreach Agent:
                  4 Outreach Assets Generated
                </p>

              </div>

            </div>

            <div
  className="
    rounded-2xl
    border
    border-slate-800
    bg-neutral-900/40 backdrop-blur-md border border-white/10
    p-6
  "
>

  <h2 className="text-xl font-bold">
    SDR Intelligence Report
  </h2>

  <p className="mt-2 text-slate-400">
    Download a complete
    AI-generated sales brief.
  </p>

  <button
    onClick={
      handleExportReport
    }
    disabled={
      exportLoading
    }
    className="
      mt-6
      rounded-lg
      bg-neutral-800 border border-white/50
      px-4
      py-2
      text-white
      bg-neutral-600 border border-white/50
    "
  >
    {
      exportLoading
      ? "Generating..."
      : "Download Report"
    }
  </button>

</div>

          </div>
          
        )}

        
        {/* FOOTER */}

        <footer className="mt-20 text-center ">
          Built for FlowZint AI Hackathon 2026
        </footer>

      </div>
    </main>
  );
}