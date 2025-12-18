# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html
config.load_autoconfig(False)


# COOKIES
config.set("content.cookies.store", False)
config.set("content.cookies.accept", "never")


config.set("url.default_page", "about:blank")
config.set("url.start_pages", "about:blank")

config.set(
    "completion.open_categories",
    ["searchengines", "quickmarks", "bookmarks", "filesystem"],
)
config.set("completion.height", "25%")


# TABS
config.set("tabs.position", "right")
config.set("tabs.width", "12%")


# COLORS
config.set("colors.completion.scrollbar.bg", "#000000")
config.set("colors.completion.scrollbar.fg", "#000000")
config.set("colors.completion.category.bg", "#000000")
config.set("colors.completion.category.fg", "#aa0507")
config.set("colors.completion.category.border.bottom", "#ebe6d3")

config.set("colors.completion.even.bg", "#050505")
config.set("colors.completion.odd.bg", "#000000")
config.set("colors.completion.fg", "#ebe6d3")

config.set("colors.tabs.bar.bg", "#000000")

config.set("colors.webpage.darkmode.enabled", True)
config.set("colors.tabs.even.bg", "black")
config.set("colors.tabs.odd.bg", "black")
config.set("colors.tabs.even.fg", "#ebe6d3")
config.set("colors.tabs.odd.fg", "#ebe6d3")

config.set("colors.tabs.selected.even.bg", "#ebe6d3")
config.set("colors.tabs.selected.odd.bg", "#ebe6d3")
config.set("colors.tabs.selected.odd.fg", "#aa0507")
config.set("colors.tabs.selected.even.fg", "#aa0507")







config.set("content.headers.accept_language", "", "https://matchmaker.krunker.io/*")
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:145.0) Gecko/20100101 Firefox/145.0",
    "https://accounts.google.com/*",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version_short} Safari/{webkit_version}",
    "https://gitlab.gnome.org/*",
)
config.set("content.images", True, "chrome-devtools://*")
config.set("content.images", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome-devtools://*")
config.set("content.javascript.enabled", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome://*/*")
config.set("content.javascript.enabled", True, "qute://*/*")
config.set(
    "content.local_content_can_access_remote_urls",
    True,
    "file:///home/serenityy/.local/share/qutebrowser/userscripts/*",
)
config.set(
    "content.local_content_can_access_file_urls",
    False,
    "file:///home/serenityy/.local/share/qutebrowser/userscripts/*",
)
