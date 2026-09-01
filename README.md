# Iron Ledger — self-hosted PWA

Installable training + physique tracker, synced across devices via Supabase.

## One-time setup

1. **Supabase** (free tier): create a project at supabase.com. In the SQL Editor,
   run `supabase-setup.sql` from this folder. Then go to Project Settings -> API
   and copy the **Project URL** and **anon public key**.
2. Paste those into `index.html`, near the top of the `<script>` block:
   ```js
   var SUPABASE_URL = "https://xxxx.supabase.co";
   var SUPABASE_ANON_KEY = "eyJ...";
   ```
3. **GitHub Pages**: push this folder to a GitHub repo, then in the repo's
   Settings -> Pages, set the source to the `main` branch, root folder.
   Your app will be live at `https://<username>.github.io/<repo>/`.
4. Open that URL on your phone, tap Share -> **Add to Home Screen** (iOS) or
   the install prompt (Android/Chrome). It launches full-screen, no browser bar.

## Signing in

The app uses passwordless email sign-in (magic link) — enter your email in the
header, click the link Supabase emails you, and you're synced. Same email on
every device gets the same log.

## Files

- `index.html` — the whole app
- `manifest.json` / `sw.js` — makes it installable + launches offline
- `icons/` — app icons
- `supabase-setup.sql` — run once to create the two tables + security rules
