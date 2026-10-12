// Render the header repository facts ourselves so the version shows the latest
// git *tag* instead of Material's latest GitHub *Release*.
//
// Material's own fetch is disabled in overrides/partials/source.html (the
// data-md-component="source" hook is removed there), so this script owns the
// facts list entirely. We render into `.md-source__repository`, which is
// present in the server HTML from the first paint, so there is no race and no
// wrong-value flash. Facts are cached in sessionStorage, so repeat views and
// instant-navigation page swaps render immediately from cache.
document$.subscribe(function () {
  var REPO = "EMSL-Computing/BASALT-Schema";
  var CACHE_KEY = "basalt_source_facts";

  var box = document.querySelector(".md-source__repository");
  if (!box) return;

  // Material formats large counts as e.g. "1.2k"; mirror that for stars/forks.
  var fmt = function (n) {
    if (typeof n !== "number") return n;
    if (n >= 1e4) return Math.round(n / 1e3) + "k";
    if (n >= 1e3) return (n / 1e3).toFixed(1).replace(/\.0$/, "") + "k";
    return String(n);
  };

  var render = function (facts) {
    var old = box.querySelector(".md-source__facts");
    if (old) old.remove();
    var ul = document.createElement("ul");
    ul.className = "md-source__facts";
    var add = function (mod, val) {
      if (val === undefined || val === null || val === "") return;
      var li = document.createElement("li");
      li.className = "md-source__fact md-source__fact--" + mod;
      li.textContent = val;
      ul.appendChild(li);
    };
    add("version", facts.version);
    add("stars", fmt(facts.stars));
    add("forks", fmt(facts.forks));
    if (ul.childNodes.length) box.appendChild(ul);
  };

  // Instant render from cache (no flash on repeat views / page swaps).
  try {
    var cached = sessionStorage.getItem(CACHE_KEY);
    if (cached) render(JSON.parse(cached));
  } catch (e) { /* sessionStorage unavailable; fall through to fetch */ }

  // Refresh from GitHub: /repos gives stars+forks, /tags gives the newest tag.
  Promise.all([
    fetch("https://api.github.com/repos/" + REPO).then(function (r) { return r.ok ? r.json() : {}; }),
    fetch("https://api.github.com/repos/" + REPO + "/tags").then(function (r) { return r.ok ? r.json() : []; })
  ]).then(function (res) {
    var meta = res[0] || {};
    var tags = res[1] || [];
    var facts = {
      version: tags.length ? tags[0].name : undefined,
      stars: typeof meta.stargazers_count === "number" ? meta.stargazers_count : undefined,
      forks: typeof meta.forks_count === "number" ? meta.forks_count : undefined
    };
    try { sessionStorage.setItem(CACHE_KEY, JSON.stringify(facts)); } catch (e) {}
    render(facts);
  }).catch(function () { /* offline / rate-limited: keep whatever cache showed */ });
});
