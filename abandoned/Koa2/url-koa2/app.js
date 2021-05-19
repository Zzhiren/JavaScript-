const Koa = require('koa');
const router = require('koa-router')();// 注意require('koa-router')反悔的是函数
const bodyParser = require('koa-bodyparser');
const controller = require('./controller');
// 创建一个Koa对象表示web app本身
const app = new Koa();


// 对于任何请求，app将调用该异步函数处理请求
app.use(async (ctx, next) => {
  console.log(`${ctx.request.method} ${ctx.request.url}`); //打印url
  await next(); //调用下一个middleware
})

app.use(bodyParser());
app.use(controller());

// add router middleware
app.use(router.routes())

app.listen(30003);

console.log('app started at port 30003...');