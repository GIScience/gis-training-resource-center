// Language dropdown (custom-launch-buttons): open the current page in the other language.
//
// In _launch_buttons.yml the items link to "#lang-en", "#lang-fr" and "#lang-es". This script
// replaces them with a relative link to the same page in that book, for example
// fr/Module_2/fr_qgis_basemap.html -> en/Module_2/en_qgis_basemap.html. The books are published
// side by side (/en, /fr, /es), so the links work on any domain. If the page doesn't exist in
// that language, the link opens the book's homepage instead.

(() => {
  const LANGUAGES = ["en", "fr", "es"];
  const MARKER = /#lang-(en|fr|es)$/;

  // Folder of the current book, e.g. https://example.org/site/fr/
  const bookUrl = () => new URL(document.documentElement.dataset.content_root || "./", window.location.href);

  const currentPage = () => {
    // Sphinx declares DOCUMENTATION_OPTIONS with const, so it isn't a property of window.
    const pagename = (typeof DOCUMENTATION_OPTIONS !== "undefined" && DOCUMENTATION_OPTIONS.pagename) || "";
    const slash = pagename.lastIndexOf("/");
    return { dir: pagename.slice(0, slash + 1), name: pagename.slice(slash + 1) };
  };

  const currentLanguage = (name) => {
    const folder = bookUrl().pathname.split("/").filter(Boolean).pop();
    if (LANGUAGES.includes(folder)) return folder;
    const prefix = name.split("_")[0];
    return LANGUAGES.includes(prefix) ? prefix : "en";
  };

  // Possible URLs of the current page in the target language, most likely first.
  // English pages are named en_*.html, except a few such as intro.html; translated pages are
  // named fr_*.html / es_*.html.
  const candidates = (target) => {
    const { dir, name } = currentPage();
    const current = currentLanguage(name);
    if (target === current) return [new URL(window.location.href.split("#")[0])];
    const stem = name.startsWith(`${current}_`) ? name.slice(current.length + 1) : name;
    if (!dir && stem === "intro") return [homepage(target)];
    const names = target === "en" ? [`en_${stem}`, stem] : [`${target}_${stem}`, stem];
    return [...new Set(names)].map((n) => new URL(`../${target}/${dir}${n}.html`, bookUrl()));
  };

  const homepage = (target) =>
    new URL(`../${target}/${target === "en" ? "intro" : `${target}_intro`}.html`, bookUrl());

  const exists = async (url) => {
    try {
      const response = await fetch(url, { method: "HEAD" });
      return response.ok;
    } catch {
      return null; // can't tell, e.g. a page opened from disk (file://)
    }
  };

  const open = async (target) => {
    const urls = candidates(target);
    for (const url of urls) {
      const found = await exists(url);
      if (found === null) return window.location.assign(urls[0]);
      if (found) return window.location.assign(url.href + window.location.hash);
    }
    window.location.assign(homepage(target));
  };

  const setUp = () => {
    document.querySelectorAll("a.dropdown-item").forEach((link) => {
      const match = (link.getAttribute("href") || "").match(MARKER);
      if (!match) return;
      const target = match[1];
      link.dataset.lang = target;
      link.href = candidates(target)[0].href;
      if (target === currentLanguage(currentPage().name)) link.setAttribute("aria-current", "page");
      link.addEventListener("click", (event) => {
        if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey) return;
        event.preventDefault();
        open(target);
      });
    });
  };

  // custom-launch-buttons adds the dropdown on DOMContentLoaded; run after it.
  document.addEventListener("DOMContentLoaded", () => setTimeout(setUp, 0));
})();
