import { Outreach } from "@/types/analysis";



interface Props {
  data: any;

  selectedTone: string;

  onToneChange: (
    tone: string
  ) => void;

  toneCache:
    Record<string, any>;

  toneLoading: boolean;
}



export default function OutreachCard({
  data,
  selectedTone,
  onToneChange,
  toneCache,
  toneLoading,
}: Props) {

  const tones = [
    "professional",
    "executive",
    "friendly",
    "consultative",
    "challenger",
  ];
  return (
    <div className="rounded-2xl border border-slate-800 bg-neutral-900/40 backdrop-blur-md border border-white/10 p-6">

      <h2 className="text-xl font-bold">
        Personalized Outreach
      </h2>

      <div className="mt-6">

        <p className="font-semibold">
          Subject
        </p>

        <p>{data?.email_subject}</p>

      </div>
      <div className="flex flex-wrap gap-2 mb-6">

  {tones.map((tone) => (

    <button
      key={tone}
      onClick={() =>
        onToneChange(tone)
      }
      className={`
        px-3
        py-2
        rounded-lg

        ${
          selectedTone === tone
            ? "bg-neutral-800 border border-white/50"
            : "bg-neutral-700 border border-white/50"
        }
      `}
    >
      {tone}

      {toneCache[tone]
        ? " ✓"
        : ""}
    </button>

  ))}
{
  toneLoading && (
    <div className="mb-4 text-slate-400">
      Generating tone...
    </div>
  )
}
</div>
      
      <div className="mt-6">

        <p className="font-semibold">
          Email
        </p>

        <p className="whitespace-pre-wrap">
          {data?.email_body}
        </p>

      </div>

      <div className="mt-6">

        <p className="font-semibold">
          LinkedIn Message
        </p>

        <p>
          {data?.linkedin_message}
        </p>

      </div>

      <div className="mt-6">

        

      </div>

    </div>
  );
}