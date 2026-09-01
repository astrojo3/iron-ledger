-- Iron Ledger — Supabase schema.
-- Run this once in your Supabase project: Dashboard -> SQL Editor -> New query -> paste -> Run.

create table if not exists workouts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users on delete cascade,
  date date not null,
  type text not null,
  exercises jsonb not null default '[]',
  duration int,
  notes text,
  created_at timestamptz not null default now()
);

create table if not exists measurements (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users on delete cascade,
  date date not null,
  weight numeric,
  bf numeric,
  neck numeric,
  chest numeric,
  waist numeric,
  arms numeric,
  thighs numeric,
  created_at timestamptz not null default now()
);

alter table workouts enable row level security;
alter table measurements enable row level security;

-- Each signed-in user can only ever see or touch their own rows.
create policy "own workouts" on workouts
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

create policy "own measurements" on measurements
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- Turn on realtime so changes push live to every open device.
alter publication supabase_realtime add table workouts;
alter publication supabase_realtime add table measurements;
