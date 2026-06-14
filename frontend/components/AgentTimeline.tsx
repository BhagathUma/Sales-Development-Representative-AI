interface Props {
  currentStep: number;
}

const agents = [
  "Research Agent",
  "Pain Point Agent",
  "Lead Scoring Agent",
  "Outreach Agent",
];

export default function AgentTimeline({
  currentStep,
}: Props) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

      <h2 className="text-xl font-bold">
        Agent Activity
      </h2>

      <div className="mt-6 space-y-4">

        {agents.map((agent, index) => {

          const active =
            index <= currentStep;

          return (
            <div
              key={agent}
              className="
                flex
                items-center
                gap-3
              "
            >

              <div
                className={`
                  h-3
                  w-3
                  rounded-full
                  ${
                    active
                      ? "bg-green-500"
                      : "bg-slate-700"
                  }
                `}
              />

              <span>
                {agent}
              </span>

            </div>
          );
        })}

      </div>

    </div>
  );
}