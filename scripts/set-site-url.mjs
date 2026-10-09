import {readFileSync,writeFileSync} from 'node:fs';
const input=process.argv[2];if(!input)throw new Error('Usage: node scripts/set-site-url.mjs https://your-domain.com');
const url=new URL(input);if(!['https:','http:'].includes(url.protocol))throw new Error('HTTP(S) URL required');
const target=url.href.replace(/\/$/,'');
for(const file of ['index.html','public/robots.txt','public/sitemap.xml']){const content=readFileSync(file,'utf8');const old=file==='index.html'?content.match(/rel="canonical" href="([^"]+)"/)[1].replace(/\/$/,''):null;if(old){writeFileSync('.site-origin',old);}const source=old||readFileSync('.site-origin','utf8');writeFileSync(file,content.replaceAll(source,target));}
