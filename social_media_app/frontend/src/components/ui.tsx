import React from "react";

export function Card({ children }: { children: React.ReactNode }) {
  return (
    <div className="rounded-xl border border-gray-200 bg-white shadow-sm dark:border-gray-800 dark:bg-neutral-900">
      {children}
    </div>
  );
}

export function Button({ children, onClick, variant = "ghost", disabled }: { children: React.ReactNode; onClick?: () => void; variant?: "ghost" | "primary"; disabled?: boolean; }) {
  const base = "inline-flex items-center gap-2 rounded-md px-3 py-1.5 text-sm transition-colors";
  const styles = variant === "primary" ? "bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50" : "hover:bg-neutral-100 dark:hover:bg-neutral-800 disabled:opacity-50";
  return (
    <button onClick={onClick} disabled={disabled} className={`${base} ${styles}`}>
      {children}
    </button>
  );
}

export function Avatar({ src, alt }: { src?: string | null; alt: string }) {
  return (
    <img src={src || "/vercel.svg"} alt={alt} className="h-10 w-10 rounded-full object-cover" />
  );
}

export function Textarea({ value, onChange, placeholder }: { value: string; onChange: (v: string) => void; placeholder?: string; }) {
  return (
    <textarea
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      className="w-full resize-none rounded-md border border-neutral-200 bg-white p-2 text-sm outline-none focus:ring-2 focus:ring-blue-500 dark:border-neutral-800 dark:bg-neutral-900"
      rows={3}
    />
  );
}
