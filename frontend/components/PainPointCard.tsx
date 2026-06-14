import { PainPointAnalysis }
from "@/types/analysis";

interface Props {
  data: PainPointAnalysis;
}

export default function PainPointCard({
  data,
}: Props) {

  return (
    <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

      <h2 className="text-xl font-bold">
        Pain Points
      </h2>

      <ul className="mt-4 space-y-2">

        {data.pain_points.map(
          (item, index) => (
            <li key={index}>
              • {item}
            </li>
          )
        )}

      </ul>

    </div>
  );
}