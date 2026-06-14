import {
  CompetitorAnalysis
} from "@/types/competitor";

interface Props {

  data: CompetitorAnalysis | null;

  loading: boolean;

  onGenerate: () => void;
}

export default function CompetitorCard({
  data,
  loading,
  onGenerate
}: Props) {

  if (!data) {

    return (
      <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

        <h2 className="text-xl font-bold">
          Competitor Analysis
        </h2>

        <button
          onClick={onGenerate}
          className="
            mt-6
            rounded-lg
            bg-neutral-800 border border-white/50
            px-4
            py-2
          "
        >
          {
            loading
            ? "Generating..."
            : "Generate Analysis"
          }
        </button>

      </div>
    );
  }

  return (
    <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

      <h2 className="text-xl font-bold">
        Competitor Analysis
      </h2>

      <div className="mt-4">

        <p>
          <strong>
            Main Competitor:
          </strong>
          {" "}
          {data.main_competitor}
        </p>

      </div>

      <div className="mt-4">

        <p className="font-semibold">
          Sales Wedge
        </p>

        <p>
          {data.sales_wedge}
        </p>

      </div>

    </div>
  );
}