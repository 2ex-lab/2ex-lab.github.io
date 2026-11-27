(function () {
  "use strict";

  var root = document.documentElement;
  var themeSelect = document.querySelector("[data-theme-select]");
  var sizeSelect = document.querySelector("[data-text-size-select]");
  var resetButton = document.querySelector("[data-preferences-reset]");
  var status = document.querySelector("[data-preferences-status]");
  var storageKey = "2exlab-reading-preferences";
  var themes = ["light", "dark", "contrast"];
  var sizes = ["normal", "large", "larger", "largest"];

  if (!themeSelect || !sizeSelect || !resetButton) return;

  function apply(theme, size) {
    var safeTheme = themes.indexOf(theme) !== -1 ? theme : "light";
    var safeSize = sizes.indexOf(size) !== -1 ? size : "normal";

    root.setAttribute("data-theme", safeTheme);
    if (safeSize === "normal") {
      root.removeAttribute("data-text-size");
    } else {
      root.setAttribute("data-text-size", safeSize);
    }
    themeSelect.value = safeTheme;
    sizeSelect.value = safeSize;
  }

  function readPreferences() {
    try {
      var saved = window.localStorage.getItem(storageKey);
      return saved ? JSON.parse(saved) : null;
    } catch (error) {
      return null;
    }
  }

  function savePreferences() {
    try {
      window.localStorage.setItem(storageKey, JSON.stringify({
        theme: themeSelect.value,
        size: sizeSelect.value
      }));
    } catch (error) {
      /* The controls still work for this page if storage is unavailable. */
    }
  }

  function announce(message) {
    if (status) status.textContent = message;
  }

  var saved = readPreferences();
  apply(saved && saved.theme, saved && saved.size);

  themeSelect.addEventListener("change", function () {
    apply(themeSelect.value, sizeSelect.value);
    savePreferences();
    announce("Aparência atualizada.");
  });

  sizeSelect.addEventListener("change", function () {
    apply(themeSelect.value, sizeSelect.value);
    savePreferences();
    announce("Tamanho do texto atualizado.");
  });

  resetButton.addEventListener("click", function () {
    apply("light", "normal");
    try {
      window.localStorage.removeItem(storageKey);
    } catch (error) {
      /* Reset remains effective for the current page. */
    }
    announce("Preferências restauradas ao padrão.");
  });
}());
