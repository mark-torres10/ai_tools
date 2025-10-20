import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Social Media App",
  description: "Twitter-like feed with profiles",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased min-h-screen bg-neutral-50 dark:bg-black text-neutral-900 dark:text-neutral-50`}>
        <div className="mx-auto max-w-2xl p-4">
          <header className="sticky top-0 z-10 mb-4 border-b border-neutral-200 bg-white/80 p-3 backdrop-blur dark:border-neutral-800 dark:bg-black/60">
            <h1 className="text-xl font-semibold">Home</h1>
          </header>
          {children}
        </div>
      </body>
    </html>
  );
}
