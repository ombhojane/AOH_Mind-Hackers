/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./*.{html,js}", "./!(build|dist|.*)/**/*.{html,js}"],
    theme: {
      extend: {
        colors: {
          gray: "#171515",
          maroon: "#620000",
          white: "#fff",
          firebrick: "#a51010",
          darkblue: "#14008c",
        },
        spacing: {},
        fontFamily: {
          jejugothic: "JejuGothic",
          mada: "Mada",
          comfortaa: "Comfortaa",
        },
        borderRadius: {
          "41xl": "60px",
        },
      },
      fontSize: {
        "4xl": "23px",
        "10xl": "29px",
        "79xl": "98px",
        "30xl": "49px",
        inherit: "inherit",
      },
      screens: {
        lg: {
          max: "1200px",
        },
        mq1050: {
          raw: "screen and (max-width: 1050px)",
        },
        mq750: {
          raw: "screen and (max-width: 750px)",
        },
        mq450: {
          raw: "screen and (max-width: 450px)",
        },
      },
    },
    corePlugins: {
      preflight: false,
    },
  };
  