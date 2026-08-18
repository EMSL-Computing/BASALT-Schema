// "Schema Visualizer" nav entry -> the standalone schema explorer, in a new tab.
//
// The nav entry in mkdocs.yml has to be an absolute URL (MkDocs only accepts
// Markdown pages or external links in `nav`, and the explorer is a static HTML
// file under docs/files/). That absolute URL is correct for the published site
// but wrong under `mkdocs serve`, so rewrite it against the site root that
// mkdocs-material reports in its `#__config` block. Setting `target` also makes
// Material's instant-loading skip the link instead of swapping it in place.

(function () {
  var LABEL = "Schema Visualizer";
  var TARGET = "files/schema-explorer.html";

  function siteRoot() {
    var cfg = document.getElementById("__config");
    if (!cfg) return null;
    try {
      var base = JSON.parse(cfg.textContent).base;
      if (!base) return null;
      return new URL(base.replace(/\/?$/, "/"), window.location.href).href;
    } catch (e) {
      return null;
    }
  }

  function patch() {
    var root = siteRoot();
    var links = document.querySelectorAll(".md-nav a, .md-tabs a");
    Array.prototype.forEach.call(links, function (a) {
      if (a.textContent.replace(/\s+/g, " ").trim() !== LABEL) return;
      if (root) a.href = root + TARGET;
      a.target = "_blank";
      a.rel = "noopener";
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(patch); // fires now and after each instant nav
  } else {
    document.addEventListener("DOMContentLoaded", patch);
  }
})();
