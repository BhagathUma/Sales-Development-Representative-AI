export type FollowupType =
  | "day3"
  | "day7"
  | "breakup";

  export interface FollowupResponse {
  followup_type: string;

  subject: string;

  email_body: string;
}