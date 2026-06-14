import { LeadScore }
from "@/types/analysis";

interface Props {
  data: LeadScore;
}

export default function LeadScoreCard({
  data,
}: Props) {

  const color =
    data.score >= 80
      ? "text-green-400"
      : data.score >= 50
      ? "text-yellow-400"
      : "text-red-400";

  return (
    <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

        <span
  className="
    inline-block
    rounded-full
    bg-green-500/20
    px-3
    py-1
  "
>
  {data.qualification}
</span>

      <h2 className="text-xl font-bold">
        Lead Score
      </h2>

      <div
        className={`mt-4 text-5xl font-bold ${color}`}
      >
        {data.score}
      </div>

      <div className="mt-4 h-3 rounded-full bg-slate-700">
        <div
            className="h-3 rounded-full bg-green-500"
            style={{
            width: `${data.score}%`
            }}
        />
        </div>

      <div className="mt-2">
        {data.qualification}
      </div>

    </div>
  );
}