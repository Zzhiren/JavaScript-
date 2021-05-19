# Webpack知识总结
## config/index.js配置
### index: path.resolve(__dirname, './index1.html'),
__dirname为当前config目录，./index1.html会在当前config目录下生成
### assetsRoot
整个打包文件的根目录 dist
### assetsSubDirectory
被webpack编译处理过的资源文件都会在这个build.assetsRoot目录下,
如果assetsSubDirectory:'./static'，则目录路径为dist/static
### assetsPublicPath
资源的根目录，也就是dist文件所在的目录，
举例：项目目录为demo，assetsPublicPath:'./'，则最后打包目录为demo/dist

例子：
```javascript
// 项目目录为test/demo
1:
 build: {
    // Template for index.html
    index: path.resolve(__dirname, '../../index.html'),
    // Paths
    assetsRoot: path.resolve(__dirname, '../../dist'),
    assetsSubDirectory: './static',
    assetsPublicPath: './dist',
 }
 test
    demo
    dist
      static
    index.html

2:
 build: {
    // Template for index.html
    index: path.resolve(__dirname, '../index.html'),
    // Paths
    assetsRoot: path.resolve(__dirname, '../../dist'),
    assetsSubDirectory: './static',
    assetsPublicPath: './dist',
 }
 test
  demo
    config
    index.html
  dist
    static
```

## 配置vue+scss+pug
### 安装需要的模块
```javascript
npm
// 安装支持pug依赖
npm install pug pug-loader pug-filters -D
// 安装支持scss依赖
npm install sass sass-loader node-sass -D

or yarn
// 安装支持pug依赖
yarn add  pug pug-loader pug-filters --dev
// 安装支持scss依赖
yarn add sass sass-loader node-sass --dev

```
### 配置相关loader
>bulid/webpack.base.conf.js
```javascript
module: {
  rules: [
    {
      test: /\.scss$/,
      loader: 'style-loader!css-loader!sass-loader?sourceMap'
    },
    {
      test: /\.pug$/,
      loader: 'pug'
    }
  ]
}
```
## 配置Scss可以全局引入
```javascript
//build/utils.js
 return {
    css: generateLoaders(),
    postcss: generateLoaders(),
    less: generateLoaders('less'),
    sass: generateLoaders('sass', { indentedSyntax: true }),
    // 加上下面这一段配置，resources为根scss文件路径
    scss: generateLoaders('sass').concat(
      {
        loader: 'sass-resources-loader',
        options: {
          resources: path.resolve(__dirname, '../src/scss/index.scss')
        }
      }
    ),
    stylus: generateLoaders('stylus'),
    styl: generateLoaders('stylus')
  }
}
```
