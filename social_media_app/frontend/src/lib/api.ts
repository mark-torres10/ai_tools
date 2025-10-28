export type Profile = {
  id: string;
  handle: string;
  display_name: string;
  bio?: string | null;
  avatar_url?: string | null;
};

export type Post = {
  id: string;
  author_id: string;
  text: string;
  created_at: string;
  like_count: number;
  comment_count: number;
  share_count: number;
};

export type PostWithAuthor = Post & { author: Profile };

export type FeedResponse = {
  items: PostWithAuthor[];
  next_cursor?: string | null;
};

export type ProfileResponse = {
  profile: Profile;
  posts: Post[];
};

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";

async function http<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers || {}),
    },
    cache: "no-store",
  });
  if (!res.ok) {
    throw new Error(`Request failed: ${res.status}`);
  }
  return (await res.json()) as T;
}

export async function fetchFeed(cursor?: string | null, limit = 20): Promise<FeedResponse> {
  const params = new URLSearchParams();
  if (cursor) params.set("cursor", cursor);
  params.set("limit", String(limit));
  return http<FeedResponse>(`/feed?${params.toString()}`);
}

export async function fetchProfile(profileId: string): Promise<ProfileResponse> {
  return http<ProfileResponse>(`/profiles/${profileId}`);
}

export async function likePost(postId: string, userId: string) {
  return http(`/posts/${postId}/like`, {
    method: "POST",
    body: JSON.stringify({ user_id: userId }),
  });
}

export async function commentPost(postId: string, userId: string, text: string) {
  return http(`/posts/${postId}/comment`, {
    method: "POST",
    body: JSON.stringify({ user_id: userId, text }),
  });
}

export async function sharePost(postId: string, userId: string) {
  return http(`/posts/${postId}/share`, {
    method: "POST",
    body: JSON.stringify({ user_id: userId }),
  });
}
