# Vijay Krishna P J — freelance developer portfolio

## Assumptions and launch status
- Vite + React + Tailwind CSS, with custom CSS for the visual design. No UI component library.
- Projects are independent technical work, not claimed paid client engagements. All reported metrics come from the supplied brief.
- No project URLs or photo were supplied: project buttons stay hidden and the portrait is explicitly a placeholder.
- A one-page resume is included, generated only from supplied details. Review or replace it before launch.
- Budget choices describe budget readiness; no monetary ranges or prices were invented. Edit `budgets` in `src/data.js` to add your preferred ranges.
- The Web3Forms integration needs your public access key. Without it the form displays an honest setup error and points visitors to email/WhatsApp. No message delivery has been tested.
- The included hosted version is private. Use a public deployment below to reach clients and search engines.
- Production compilation passes. Lighthouse 90+ is a target, not a measured result. Browser/device QA and WCAG conformance have not been certified in this environment.

## Run locally
1. Install Node.js 22 LTS or a compatible newer LTS release.
2. Extract this archive and open a terminal in `vijay-portfolio`.
3. Run `npm ci`.
4. Copy `.env.example` to `.env.local`.
5. Put your Web3Forms public access key in `VITE_WEB3FORMS_KEY`. Obtain it for your email at https://web3forms.com. The public form key is designed to be sent by browsers; never place a secret token in a `VITE_` variable.
6. Run `npm run dev` and open the URL printed in the terminal.
7. Run `npm run build` to create `dist`; `npm run preview` serves the production output locally.

## Edit content
- `src/data.js`: owner/contact links, photo path, resume path, services, projects, process, grouped skills and budget choices.
- `src/components/Hero.jsx` and `About.jsx`: headline and personal bio.
- `src/styles.css`: CSS variables, typography, spacing, breakpoints, light/dark colors.
- Project `demo` and `github` values: keep empty until a real URL exists. Never paste bracket placeholders as links.
- Place an optimized WebP/AVIF photo in `public` and set `owner.photo` to its URL. Preserve explicit image dimensions. For GitHub project Pages use a base-aware path.
- Replace `public/resume.pdf` with your approved resume; the button downloads this file. Optional `scripts/create-resume.py` requires Python, ReportLab and the DejaVu fonts at the paths used in the script.
- A commented-out testimonials insertion point is in `src/App.jsx`. Enable only with real quotes and permission.

## Set your public URL
Before deployment run:

```sh
node scripts/set-site-url.mjs https://your-domain.com
npm run build
```

This updates canonical, Open Graph, Twitter image, JSON-LD, sitemap and robots origins. A project Pages URL may include `/repository-name`. The `.env.example` site URL is only a reminder; metadata is static and changed with this script. Do not leave the private preview URL as your public canonical.

## Free deployment
Hosting plans and limits can change; check the provider’s current terms, including commercial-use eligibility. Netlify or GitHub Pages are practical static-host options; Vercel Hobby may restrict commercial usage.

### Netlify
1. Push the extracted source to a GitHub repository (exclude node_modules, dist, .env.local).
2. In Netlify choose Add new project / Import an existing project, then select the repository.
3. Use build command `npm run build` and publish directory `dist` (also set in netlify.toml).
4. Add `VITE_WEB3FORMS_KEY` in the build environment settings.
5. Deploy, then use the assigned public URL with the metadata script above and push the update.
6. Verify your form from the live domain. `public/_headers` adds security and asset cache headers.

### Vercel
1. Confirm your plan permits this commercial portfolio.
2. Import the source repository, choose Vite, build `npm run build`, output `dist`.
3. Add `VITE_WEB3FORMS_KEY` to project environment variables.
4. Deploy. Set your resulting public URL with the metadata script, commit and redeploy.
5. Security headers are defined in `vercel.json`.

### GitHub Pages
1. Push the source to a GitHub repository and open Settings / Pages / Source: GitHub Actions.
2. Use the supplied `.github/workflows/pages.yml`.
3. In Settings / Secrets and variables / Actions add repository variable `WEB3FORMS_KEY`.
4. For a project site, set the workflow base to `/YOUR_REPOSITORY/`; it defaults automatically to the repository name. For a `username.github.io` repository or custom root domain set it to `/`.
5. Set the full public canonical URL with the metadata script. Commit and push to `main`.
6. GitHub Pages ignores `_headers` and `vercel.json`; verify the host’s own headers.

## Launch checklist
- [ ] Confirm every email, phone, GitHub and LinkedIn link.
- [ ] Add real Inventory demo/repository URLs and other project links where available.
- [ ] Add your professional photo in WebP/AVIF.
- [ ] Review or replace `public/resume.pdf`.
- [ ] Add the Web3Forms public key and test a real delivery to your inbox.
- [ ] Check success, rejected submission, offline/timeout and empty/invalid input behavior.
- [ ] Configure available provider spam/domain controls; honeypot alone is not complete abuse prevention.
- [ ] Set the public canonical URL and check sitemap, robots and social-card image.
- [ ] Review mobile at 320, 360, 768, 1024, 1440 and 1920 px, both themes and 200% zoom.
- [ ] Keyboard-test menu, focus, skip link, case studies and form; test a screen reader.
- [ ] Run Lighthouse in Chrome on the production build in mobile mode; target 90+ Performance, Accessibility, Best Practices and SEO. Fix actual findings before claiming scores.
- [ ] Check reduced-motion, system theme and saved theme behavior.
- [ ] Submit your sitemap to search engines after public launch.

## After launch: three worthwhile improvements
1. Add privacy-conscious analytics for quote clicks and form completion; use evidence to improve the contact flow.
2. Publish concise case studies with authentic screenshots, live demos and actual client outcomes.
3. Add real client testimonials with permission after completed work.

## Implementation notes
Native `details` gives case studies keyboard support. Labels, semantic landmarks, live status messages, skip link and visible focus styles support accessibility. No fabricated proficiency bars or client endorsements. The form uses HTML constraint validation, a hidden honeypot, duplicate-send guard, response checking and a 15-second timeout. User input is never rendered as HTML. Direct contact links work independently of the form.

Google Fonts uses display=swap and fallbacks. There are no heavy animation packages or unnecessary in-page photos. The inventory illustration is a clearly labelled capability overview, not an invented screenshot. The social preview is a real bundled PNG. Layout reservations prevent photo shifts. Theme selection runs before rendering to reduce flashes.

Form integration reference: https://docs.web3forms.com/how-to-guides/js-frameworks/react-js/react-js

## File tree
See `FILE_TREE.txt` for the complete packaged tree. All application source, assets, lockfile, deployment configuration and this guide are included. `dist` and node_modules are deliberately excluded: reproduce them with npm ci and npm run build.
