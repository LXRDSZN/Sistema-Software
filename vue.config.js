module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      },
      '/src/assets': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        pathRewrite: {
          '^/src/assets': '/src/assets'
        }
      }
    }
  }
}
