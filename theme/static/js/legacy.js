// Static hosts cannot route WordPress's /?p=123 URLs on their own.
// Resolve them only at the home page, using paths relative to this script.
(async () => {
  const script = document.currentScript;
  const id = new URLSearchParams(location.search).get('p');
  if (!id || !script) return;
  const root = new URL('../../', script.src);
  if (location.pathname !== root.pathname && location.pathname !== root.pathname + 'index.html') return;
  try {
    const response = await fetch(new URL('legacy-posts.json', root));
    if (!response.ok) return;
    const posts = await response.json();
    if (Object.hasOwn(posts, id)) location.replace(new URL(posts[id], root).href + location.hash);
  } catch (error) {
    console.warn('Could not resolve the old WordPress link.', error);
  }
})();
