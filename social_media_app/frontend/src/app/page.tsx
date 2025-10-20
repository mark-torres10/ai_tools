"use client";
import useSWRInfinite from "swr/infinite";
import Link from "next/link";
import { Avatar, Button, Card, Textarea } from "@/components/ui";
import { fetchFeed, likePost, commentPost, sharePost, PostWithAuthor } from "@/lib/api";
import { useEffect, useRef, useState } from "react";

type PageData = { next_cursor?: string | null } | null;

const getKey = (pageIndex: number, previousPageData: PageData) => {
  if (previousPageData && !previousPageData?.next_cursor) return null;
  if (pageIndex === 0) return { cursor: null };
  return { cursor: previousPageData?.next_cursor ?? null };
};

export default function Home() {
  const { data, size, setSize, isValidating, mutate } = useSWRInfinite(
    getKey,
    async (key: { cursor: string | null }) => fetchFeed(key.cursor)
  );

  const items = (data?.flatMap((p) => p.items) || []) as PostWithAuthor[];
  const nextCursor = data?.[data.length - 1]?.next_cursor ?? null;
  const [commenting, setCommenting] = useState<Record<string, string>>({});
  const currentUser = "u01";
  const loadMoreRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!nextCursor) return;
    const el = loadMoreRef.current;
    if (!el) return;
    const obs = new IntersectionObserver((entries) => {
      const entry = entries[0];
      if (entry.isIntersecting) {
        setSize((s) => s + 1);
      }
    }, { rootMargin: "200px" });
    obs.observe(el);
    return () => {
      obs.disconnect();
    };
  }, [nextCursor, setSize]);

  return (
    <div className="flex flex-col gap-3">
      {items.map((item) => (
        <Card key={item.id}>
          <div className="flex gap-3 p-3">
            <Link href={`/profile/${item.author_id}`} className="shrink-0">
              <Avatar src={item.author.avatar_url} alt={item.author.display_name} />
            </Link>
            <div className="min-w-0 flex-1">
              <div className="flex items-center gap-2">
                <Link href={`/profile/${item.author_id}`} className="font-semibold hover:underline">
                  {item.author.display_name}
                </Link>
                <span className="text-sm text-neutral-500">@{item.author.handle}</span>
                <span className="text-sm text-neutral-500">· {new Date(item.created_at).toLocaleString()}</span>
              </div>
              <p className="whitespace-pre-wrap break-words py-2">{item.text}</p>
              <div className="flex items-center gap-3 pt-1">
                <Button onClick={async () => { await likePost(item.id, currentUser); await mutate(); }}>❤️ {item.like_count}</Button>
                <Button onClick={async () => { await sharePost(item.id, currentUser); await mutate(); }}>🔁 {item.share_count}</Button>
              </div>
              <div className="pt-2">
                <Textarea
                  value={commenting[item.id] || ""}
                  onChange={(v) => setCommenting((s) => ({ ...s, [item.id]: v }))}
                  placeholder="Write a comment"
                />
                <div className="mt-1 flex justify-end">
                  <Button variant="primary" onClick={async () => { const text = commenting[item.id] || ""; if (!text.trim()) return; await commentPost(item.id, currentUser, text); setCommenting((s) => ({ ...s, [item.id]: "" })); await mutate(); }}>Comment ({item.comment_count})</Button>
                </div>
              </div>
            </div>
          </div>
        </Card>
      ))}
      <div className="py-4 text-center" ref={loadMoreRef}>
        {nextCursor ? (
          <Button onClick={() => setSize(size + 1)} disabled={isValidating}>Load more</Button>
        ) : (
          <span className="text-sm text-neutral-500">You are all caught up</span>
        )}
      </div>
    </div>
  );
}
