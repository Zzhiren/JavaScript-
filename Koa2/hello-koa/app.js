const Koa = require('koa');

// 创建一个Koa对象表示web app本身
const app = new Koa();

// 对于任何请求，app将调用该异步函数处理请求
app.use(async (ctx, next) => {
  // await next();
  // ctx.response.type = 'text/html';
  // ctx.response.body = '<h1>Hello, Koa2!</h1>';
  console.log(`${ctx.request.method} ${ctx.request.url}`); //打印url
  await next(); //调用下一个middleware
})

app.use(async (ctx, next) =>{
  const start = new Date().getTime(); // 当前时间
  await next(); //调用下一个middleware
  const ms = new Date().getTime() - start; //耗时时间
  console.log(`Time: ${ms}ms`); //打印耗费时间
});

app.use(async (ctx, next) => {
  await next();
  ctx.response.type = 'text/html';
  ctx.response.body = '<h1>Hello, Koa2!</h1>';
})

app.listen(30003);

console.log('app started at port 30003...');