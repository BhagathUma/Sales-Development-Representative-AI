import { FollowupResponse } from "./followup";


export interface CompanyAnalysis {
  industry: string;
  company_summary: string;
  target_customers: string[];
  main_services: string[];
  business_model: string;
  pain_points: string[];
  ai_opportunities: string[];
}

export interface PainPointAnalysis {
  pain_points: string[];
  opportunities: string[];
  urgency_level: string;
}

export interface LeadScore {
  score: number;
  qualification: string;
  reasons: string[];
}

export interface Outreach {
  email_subject: string;
  email_body: string;
  linkedin_message: string;
  call_opener: string;
}

export interface SDRAnalysis {
  company_analysis: CompanyAnalysis;
  pain_points: PainPointAnalysis;
  lead_score: LeadScore;
  outreach: Outreach;
}

export interface SDRAnalysis {
  company_analysis: CompanyAnalysis;
  pain_points: PainPointAnalysis;
  lead_score: LeadScore;
  outreach: Outreach;

  followups?: {
    day3?: FollowupResponse;
    day7?: FollowupResponse;
    breakup?: FollowupResponse;
  };
}