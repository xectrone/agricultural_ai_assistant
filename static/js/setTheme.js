/*
 * Set Theme (dark mode + color theme)
 *
 */

let lHtml = document.documentElement;
let rememberDarkMode = !lHtml.classList.contains("dark-custom-defined");
let rememberTheme = lHtml.classList.contains("remember-theme");

if (rememberDarkMode) {
  // Set Dark mode
  let darkModePreference = localStorage.getItem("dashmixDarkMode");

  if (darkModePreference === "on") {
    lHtml.classList.add("dark");
  } else if (darkModePreference === "off") {
    lHtml.classList.remove("dark");
  } else if (darkModePreference === "system") {
    if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
      lHtml.classList.add("dark");
    } else {
      lHtml.classList.remove("dark");
    }
  }
}

if (rememberTheme) {
  let colorTheme = localStorage.getItem("dashmixColorTheme");

  // Set Color Theme
  if (colorTheme) {
    let themeEl = document.getElementById("css-theme");

    if (themeEl && colorTheme === "default") {
      themeEl.parentNode.removeChild(themeEl);
    } else {
      if (themeEl) {
        themeEl.setAttribute("href", colorTheme);
      } else {
        let themeLink = document.createElement("link");

        themeLink.id = "css-theme";
        themeLink.setAttribute("rel", "stylesheet");
        themeLink.setAttribute("href", colorTheme);

        document
          .getElementById("css-main")
          .insertAdjacentElement("afterend", themeLink);
      }
    }
  }
}
