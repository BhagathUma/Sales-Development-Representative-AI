import { CompanyAnalysis }
from "@/types/analysis";

interface Props {
  data: CompanyAnalysis;
}

export default function CompanyCard({
  data,
}: Props) {

  return (
    <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">


        <div className="flex flex-wrap gap-2">

  {data.main_services?.map(
    service => (
      <span
        key={service}
        className="
          rounded-full
          bg-neutral-800 border border-white/50
          px-3
          py-1
          text-sm
        "
      >
        {service}
      </span>
    )
  )}

</div>



      <h2 className="text-xl font-bold">
        Company Analysis
      </h2>

      <div className="mt-4 space-y-4">

        <div>
          <p className="text-slate-400">
            Industry
          </p>

          <p>{data.industry}</p>
        </div>

        <div>
          <p className="text-slate-400">
            Business Model
          </p>

          <p>{data.business_model}</p>
        </div>

        <div>
          <p className="text-slate-400">
            Summary
          </p>

          <p>{data.company_summary}</p>
        </div>

      </div>

    </div>
  );
}