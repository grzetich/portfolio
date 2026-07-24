export default function (eleventyConfig) {
  // Static passthrough: served verbatim, never templated
  const passthrough = ["assets", "yobitel", "resume.json", "resume_api.py",
    "robots.txt", "feat-api.md", "CLAUDE.md", "GEMINI.md", "llms.txt"];
  for (const p of passthrough) {
    eleventyConfig.addPassthroughCopy(p);
    eleventyConfig.ignores.add(p.includes(".") ? p : `${p}/**`);
  }

  // Jekyll filter compatibility
  eleventyConfig.addFilter("relative_url", (v) => v);
  eleventyConfig.addFilter("absolute_url", (v) => new URL(v || "/", "https://grzeti.ch").href);

  return {
    dir: {
      input: ".",
      includes: "_includes",
      layouts: "_layouts",
      data: "_data",
      output: "_site"
    },
    markdownTemplateEngine: "liquid",
    htmlTemplateEngine: "liquid"
  };
}
