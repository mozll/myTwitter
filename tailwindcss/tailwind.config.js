/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../**/*.html"],
  theme: {
    extend: {
      colors: {
        "twitterGreen": "#00ba7c",
        "twitterDarkGreen" : "#009362",
        "twitterDarkMode" : "#15202b",
        "twitterLessDark" : "#1e2732", 
        "twitterLightDark" : "#273340", 
        "twitterRed" :"#F91880", 
        "twitterBlue" : "#0ea5e9",
      },
    },
  },
  plugins: [],
}
