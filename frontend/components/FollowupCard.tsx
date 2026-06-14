"use client";

import { FollowupResponse } from "@/types/followup";

interface FollowupCardProps {
  selectedFollowup: string;

  followupLoading: boolean;

  followupCache: Record<
    string,
    FollowupResponse
  >;

  onSelect: (
    type: string
  ) => void;
}

const followupOptions = [
  {
    key: "day3",
    label: "Day 3",
  },

  {
    key: "day7",
    label: "Day 7",
  },

  {
    key: "breakup",
    label: "Breakup",
  },
];

export default function FollowupCard({
  selectedFollowup,
  followupLoading,
  followupCache,
  onSelect,
}: FollowupCardProps) {

  const currentFollowup =
    selectedFollowup
      ? followupCache[
          selectedFollowup
        ]
      : null;

  return (
    <div
      className="
        rounded-2xl
        border
        bg-neutral-900/40
        bg-neutral-900/40 backdrop-blur-xl border border-white/10
        p-6
      "
    >
      <h2 className="text-xl font-bold">
        Follow-Up Sequences
      </h2>

      <p className="mt-2 text-slate-400">
        Generate follow-up outreach
        based on the original email.
      </p>

      {/* Buttons */}

      <div className="mt-6 flex flex-wrap gap-3">

        {followupOptions.map(
          (option) => {

            const generated =
              !!followupCache[
                option.key
              ];

            const active =
              selectedFollowup ===
              option.key;

            return (
              <button
                key={option.key}
                onClick={() =>
                  onSelect(
                    option.key
                  )
                }
                className={`
                  rounded-lg
                  px-4
                  py-2
                  text-sm
                  font-medium
                  transition

                  ${
                    active
                      ? "bg-neutral-800 border border-white/50"
                      : "bg-neutral-700 border border-white/50"
                  }
                `}
              >
                {generated
                  ? "✓ "
                  : ""}
                {option.label}
              </button>
            );
          }
        )}

      </div>

      {/* Loading */}

      {followupLoading && (
        <div className="mt-6">
          <p className="text-slate-400">
            Generating follow-up...
          </p>
        </div>
      )}

      {/* Empty State */}

      {!followupLoading &&
        !currentFollowup && (
          <div
            className="
              mt-6
              rounded-lg
              border
              border-dashed
              border-slate-700
              p-6
              text-center
              text-slate-500
            "
          >
            Select Day 3, Day 7,
            or Breakup Email to
            generate a follow-up.
          </div>
        )}

      {/* Follow-Up Content */}

      {!followupLoading &&
        currentFollowup && (
          <div className="mt-6 space-y-6">

            <div>
              <h3 className="font-semibold">
                Subject
              </h3>

              <p className="mt-2 text-slate-300">
                {
                  currentFollowup.subject
                }
              </p>
            </div>

            <div>
              <h3 className="font-semibold">
                Email
              </h3>

              <div
                className="
                  mt-2
                  whitespace-pre-wrap
                  rounded-lg
                  border-slate-300
                  bg-neutral-950
                  p-4
                  text-slate-300
                  
                "
              >
                {
                  currentFollowup.email_body
                }
              </div>
            </div>

          </div>
        )}
    </div>
  );
}