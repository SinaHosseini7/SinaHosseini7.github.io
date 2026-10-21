/* Sina Hosseini site: theme toggle and mobile menu only (blueprint 9.2, 9.3). No dependencies. */
(function () {
  "use strict";

  var root = document.documentElement;
  var KEY = "theme";
  var userChose = false;

  function readStored() {
    try {
      var v = window.localStorage.getItem(KEY);
      return v === "light" || v === "dark" ? v : null;
    } catch (e) {
      return null;
    }
  }

  function store(value) {
    try {
      window.localStorage.setItem(KEY, value);
    } catch (e) {
      /* Storage blocked: the choice lasts for this page only. */
    }
  }

  var media = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function currentTheme() {
    var t = root.getAttribute("data-theme");
    if (t === "light" || t === "dark") return t;
    return media && media.matches ? "dark" : "light";
  }

  function syncToggles() {
    var dark = currentTheme() === "dark";
    var buttons = document.querySelectorAll(".theme-toggle");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute("aria-pressed", dark ? "true" : "false");
    }
  }

  function applyTheme(t) {
    root.setAttribute("data-theme", t);
    syncToggles();
  }

  /* 1. Follow live system changes until the visitor has chosen a theme. */
  if (readStored()) userChose = true;
  function onSystemChange(e) {
    if (userChose || readStored()) return;
    applyTheme(e.matches ? "dark" : "light");
  }
  if (media) {
    if (media.addEventListener) media.addEventListener("change", onSystemChange);
    else if (media.addListener) media.addListener(onSystemChange);
  }

  function initThemeToggle() {
    syncToggles();
    var buttons = document.querySelectorAll(".theme-toggle");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].addEventListener("click", function () {
        var next = currentTheme() === "dark" ? "light" : "dark";
        userChose = true;
        store(next);
        applyTheme(next);
      });
    }
  }

  /* 2. Mobile menu. */
  function initMenu() {
    var header = document.querySelector(".site-header");
    var button = document.querySelector(".nav-toggle");
    if (!header || !button) return;
    var menu = document.getElementById(button.getAttribute("aria-controls"));
    var labelOpen = button.getAttribute("data-label-open");
    var labelClose = button.getAttribute("data-label-close");

    function isOpen() {
      return button.getAttribute("aria-expanded") === "true";
    }

    function setOpen(open, returnFocus) {
      button.setAttribute("aria-expanded", open ? "true" : "false");
      if (labelOpen && labelClose) button.setAttribute("aria-label", open ? labelClose : labelOpen);
      header.classList.toggle("is-open", open);
      if (!open && returnFocus) button.focus();
    }

    button.addEventListener("click", function () {
      setOpen(!isOpen(), false);
    });

    document.addEventListener("keydown", function (e) {
      if ((e.key === "Escape" || e.key === "Esc") && isOpen()) {
        setOpen(false, true);
      }
    });

    document.addEventListener("click", function (e) {
      if (isOpen() && !header.contains(e.target)) setOpen(false, false);
    });

    /* Keyboard: Tab past the last menu link (or Shift+Tab out of the header) closes the menu,
       so focus never lands under the open panel. */
    header.addEventListener("focusout", function (e) {
      if (isOpen() && e.relatedTarget && !header.contains(e.relatedTarget)) setOpen(false, false);
    });

    if (menu) {
      menu.addEventListener("click", function (e) {
        if (e.target.closest && e.target.closest("a")) setOpen(false, false);
      });
    }

    /* Close the menu when the inline menu takes over (wider screen or rotation). */
    var wide = window.matchMedia ? window.matchMedia("(min-width: 45em)") : null;
    function onWide() {
      if (wide.matches && isOpen()) setOpen(false, false);
    }
    if (wide) {
      if (wide.addEventListener) wide.addEventListener("change", onWide);
      else if (wide.addListener) wide.addListener(onWide);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initThemeToggle();
      initMenu();
    });
  } else {
    initThemeToggle();
    initMenu();
  }
})();
