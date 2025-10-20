import Link from "next/link";
import { Avatar, Card } from "@/components/ui";
import { fetchProfile } from "@/lib/api";

export default async function ProfilePage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const data = await fetchProfile(id);
  return (
    <div className="flex flex-col gap-3">
      <Card>
        <div className="flex gap-3 p-3">
          <Avatar src={data.profile.avatar_url} alt={data.profile.display_name} />
          <div>
            <div className="text-xl font-semibold">{data.profile.display_name}</div>
            <div className="text-neutral-500">@{data.profile.handle}</div>
            {data.profile.bio && <p className="pt-2 text-sm">{data.profile.bio}</p>}
          </div>
        </div>
      </Card>
      {data.posts.map((p) => (
        <Card key={p.id}>
          <div className="flex gap-3 p-3">
            <Link href={`/profile/${data.profile.id}`} className="shrink-0">
              <Avatar src={data.profile.avatar_url} alt={data.profile.display_name} />
            </Link>
            <div className="min-w-0 flex-1">
              <div className="flex items-center gap-2">
                <span className="font-semibold">{data.profile.display_name}</span>
                <span className="text-sm text-neutral-500">@{data.profile.handle}</span>
                <span className="text-sm text-neutral-500">· {new Date(p.created_at).toLocaleString()}</span>
              </div>
              <p className="whitespace-pre-wrap break-words py-2">{p.text}</p>
            </div>
          </div>
        </Card>
      ))}
    </div>
  );
}
