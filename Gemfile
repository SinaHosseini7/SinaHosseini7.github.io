source "https://rubygems.org"

# GitHub Pages: the same Jekyll (3.10.0) and plugins that GitHub uses to build the site.
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end

# Needed by "jekyll serve" on Ruby 3.x.
gem "webrick", "~> 1.8"

# Removes a notice from the GitHub metadata plugin on every build.
gem "faraday-retry"

# Windows only: time zone data and fast file watching.
platforms :windows, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
gem "wdm", ">= 0.1.0", platforms: :windows
