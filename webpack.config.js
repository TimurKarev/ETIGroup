const path = require('path');

const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  mode: 'development',
  entry: './assets/index.js',  // path to our input file
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static'),  // path to our Django static directory
    publicPath: "/static/"
  },
  devServer: {
    contentBase: path.resolve(__dirname, './static'),
    writeToDisk: true,
    proxy: {
     '!/static/**': {
        //target: 'http://localhost:8000', // points to django dev server
        target: 'https://etiotk.herokuapp.com/',
        changeOrigin: true,
      },
    }
  },
  resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        },
        extensions: ['*', '.js', '.vue', '.json']
    },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
         extractCSS: process.env.NODE_ENV === 'production'
        }
      },
      // this will apply to both plain `.js` files
      // AND `<script>` blocks in `.vue` files
      {
        test: /\.js$/,
        use: ['babel-loader', 'vue-hot-reload-loader']
      },
      // this will apply to both plain `.css` files
      // AND `<style>` blocks in `.vue` files
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          {
            loader: 'css-loader',
            options: {
              esModule: false
            }
          }
        ]
      },
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              implementation: require('sass'),
              sassOptions: {
                indentedSyntax: true // optional
              }
            }
          },
        ]
      },
            {
        test: /\.(eot|svg|ttf|woff|woff2|png|)$/i,
        loader: 'url-loader'
      },

    ]
  },
  plugins: [
    // make sure to include the plugin for the magic
    new VueLoaderPlugin(),
  ]
}