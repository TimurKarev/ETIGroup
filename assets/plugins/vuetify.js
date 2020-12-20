import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify)

const opts = {
    theme: {
    themes: {
      light: {
        primary: colors.grey.lighten1, // #E53935
        secondary: colors.black, // #FFCDD2
        accent: colors.pink.darken4, // #3F51B5
      },
    },
  },
}

export default new Vuetify(opts)