"use client";

interface UrlInputProps {
  url: string;
  setUrl: (url: string) => void;
}

export default function UrlInput({
  url,
  setUrl,
}: UrlInputProps) {
  return (
    <input
      type="text"
      value={url}
      onChange={(e) =>
        setUrl(e.target.value)
      }
      placeholder="https://company.com"
      className="
        w-full
        rounded-lg
        border
        px-4
        py-3
      "
    />
  );
}